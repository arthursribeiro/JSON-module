import decimal
import unittest
from unittest import TestCase
from io import StringIO
from contextlib import contextmanager

import JSONModule
import decoder
import scanner
from collections import OrderedDict


@contextmanager
def use_python_scanner():
    py_scanner = scanner.py_make_scanner
    old_scanner = decoder.make_scanner
    decoder.make_scanner = py_scanner
    try:
        yield
    finally:
        decoder.make_scanner = old_scanner


class TestDecode(TestCase):
    def test_decimal(self):
        rval = JSONModule.loads('1.1', parse_float=decimal.Decimal)
        self.assertTrue(isinstance(rval, decimal.Decimal))
        self.assertEqual(rval, decimal.Decimal('1.1'))

    def test_float(self):
        rval = JSONModule.loads('1', parse_int=float)
        self.assertTrue(isinstance(rval, float))
        self.assertEqual(rval, 1.0)

    def test_object_pairs_hook(self):
        s = '{"xkd":1, "kcw":2, "art":3, "hxm":4, "qrt":5, "pad":6, "hoy":7}'
        p = [("xkd", 1), ("kcw", 2), ("art", 3), ("hxm", 4),
             ("qrt", 5), ("pad", 6), ("hoy", 7)]
        self.assertEqual(JSONModule.loads(s), eval(s))
        self.assertEqual(JSONModule.loads(s, object_pairs_hook = lambda x: x), p)
        self.assertEqual(JSONModule.load(StringIO(s),
                                   object_pairs_hook=lambda x: x), p)
        od = JSONModule.loads(s, object_pairs_hook = OrderedDict)
        self.assertEqual(od, OrderedDict(p))
        self.assertEqual(type(od), OrderedDict)
        # the object_pairs_hook takes priority over the object_hook
        self.assertEqual(JSONModule.loads(s,
                                    object_pairs_hook = OrderedDict,
                                    object_hook = lambda x: None),
                         OrderedDict(p))

    def test_decoder_optimizations(self):
        # Several optimizations were made that skip over calls to
        # the whitespace regex, so this test is designed to try and
        # exercise the uncommon cases. The array cases are already covered.
        rval = JSONModule.loads('{   "key"    :    "value"    ,  "k":"v"    }')
        self.assertEqual(rval, {"key":"value", "k":"v"})

    def check_keys_reuse(self, source, loads):
        rval = loads(source)
        (a, b), (c, d) = sorted(rval[0]), sorted(rval[1])
        self.assertIs(a, c)
        self.assertIs(b, d)

    def test_keys_reuse(self):
        s = '[{"a_key": 1, "b_\xe9": 2}, {"a_key": 3, "b_\xe9": 4}]'
        self.check_keys_reuse(s, JSONModule.loads)
        # Disabled: the pure Python version of json simply doesn't work
        with use_python_scanner():
            self.check_keys_reuse(s, decoder.JSONDecoder().decode)

if __name__ == '__main__':
    unittest.main()
