#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# DAO: @{table_name}
# -------------------------------

from src.bean.@{table_name} import @{TableName}
from src.dao._base import BaseDao


class @{TableName}Dao(BaseDao):
    TABLE_NAME = "@{table_name}"
    SQL_COUNT = "select count(1) from @{table_name}"
    SQL_TRUNCATE = "truncate table @{table_name}"
    SQL_INSERT = "@{insert}"
    SQL_DELETE = "delete from @{table_name} where 1 = 1 "
    SQL_UPDATE = "@{update}"
    SQL_SELECT = "@{select}"

    def __init__(self):
        BaseDao.__init__(self)

    def _to_bean(self, row):
        bean = None
        if row:
            bean = @{TableName}()
@{set_values}
        return bean
