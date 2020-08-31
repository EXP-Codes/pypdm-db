#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/8/30 15:13
# @File   : pypdm.py
# -----------------------------------------------


from .dbc._mysql import MysqlDBC
from .dbc._sqlite import SqliteDBC
from ._pdm import *


def build(
        dbtype = 'sqlite',
        host = '127.0.0.1',
        port = 3306,
        username = 'root',
        password = '123456',
        dbname = 'test',
        charset = CHARSET,
        pdm_pkg = 'src.pdm',
        table_whitelist = [],
        table_blacklist = [],
        to_log = False
    ) :
    '''
    构造指定数据库的 PDM 对象文件
    :param dbtype: 数据库类型，只支持 sqlite 或 mysql
    :param host: 数据库 IP
    :param port: 数据库端口
    :param username: 登陆账号
    :param password: 登陆密码
    :param dbname: 数据库名称
    :param charset: 数据库编码
    :param pdm_pkg: 期望生成 PDM 文件的包路径
    :param table_whitelist: 要生成哪些表的 PDM 文件（默认所有表）
    :param table_blacklist: 不生成哪些表的 PDM 文件
    :param to_log: 是否启用内部日志
    :return:
    '''
    if to_log :
        log.init()

    dbc = _connect_to_db(host, port, username, password, dbtype, dbname, charset)
    if dbc :
        pdm = PDM(dbc, pdm_pkg)
        pdm.to_pdm(table_whitelist, table_blacklist)



def _connect_to_db(dbtype, host, port, username, password, dbname, charset) :
    '''
    根据数据库类型获取数据库连接对象
    :param dbtype: 数据库类型，只支持 sqlite 或 mysql
    :param host: 数据库 IP
    :param port: 数据库端口
    :param username: 登陆账号
    :param password: 登陆密码
    :param dbname: 数据库名称
    :param charset: 数据库编码
    :return: 数据库连接对象
    '''
    if  dbtype.lower() == 'sqlite' :
        dbc = SqliteDBC(dbname)

    elif dbtype.lower() == 'mysql' :
        dbc = MysqlDBC(host, port, username, password, dbname, charset)

    return dbc





