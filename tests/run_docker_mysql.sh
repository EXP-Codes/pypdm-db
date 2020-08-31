docker pull mysql:latest
docker run -d --rm -v "$PWD/db/mysql/conf/:/etc/mysql/conf.d/" -v "$PWD/db/mysql/data/:/var/lib/mysql/" -p 3306:3306 --name mysql8 -e MYSQL_ROOT_PASSWORD=123456 mysql