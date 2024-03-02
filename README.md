# JsonCleaner

## Description

JsonCleaner is a program that rewrites a JSON file into a readable format.

__Example :__

```json
[{"test":98765678,"text":"This is a text containing special characters {][]}","object":{"name":"Henry","letters":["H","e","n","r","y"]},"list":[1,2,3,4,5],"emptyList":[],"emptyObject":{}}]
```

becomes:

```json
[
	{
		"test": 98765678,
		"text": "This is a text containing special characters {][]}",
		"object": {
			"name": "Henry",
			"letters": [
				"H",
				"e",
				"n",
				"r",
				"y"
			]
		},
		"list": [
			1,
			2,
			3,
			4,
			5
		],
		"emptyList": [],
		"emptyObject": {}
	}
]
```

## Use

```shell
python3 json-cleaner.py [JSON FILE PATH]
```

The execution is aborted when :
- A file path wasn't provided
- The file is not found
- The content of the file isn't a syntax correct JSON to begin with.