docker pull mysql:latest
docker run -d --rm -v "$PWD/data/mysql:/var/lib/mysql" -p 3306:3306  --name mysql_test_pypdm -e MYSQL_ROOT_PASSWORD=123456 mysql