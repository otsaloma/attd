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

from attd import AttributeDict
from attd import FallbackAttributeDict


class TestAttributeDict:

    def setup_method(self, method):
        self.ad = AttributeDict()

    def test___delattr__(self):
        self.ad.test = 1
        assert "test" in self.ad
        assert hasattr(self.ad, "test")
        del self.ad.test
        assert "test" not in self.ad
        assert not hasattr(self.ad, "test")

    def test___getattr__(self):
        self.ad.test = 1
        assert self.ad.test == 1
        assert self.ad.test is self.ad["test"]

    def test___setattr__(self):
        self.ad.test = 1
        assert self.ad.test == 1
        assert self.ad.test is self.ad["test"]

    def test___setattr____conflict(self):
        self.ad.items = []
        assert callable(self.ad.items)

    def test___setattr____nested(self):
        self.ad.test = {"test": {"nested": 1}}
        assert self.ad.test.test.nested == 1

    def test___setitem__(self):
        self.ad["test"] = 1
        assert self.ad["test"] == 1
        assert self.ad.test is self.ad["test"]

    def test_copy(self):
        self.ad.test = "test"
        adc = self.ad.copy()
        assert adc == self.ad
        assert adc is not self.ad

    def test_setdefault(self):
        self.ad.setdefault("test", 1)
        assert self.ad["test"] == 1
        assert self.ad.test is self.ad["test"]

    def test_setdefault__nested(self):
        self.ad.test = {"test": {"nested": 1}}
        assert self.ad.test.test.nested == 1

    def test_update(self):
        self.ad.update({"test": 1})
        assert self.ad["test"] == 1
        assert self.ad.test is self.ad["test"]

    def test_update__nested(self):
        self.ad.update({"test": {"nested": 1}})
        assert self.ad.test.nested == 1

    def test_from_json(self):
        test = AttributeDict.from_json('{"test": 1}')
        assert isinstance(test, AttributeDict)
        assert test == {"test": 1}

    def test_to_json(self):
        self.ad.test = 1
        test = self.ad.to_json()
        test = AttributeDict.from_json(test)
        assert test == self.ad


class TestFallbackAttributeDict:

    def setup_method(self, method):
        self.ad = FallbackAttributeDict()

    def test___getattr__(self):
        assert self.ad.a.b.c == {}

    def test___getitem__(self):
        assert self.ad["a"]["b"]["c"] == {}
