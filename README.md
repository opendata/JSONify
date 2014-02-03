# JSONify

It turns CSV into JSON. By operating on an incoming stream of data, rather than parsing an entire file at once, it can handle even very large CSV files.

## Usage

```
cat records.csv | jsonify.py > records.json
```
