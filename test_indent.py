import unittest
from unittest import TestCase

import JSONModule
import json
import textwrap

class TestIndent(TestCase):
    def test_indent(self):
        h = [['blorpie'], ['whoops'], [], 'd-shtaeou', 'd-nthiouh', 'i-vhbjkhnth',
             {'nifty': 87}, {'field': 'yes', 'morefield': False} ]

        expect = textwrap.dedent("""\
        [
        \t[
        \t\t"blorpie"
        \t],
        \t[
        \t\t"whoops"
        \t],
        \t[],
        \t"d-shtaeou",
        \t"d-nthiouh",
        \t"i-vhbjkhnth",
        \t{
        \t\t"nifty": 87
        \t},
        \t{
        \t\t"field": "yes",
        \t\t"morefield": false
        \t}
        ]""")


        d1 = JSONModule.dumps(h)
        d2 = JSONModule.dumps(h, indent=2, sort_keys=True, separators=(',', ': '))
        d3 = JSONModule.dumps(h, indent='\t', sort_keys=True, separators=(',', ': '))

        h1 = JSONModule.loads(d1)
        h2 = JSONModule.loads(d2)
        h3 = JSONModule.loads(d3)

        self.assertEqual(h1, h)
        self.assertEqual(h2, h)
        self.assertEqual(h3, h)
        self.assertEqual(d2, expect.expandtabs(2))
        self.assertEqual(d3, expect)

if __name__ == '__main__':
    unittest.main()
