import unittest
from unittest import TestCase

import JSONModule

class TestDefault(TestCase):
    def test_default(self):
        self.assertEqual(
            JSONModule.dumps(type, default=repr),
            JSONModule.dumps(repr(type)))

if __name__ == '__main__':
    unittest.main()
