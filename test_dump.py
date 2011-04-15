import unittest
from unittest import TestCase
from io import StringIO

import JSONModule

class TestDump(TestCase):
    def test_dump(self):
        sio = StringIO()
        JSONModule.dump({}, sio)
        self.assertEqual(sio.getvalue(), '{}')

    def test_dumps(self):
        self.assertEqual(JSONModule.dumps({}), '{}')

    def test_encode_truefalse(self):
        self.assertEqual(JSONModule.dumps(
                 {True: False, False: True}, sort_keys=True),
                 '{"false": true, "true": false}')
        self.assertEqual(JSONModule.dumps(
                {2: 3.0, 4.0: 5, False: 1, 6: True}, sort_keys=True),
                '{"false": 1, "2": 3.0, "4.0": 5, "6": true}')

if __name__ == '__main__':
    unittest.main()
