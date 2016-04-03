Python 3 script to convert DSpace search results saved in CSV format to a simple XML
representation, using [tablib](http://tablib.readthedocs.org/) for processing
the CSV data and minidom for building and outputting the XML document.

(I once needed to harvest some records from a repository for which I didn't
have backend access to export data, and needed more fields and granularity than
could be retrieved via OAI-PMH.)

Where the CSV source concatenates multiple instances of the same metadata
element (e.g. dc.contributor.author) into a single column/field with values
separated by '||', these are split back into separate repeated elements in the
XML output. Also, junk '[en]' suffixes in column names are stripped.

Takes filename of CSV source file as an argument and outputs to same base name
with .xml extension (foo.csv -> foo.xml).
