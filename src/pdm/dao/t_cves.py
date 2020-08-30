#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# DAO: t_cves
# -------------------------------

from src.pdm.t_cves import TCves
from pypdm.bean._base import BaseDao


class TCvesDao(BaseDao):
    TABLE_NAME = "t_cves"
    SQL_COUNT = "select count(1) from t_cves"
    SQL_TRUNCATE = "truncate table t_cves"
    SQL_INSERT = "insert into t_cves(s_src, s_cves, s_title, s_time, s_info, s_url) values(%s, %s, %s, %s, %s, %s)"
    SQL_DELETE = "delete from t_cves where 1 = 1 "
    SQL_UPDATE = "update t_cves set s_src = %s, s_cves = %s, s_title = %s, s_time = %s, s_info = %s, s_url = %s where 1 = 1 "
    SQL_SELECT = "select s_md5, s_src, s_cves, s_title, s_time, s_info, s_url from t_cves where 1 = 1 "

    def __init__(self):
        BaseDao.__init__(self)

    def _to_bean(self, row):
        bean = None
        if row:
            bean = TCves()
            bean.md5 = self._to_val(row, 0)
            bean.src = self._to_val(row, 1)
            bean.cves = self._to_val(row, 2)
            bean.title = self._to_val(row, 3)
            bean.time = self._to_val(row, 4)
            bean.info = self._to_val(row, 5)
            bean.url = self._to_val(row, 6)
        return bean
