---
layout: post
title: SQL Connection Strings
slug: sql-connection-strings
author: Martin Thoma
date: 2019-06-02 20:00
category: Code
tags: SQLAlchemy, Database, MySQL
featured_image: logos/python.png
---
When you want to connect to a database in SQLAlchemy, you need a connection
string. It usually has the form

```
dialect[+driver]://user:password@host/dbname[?key=value..]
```

Quite often, the `user` is `root` and the `host` is `localhost`.

Once you have the valid connection string, you can **test if it works** via this script:

```
import sqlalchemy
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
print(engine.table_names())
```


## SQLite


`requirements.txt`: None


Connection:

```
SQLALCHEMY_DATABASE_URI = 'sqlite:///absolute_filepath'

# Example:
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
```

The first two slashes come from the seperator of dialect and driver, the third
one from the separation between credentials+host and dbname, the fourth one is
the path which is kind of the name of the database.

If you want an in-memory SQLite DB, just specify an empty URL ([source](https://docs.sqlalchemy.org/en/13/core/engines.html#sqlite)):

```
SQLALCHEMY_DATABASE_URI = 'sqlite://'
```


## MySQL and MariaDB

`requirements.txt`:

```
PyMySQL
```

Connection:

```
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@host/dbname'
```

There are a lot of [other MySQL drivers](https://docs.sqlalchemy.org/en/13/dialects/mysql.html):

* [`mysqldb`](https://pypi.org/project/MySQL-python/): C extension; does not work with Python 3 ([reasons for pymysql](https://stackoverflow.com/a/14076841/562769))
* [`mysqlconnector`](https://dev.mysql.com/doc/connector-python/en/): Officially provided by MySQL; worst performance and not downloadable via PyPI ([source](https://stackoverflow.com/a/46396881/562769))

## Others

I haven't tried it, but [sqlalchemy lists more](https://docs.sqlalchemy.org/en/13/dialects/index.html) like Oracle, Microsoft SQL Server and Sybase.
