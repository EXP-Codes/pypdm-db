# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from src.pypdm import *


class TestSimple(unittest.TestCase):

    def test_build(self):
        whitelist = [ 't_cves' ]
        dbname = 'D:\\workspace\\Github\\threat-broadcast\\tpls\\cves.db'
        # self.assertEqual(build(5), 6)


if __name__ == '__main__':
    unittest.main()

