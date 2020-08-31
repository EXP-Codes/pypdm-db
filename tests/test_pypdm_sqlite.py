# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
from src.pypdm.assist.cfg import *
from src.pypdm import builder
from src.pypdm.dbc._sqlite import SqliteDBC

DB_PATH =  'data/sqlite/test.db'
DB_CONN = SqliteDBC(DB_PATH)


class TestPypdmSqlite(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        DB_CONN.exec_script('data/init_db.sql')

    @classmethod
    def tearDownClass(cls) :
        DB_CONN.exec_script('data/rollback_db.sql')

    def setUp(self) :
        pass

    def tearDown(self) :
        pass

    def test_build_pdm(self) :
        rst = builder.build(
            dbtype = SQLITE,
            dbname = DB_PATH,
            pdm_pkg = 'src.pdm.sqlite',
            table_whitelist = [],
            table_blacklist = [ 't_employers', 't_employees' ],
            to_log = True
        )
        print(rst)
        # self.assertEqual(rst, True)

    def test_bbb(self) :
        print('vvv')


if __name__ == '__main__':
    unittest.main()



