#!/usr/bin/env python

# Include a few standard libraries.
import csv
import sys
import json

# Start our JSON output.
print '['

# Iterate through the CSV file.
num_rows = 0

"""
Unfortunately, this uses a dictionary, which means that the values of the CSV
file are all mixed up. We'll want to modify this to preserve the order of the
columns. http://stackoverflow.com/a/1885353
"""
for obj in csv.DictReader(sys.stdin):
	if num_rows > 0:
		print ','
	print json.dumps(obj)
	num_rows += 1

# Conclude our JSON output.
print ']'
