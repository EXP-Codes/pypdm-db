# 单元测试说明

------

```
docker exec -it -u mysql 27492a40a39e /bin/bash
mysql -uroot -p
use mysql;
select host, user from user;


 #修改加密规则 （这行我没有写，不过貌似也可以）
ALTER USER 'root'@'%' IDENTIFIED BY '123456' PASSWORD EXPIRE NEVER;
#更新一下用户的密码
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
#刷新权限
FLUSH PRIVILEGES;
```