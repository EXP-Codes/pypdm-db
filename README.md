# pypdm

> mysql/sqlite 的 PDM 生成器

------

[Python Packaging User Guide](https://packaging.python.org/#python-packaging-user-guide)
[PyPA sample project](https://github.com/pypa/sampleproject)

## 程序打包

通过执行下列语句来进行打包：

```
python setup.py xxx
```

其中xxx可以是下列几种方式中其中一个：

- sdist             create a source distribution (tarball, zip file, etc.)
- bdist             create a built (binary) distribution
- bdist_dumb        create a "dumb" built distribution
- bdist_rpm         create an RPM distribution
- bdist_wininst     create an executable installer for MS Windows
- bdist_egg         create an "egg" distribution

举个例子：

```
python setup.py sdist　#生成的文件支持 pip
```

此时在根目录出现了dist文件夹，里面有name-version.tar.gz这个文件，这就是我们要发布到PyPI的压缩包了。


## 发布到PyPI

首先我们需要在PyPI上注册一个帐号，并在本地用户根目录下创建文件 `~/.pypirc`，这样以后就不需要输入帐号密码了。

```
[distutils]
index-servers=pypi

[pypi]
repository = https://pypi.python.org/pypi
username = <username>
password = <password>
```

接下来，需要在PyPI网站上注册一个项目，网站提供三种方式注册，选择一种即可，最简单的是通过上传打包时生成的PKG-INFO文件，生成项目信息。此步骤只需在第一次发布时操作。

接下来就是最后一步，上传打包好的库。我们这里是用twine，如果环境中没有安装，需要先采用 `pip install twine` 安装即可。

```
twine upload dist/*
```

此时在网页上就可以看到自己的源代码包啦，并且可以通过使用 `pip install <packagename>` ,就可以使用我们自己写的Python库了。

------

本地打包：
python setup.py sdist

安装
cd .\dist\
pip install .\pypdm-1.0.0.tar.gz


------

推荐使用 https://github.com/PyMySQL/PyMySQL


pip install pymysql

TODO: 通过启动参数决定是否 log.init() 使用内部日志


mysql 预编译语句的占位符是 %s
sqlite 预编译语句的占位符是 ?

mysql 没有默认主键列，因此生成的 dao 模板的 insert/update SQL 语句要去掉第一列
sqlite 默认主键是隐藏自增列 rowid，因此生成的 dao 模板的 insert/update SQL 语句要保留第一列
