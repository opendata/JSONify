#!/usr/bin/env python

# Include a few standard libraries.
import csv
import sys
import json

# Start our JSON output.

# Iterate through the CSV file.
result = []
"""
Unfortunately, this uses a dictionary, which means that the values of the CSV
file are all mixed up. We'll want to modify this to preserve the order of the
columns. http://stackoverflow.com/a/1885353
"""
for obj in csv.DictReader(sys.stdin, skipinitialspace=True):
    result.append(obj)

# Conclude our JSON output.
print json.dumps(result, indent=2)
