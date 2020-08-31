# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import shutil
import unittest
from src.pypdm.assist.cfg import *
from src.pypdm import builder
from src.pypdm.dbc._sqlite import SqliteDBC

DB_PATH =  'data/sqlite/test.db'
DB_CONN = SqliteDBC(DB_PATH)
CACHE_ROOT_DIR = 'src'


class TestPypdmSqlite(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        DB_CONN.exec_script('data/init_db.sql')

    @classmethod
    def tearDownClass(cls) :
        DB_CONN.exec_script('data/rollback_db.sql')
        # if os.path.exists(CACHE_ROOT_DIR) :
        #     shutil.rmtree(CACHE_ROOT_DIR)

    def setUp(self) :
        pass

    def tearDown(self) :
        pass

    def test_build_pdm(self) :
        paths = builder.build(
            dbtype = SQLITE,
            dbname = DB_PATH,
            pdm_pkg = 'src.pdm.sqlite',
            table_whitelist = [ 't_teachers', 't_students' ],
            table_blacklist = [ 't_employers', 't_employees' ],
            to_log = True
        )
        self.assertEqual(len(paths), 4)
        self.assertTrue('src/pdm/sqlite/bean/t_teachers.py' in paths)
        self.assertTrue('src/pdm/sqlite/dao/t_teachers.py' in paths)
        self.assertTrue('src/pdm/sqlite/bean/t_students.py' in paths)
        self.assertTrue('src/pdm/sqlite/dao/t_students.py' in paths)


    def test_insert(self) :
        from tests.src.pdm.sqlite.dao.t_teachers import TTeachersDao
        dao = TTeachersDao()
        beans = dao.query_all(DB_CONN)
        for bean in beans :
            print(bean)




if __name__ == '__main__':
    unittest.main()



