# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from src import pypdm


class TestSimple(unittest.TestCase):

    def setUp(self) :
        pass

    def tearDown(self) :
        pass

    def test_build(self) :
        rst = pypdm.build(
            dbtype = 'sqlite',
            dbname = 'data/sqlite.db',
            table_whitelist = [ 't_cves' ]
        )
        self.assertEqual(rst, True)


if __name__ == '__main__':
    unittest.main()


