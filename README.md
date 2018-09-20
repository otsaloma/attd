Attribute Dictionary
====================

[![Build Status](https://travis-ci.org/otsaloma/attd.svg)](https://travis-ci.org/otsaloma/attd)

attd is a Python module that provides a dictionary with attribute access
to keys. It is especially convenient when working with deeply nested
data from JSON APIs.

## Installation

```bash
pip install attd
```

## Documentation

```python
>>> import attd
>>> data = attd.Dictionary({"a": {"b": {"c": 1}}})
>>> data["a"]["b"]["c"]
1
>>> data.a.b.c
1
>>> data = attd.FallbackDictionary({})
>>> data["a"]["b"]["c"]
FallbackDictionary()
>>> data.a.b.c
FallbackDictionary()
```

Check the source code for details – it's short and should be fairly
self-explanatory.
