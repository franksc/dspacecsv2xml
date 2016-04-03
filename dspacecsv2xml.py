#!/usr/bin/env python3

"""
Convert DSpace search results CSV to XML
"""

import argparse, os
import re
import tablib
import xml.dom.minidom as minidom

def addsubelement(document, parent, element, value):
    element = re.sub(r"\[en\]", "", element)
    subelement = document.createElement(element)
    subelement.appendChild(document.createTextNode(value))
    parent.appendChild(subelement)

def processrow(root, document, data, row):
    record = document.createElement("record")
    root.appendChild(record)

    for header in data.headers:
        if data[header][row]:
            if re.search(r"\|\|", data[header][row]):
                for s in re.split("\|\|", data[header][row]):
                    addsubelement(document, record, header, s)
            else:
                addsubelement(document, record, header, data[header][row])

def main():
    parser = argparse.ArgumentParser(description="Convert DSpace search results CSV to XML")
    parser.add_argument("infilename", help="CSV source file")
    args = parser.parse_args()

    data = tablib.Dataset()
    with open(args.infilename, "r") as f:
        data.csv = f.read()

    document = minidom.getDOMImplementation().createDocument(None, "records", None)
    root = document.documentElement

    for row in range(data.height):
        processrow(root, document, data, row)

    outfile = open(os.path.splitext(os.path.basename(args.infilename))[0] + ".xml", "w")
    print(document.toprettyxml(), file=outfile)

if __name__ == "__main__":
    main()
