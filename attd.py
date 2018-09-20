# -*- coding: utf-8 -*-

# Copyright (c) 2017 Osmo Salomaa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""Dictionary with attribute access to keys."""

import collections
import functools
import json
import keyword
import sys

__all__ = ("Dictionary", "FallbackDictionary")


def translate_error(fm, to):
    def outer_wrapper(function):
        @functools.wraps(function)
        def inner_wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except fm as error:
                raise to(str(error))
        return inner_wrapper
    return outer_wrapper


class Dictionary(collections.OrderedDict):

    """Dictionary with attribute access to keys."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.items():
            setattr(self, key, value)

    def __coerce(self, value):
        if isinstance(value, Dictionary):
            # Assume all children are Dictionaries as well.
            # This allows us to do a fast Dictionary(x) to
            # ensure that we have attribute access.
            return value
        if isinstance(value, dict):
            return Dictionary(value)
        if isinstance(value, (list, tuple, set)):
            items = map(self.__coerce, value)
            return type(value)(items)
        return value

    @translate_error(KeyError, AttributeError)
    def __delattr__(self, name):
        return self.__delitem__(name)

    @translate_error(KeyError, AttributeError)
    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setattr__(self, name, value):
        if not isinstance(name, str):
            # Fail silently for non-string keys.
            return
        if not name.isidentifier() or keyword.iskeyword(name):
            # Warn if trying to set an invalid attribute name.
            message = "Not adding attribute {!r}"
            return print(message.format(name), file=sys.stderr)
        if name in dir(collections.OrderedDict):
            # Warn if trying to override standard methods.
            message = "Not overriding attribute {!r}"
            return print(message.format(name), file=sys.stderr)
        return self.__setitem__(name, value)

    def __setitem__(self, key, value):
        value = self.__coerce(value)
        return super().__setitem__(key, value)

    def copy(self):
        return self.__class__(super().copy())

    def setdefault(self, key, default=None):
        default = self.__coerce(default)
        return super().setdefault(key, default)

    def update(self, *args, **kwargs):
        other = Dictionary(*args, **kwargs)
        return super().update(other)

    # Non-standard methods:

    @classmethod
    def from_json(cls, string, **kwargs):
        obj = json.loads(string, **kwargs)
        if not isinstance(obj, dict):
            raise TypeError("Not a dictionary")
        return cls(obj)

    def to_json(self, **kwargs):
        kwargs.setdefault("ensure_ascii", False)
        kwargs.setdefault("indent", 2)
        return json.dumps(self, **kwargs)


class FallbackDictionary(Dictionary):

    """Attribute dictionary returning {} for missing keys."""

    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        return FallbackDictionary({})
