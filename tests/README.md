# 单元测试说明

------

## sqlite 测试

- 数据库文件： [test.db](db/sqlite/test.db)
- 初始化脚本： [init_db.sql](db/sqlite/init_db.sql)、[rollback_db.sql](db/sqlite/rollback_db.sql)
- 单元测试脚本： `python ./test_pypdm_sqlite.py`


## mysql 测试

- docker 启动脚本： [docker-compose up -d](docker-compose.yml)
- 数据挂载目录： [data](db/mysql/data)
- 初始化脚本： [init_db.sql](db/mysql/init_db.sql)、[rollback_db.sql](db/mysql/rollback_db.sql)
- 单元测试脚本： `python ./test_pypdm_mysql.py`


## 关于临时数据

### PDM 临时数据

通过单元测试生成的 PDM 文件存储在 [tmp](tmp) 目录，该目录删除并不影响测试，保留纯粹方便核对生成的 PDM 内容。


### sqlite 临时数据

sqlite 使用的是 python3 自带的 sqlite3 数据库，测试库文件存储在 [test.db](db/sqlite/data/test.db)，删除该文件并不影响测试。


### mysql 容器数据

mysql 使用的是 docker 的 mariadb 数据库，测试库文件存储在 [data](db/mysql/data) 目录。

若不慎删了 [data](db/mysql/data) 目录，需要执行 `docker-compose up -d` 重新拉取并运行测试库。


