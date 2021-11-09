# 单元测试说明

------

## sqlite 测试

- 数据库文件： [test.db](db/sqlite/test.db)
- 初始化脚本： [init_db.sql](db/sqlite/init_db.sql)、[rollback_db.sql](db/sqlite/rollback_db.sql)
- 单元测试脚本： `python ./test_pypdm_sqlite.py`


## mysql 测试

- docker 启动脚本： [run_docker_mysql.ps1](run_docker_mysql.ps1)、[run_docker_mysql.sh](run_docker_mysql.sh)
- 数据挂载目录： [data](db/mysql/data)、[conf](db/mysql/conf)
- 初始化脚本： [init_db.sql](db/mysql/init_db.sql)、[rollback_db.sql](db/mysql/rollback_db.sql)
- 单元测试脚本： `python ./test_pypdm_mysql.py`


## 关于临时数据

### PDM 临时数据

通过单元测试生成的 PDM 文件存储在 [tmp](tmp) 目录，该目录删除并不影响测试，保留纯粹方便核对生成的 PDM 内容。


### sqlite 临时数据

sqlite 使用的是 python3 自带的 sqlite3 数据库，测试库文件存储在 [test.db](db/sqlite/test.db)，删除该文件并不影响测试。


### mysql 容器数据

mysql 使用的是 mysql8 的官方镜像作为测试库，因为 mysql8 的加密规则不向前兼容、而且没有 test 数据库，直接使用该镜像对测试很不方便。故对数据库做了对应的调整，并挂载到 [data](db/mysql/data) 目录以便直接可以用于单元测试。

若不慎删了 [data](db/mysql/data) 目录，可以通过以下步骤重新调整 mysql8 数据库：

```
# 拉取并运行 mysql8 镜像
./run_docker_mysql.[sh|ps1]

# 登入镜像
docker exec -it -u mysql <容器ID> /bin/bash

# 登陆数据库
mysql -uroot -p
use mysql;

# 修改 root 用户加密规则 
ALTER USER 'root'@'%' IDENTIFIED BY '123456' PASSWORD EXPIRE NEVER;

# 更新 root 用户的密码
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';

# 刷新权限
FLUSH PRIVILEGES;

# 创建 test 数据库
CREATE DATABASE IF NOT EXISTS test DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```


## 赞助途径

| 支付宝 | 微信 |
|:---:|:---:|
| ![](docs/imgs/alipay.png) | ![](docs/imgs/wechat.png) |


## 版权声明

　[![Copyright (C) EXP,2016](https://img.shields.io/badge/Copyright%20(C)-EXP%202016-blue.svg)](http://exp-blog.com)　[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

- Site: [http://exp-blog.com](http://exp-blog.com) 
- Mail: <a href="mailto:289065406@qq.com?subject=[EXP's Github]%20Your%20Question%20（请写下您的疑问）&amp;body=What%20can%20I%20help%20you?%20（需要我提供什么帮助吗？）">289065406@qq.com</a>


------
