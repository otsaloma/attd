Attribute Dictionary
====================

[![Build Status](https://travis-ci.org/otsaloma/attd.svg)](https://travis-ci.org/otsaloma/attd)
[![PyPI](https://img.shields.io/pypi/v/attd.svg)](https://pypi.org/project/attd/)

attd is a Python module that provides a dictionary with attribute access
to keys. It is especially convenient when working with deeply nested
data from JSON APIs.

## Installation

```bash
pip install attd
```

## Documentation

```python
>>> from attd import AttributeDict
>>> data = AttributeDict({"a": {"b": {"c": 1}}})
>>> data["a"]["b"]["c"]
1
>>> data.a.b.c
1
>>> from attd import FallbackAttributeDict
>>> data = FallbackAttributeDict({})
>>> data["a"]["b"]["c"]
FallbackAttributeDict()
>>> data.a.b.c
FallbackAttributeDict()
```

Check the source code for details – it's short and should be fairly
self-explanatory.
