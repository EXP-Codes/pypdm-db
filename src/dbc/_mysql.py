#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# Mysql 数据库接口
# -------------------------------

import pymysql as pdbc

from src.assist import log


class MysqlDBC:
    """
    Mysql 数据库封装类
    """

    def __init__(self, host='127.0.0.1', port=3306, username='root', password='123456', dbname='test', charset='utf8'):
        """
        构造函数
        :param host: 数据库地址
        :param port: 数据库端口
        :param username: 数据库账号
        :param password: 数据库密码
        :param dbname: 数据库名称
        :param charset: 数据库编码
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.dbname = dbname
        self.charset = charset
        self._conn = None


    def conn(self):
        """
        连接到数据库
        :return: 数据库连接（失败返回 None）
        """
        if not self._conn:
            try:
                self._conn = pdbc.connect(
                    host = self.host,
                    port = self.port,
                    user = self.username,
                    password = self.password,
                    db = self.dbname,
                    charset = self.charset
                )
            except:
                log.error("连接数据库 [%s] 失败" % self.dbname)
        return self._conn


    def close(self):
        """
        断开数据库连接
        :return: 是否断开成功
        """
        is_ok = False
        if self._conn:
            try:
                self._conn.close()
                self._conn = None
                is_ok = True
            except:
                log.error("断开数据库 [%s] 失败" % self.dbname)
        return is_ok


    def reconn(self):
        """
        重连数据库
        :return: 数据库连接（失败返回 None）
        """
        self.close()
        return self.conn()


    def commit(self):
        """
        提交事务
        :return: 是否提交成功
        """
        is_ok = False
        if self._conn:
            try:
                self._conn.commit()
                is_ok = True
            except:
                log.error("提交事务到数据库 [%s] 失败" % self.dbname)
        return is_ok


    def init(self, sql_script):
        """
        初始化数据库
        :param sql_script: 建库脚本（注意控制好数据表是否存在）
        :return: 是否初始化成功
        """
        if self.conn():
            try:
                data = ""
                with open(sql_script, "r") as file:
                    data = file.read()

                if data:
                    cursor = self._conn.cursor()
                    sqls = data.split(";")
                    for sql in sqls:
                        sql = sql.strip()
                        if sql:
                            cursor.execute(sql)
                    cursor.close()
            except:
                log.error("初始化数据库 [%s] 失败" % self.dbname)
            self.close()
