#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# DAO: t_teachers
# -------------------------------

from ..bean.t_teachers import TTeachers
from pypdm.dao._base import BaseDao


class TTeachersDao(BaseDao) :
    TABLE_NAME = 't_teachers'
    SQL_COUNT = 'select count(1) from t_teachers'
    SQL_TRUNCATE = 'truncate table t_teachers'
    SQL_INSERT = 'insert into t_teachers(s_name, s_remark) values(%s, %s)'
    SQL_DELETE = 'delete from t_teachers where 1 = 1 '
    SQL_UPDATE = 'update t_teachers set s_name = %s, s_remark = %s where 1 = 1 '
    SQL_SELECT = 'select i_id, s_name, s_remark from t_teachers where 1 = 1 '

    def __init__(self) :
        BaseDao.__init__(self)

    def _to_bean(self, row) :
        bean = None
        if row:
            bean = TTeachers()
            bean.id = self._to_val(row, 0)
            bean.name = self._to_val(row, 1)
            bean.remark = self._to_val(row, 2)
        return bean
