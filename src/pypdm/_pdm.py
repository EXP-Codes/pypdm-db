#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/8/31 10:10
# @File   : _pdm.py
# -----------------------------------------------

import re
import string
from .assist.cfg import *
from .assist import log


class PDM :

    def __init__(self, dbc, pdm_pkg) :
        self.dbc = dbc
        self.pdm_pkg = pdm_pkg
        pdm_path = pdm_pkg.replace('.', '/')
        self.bean_pkg_path = '%s/bean/' % pdm_path
        self.dao_pkg_path = '%s/dao/' % pdm_path


    def to_pdm(self, whitelist = [], blacklist = []) :
        conn = self.dbc.conn()
        if not whitelist :
            whitelist = self.get_all_tables(conn)

        for table_name in whitelist :
            if table_name in blacklist :
                continue

            columns = self.get_columns(conn, table_name)
            bean_file_content = self._to_beans(table_name, columns)
            self.save(bean_file_content, self.bean_pkg_path, table_name, '.py')

            dao_file_content = self._to_daos(table_name, columns)
            self.save(dao_file_content, self.dao_pkg_path, table_name, '.py')

        self.dbc.close()


    def get_all_tables(self, conn) :
        tables = []
        try:
            cursor = conn.cursor()
            cursor.execute('show tables')
            rows = cursor.fetchall()
            for row in rows:
                tables.append(row[0].encode(CHARSET))
            cursor.close()
        except:
            log.error("查询 table 列表失败")
        return tables


    def get_columns(self, conn, table_name) :
        cursor = conn.cursor()
        cursor.execute('select * from %s limit 0' % table_name)
        columns = [tuple[0] for tuple in cursor.description]
        cursor.close()
        return columns


    def _to_beans(self, table_name, columns) :
        tpl = DBTemplate(BEAN_TPL)
        variables = list(map(self.to_var, columns))
        placeholders = {
            '{table_name}': table_name,
            '{TableName}': self.to_camel(table_name),
            '{columns}': '\n'.join(list(map((lambda col: '\t%s = "%s"' % (col, col)), columns))),
            '{variables}': '\n'.join(list(map((lambda col: '\t\tself.%s = None' % col), variables))),
            '{params}': '\n'.join(list(('\t\t\tself.%s,' % col) for col in variables[1:])),
            '{kvs}': '\n'.join(list(map(self.to_kv, columns)))
        }
        return tpl.safe_substitute(placeholders).replace('\t', '    ')


    def to_camel(self, underline) :
        camel = ''
        if isinstance(underline, str) :
            for word in underline.split('_') :
                camel += word.capitalize()
        return camel


    def to_var(self, col) :
        return re.sub(r'^[a-zA-Z]_', '', col)


    def to_kv(self, col) :
        return '\t\t\t\t"\t%s = %s" % (self.' + col + ', self.' + self.to_var(col) + '),'


    def _to_daos(self, table_name, columns) :
        tpl = DBTemplate(DAO_TPL)
        placeholders = {
            '{pkg_path}': self.pdm_pkg,
            '{table_name}': table_name,
            '{TableName}': self.to_camel(table_name),
            '{insert}': self.to_insert(table_name, columns),
            '{update}': self.to_update(table_name, columns),
            '{select}': self.to_select(table_name, columns),
            '{set_values}': '\n'.join(('\t\t\tbean.%s = self._to_val(row, %i)' % (self.to_var(col), idx)) for idx, col in enumerate(columns))
        }
        return tpl.safe_substitute(placeholders).replace('\t', '    ')


    def to_insert(self, table_name, columns) :
        cols = ', '.join(columns[1:])
        vars = 's, %' * (len(columns) - 2)
        return 'insert into ' + table_name + '(' + cols + ') values(%' + vars + 's)'


    def to_update(self, table_name, columns) :
        cols = ', '.join(list(map((lambda col: col + ' = %s'), columns[1:])))
        return 'update ' + table_name + ' set ' + cols + ' where 1 = 1 '


    def to_select(self, table_name, columns) :
        sql = 'select %s from ' + table_name + ' where 1 = 1 '
        return sql % (', '.join(columns))


    def save(self, content, filedir, filename, suffix) :
        '''
        写入 PDM 文件
        :param content: 文件内容
        :param filedir: 存储目录
        :param filename: 文件名
        :param suffix: 文件后缀
        :return: PDM 文件路径
        '''
        if not os.path.exists(filedir) :
            os.makedirs(filedir)
        path = '%s%s%s' % (filedir, filename, suffix)
        with open(path, 'w+') as file :
            file.write(content)
        return path




class DBTemplate(string.Template) :
    delimiter = '@'
    idpattern = r'\{\w+\}'
