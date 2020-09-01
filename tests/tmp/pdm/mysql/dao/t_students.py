#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# DAO: t_students
# -------------------------------

from ..bean.t_students import TStudents
from pypdm.dao._base import BaseDao


class TStudentsDao(BaseDao) :
    TABLE_NAME = 't_students'
    SQL_COUNT = 'select count(1) from t_students'
    SQL_TRUNCATE = 'truncate table t_students'
    SQL_INSERT = 'insert into t_students(s_name, s_remark) values(%s, %s)'
    SQL_DELETE = 'delete from t_students where 1 = 1 '
    SQL_UPDATE = 'update t_students set s_name = %s, s_remark = %s where 1 = 1 '
    SQL_SELECT = 'select i_id, s_name, s_remark from t_students where 1 = 1 '

    def __init__(self) :
        BaseDao.__init__(self)

    def _to_bean(self, row) :
        bean = None
        if row:
            bean = TStudents()
            bean.id = self._to_val(row, 0)
            bean.name = self._to_val(row, 1)
            bean.remark = self._to_val(row, 2)
        return bean
