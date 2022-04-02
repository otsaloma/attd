Attribute Dictionary
====================

[![Test](https://github.com/otsaloma/attd/workflows/Test/badge.svg)](https://github.com/otsaloma/attd/actions)
[![PyPI](https://img.shields.io/pypi/v/attd.svg)](https://pypi.org/project/attd/)
[![Downloads](https://pepy.tech/badge/attd/month)](https://pepy.tech/project/attd)

attd is a Python package that provides a dictionary with attribute
access to keys. It is especially convenient when working with deeply
nested data from JSON APIs.

## Installation

```bash
# Latest stable version
pip install -U attd

# Latest development version
pip install -U git+https://github.com/otsaloma/attd
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
>>> data = FallbackAttributeDict()
>>> data["a"]["b"]["c"]
{}
>>> data.a.b.c
{}
```
