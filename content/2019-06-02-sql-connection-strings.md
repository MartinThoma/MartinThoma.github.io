---
layout: post
title: SQL Connection Strings
slug: sql-connection-strings
lang: en
author: Martin Thoma
date: 2019-06-02 20:00
category: Code
tags: SQLAlchemy, Database, MySQL
featured_image: logos/python.png
---
When you want to connect to a database in SQLAlchemy, you need a connection
string. It usually has the form

```text
dialect[+driver]://user:password@host/dbname[?key=value..]
```

Quite often, the `user` is `root` and the `host` is `localhost`.

Once you have the valid connection string, you can **test if it works** via this script:

```python
import sqlalchemy

engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
print(engine.table_names())
```


## SQLite


`requirements.txt`: None


Connection:

```python
SQLALCHEMY_DATABASE_URI = "sqlite:///absolute_filepath"

# Example:
SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
```

The first two slashes come from the separator after the dialect (`://`), the third
one separates the (empty) host from the database name, and the fourth one is
the beginning of the absolute path to the database file.

If you want an in-memory SQLite DB, just specify an empty URL ([source](https://docs.sqlalchemy.org/en/13/core/engines.html#sqlite)):

```python
SQLALCHEMY_DATABASE_URI = "sqlite://"
```


## MySQL and MariaDB

`requirements.txt`:

```text
PyMySQL
```

Connection:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@host/dbname"
```

There are a lot of [other MySQL drivers](https://docs.sqlalchemy.org/en/13/dialects/mysql.html):

* [`mysqldb`](https://pypi.org/project/MySQL-python/): C extension; does not work with Python 3 ([reasons for pymysql](https://stackoverflow.com/a/14076841/562769))
* [`mysqlconnector`](https://dev.mysql.com/doc/connector-python/en/): Officially provided by MySQL; worst performance and not downloadable via PyPI ([source](https://stackoverflow.com/a/46396881/562769))

## Others

I haven't tried them, but [SQLAlchemy lists more](https://docs.sqlalchemy.org/en/13/dialects/index.html) like Oracle, Microsoft SQL Server and Sybase.
