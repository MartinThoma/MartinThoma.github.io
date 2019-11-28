---
layout: post
title: Key-Value Stores
slug: key-value-stores
author: Martin Thoma
date: 2019-09-29 20:00
category: Code
tags: Database, Redis, MySQL, MariaDB, Postgres, pickledb, Python, NoSQL, sysbench, DBaaS
featured_image: logos/db.png
---
[Key-value stores](https://en.wikipedia.org/wiki/Key-value_database) are
specialized NoSQL databases. Essentially, they are dictionaries[^1].


## Database Properties

[ACID](https://en.wikipedia.org/wiki/ACID) is a set of properties of database
transactions intended to guarantee validity even in the event of errors, power
failures, etc:

* **A**tomicity: Either all statements are applied or none. This is important for SELECTs.
* **C**onsistency: A transaction brings the DB from one valid state to another; see also [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)
* **I**solation: concurrent execution of transactions leaves the database in
  the same state that would have been obtained if the transactions were
  executed sequentially
* **D**urability: once a transaction has been committed, it will remain
  committed even in the case of a system failure

Please notice that Atomicity, Consistency and Isolation are not relevant in
many cases where you use a key-value store as you only have GET / SET for one
key.


## Database Features

* **Embedded or client/server**: An [embedded database](https://en.wikipedia.org/wiki/Embedded_database)
  is not visible to remote servers. It is embedded in the current process
  (which can, of course, make it visible).
* **Type System**: Enforcing types takes time and gives guarantees. Some
  databases have very simple type systems (e.g. SQLite) and some offer more
  (e.g. MySQL)
* **Availability / Failover**: Systems fail. The machine which contains your database could
  simply be plugged out. How do you deal with that?
    * **Backup options**: If this is relevant at all depends very much what you
      use it for. If the key-value store is used as a cache, then backup
      options are probably not necessary. If it is used to store configuration,
      then it likely is.
    * **Replication**: Having another machine which replicates the data is the
      only way to make sure that the system is available, even if the main
      machine breaks. See [Redis Replication](https://redis.io/topics/replication).
* **Scalability**: Suppose you want to store more than you can do on the hardware
  of a single machine. Do you have to buy a better machine (scale vertically)
  or is it possible to have another (cheap) machine and run the datase on two
  machines in a distributed way (scale horizontally)? This is done via [sharding](https://www.digitalocean.com/community/tutorials/understanding-database-sharding).
* **Users**: Having a user system and different databases in the same database
  management system is nice, because it allows centralisation of the service
  for different teams at the same company. Then somebody takes care of the
  database being up / being backed up and others just get a user.


## Use Cases

*Configuration*: Suppose you have a product which makes use of micro services.
In some cases, those micro services need some alignment in form of
configuration.

*Caches*: Web services can contain all sorts of computations which might need
longer than acceptable. Caching / pre-calculating those are a common approach
for this problem.

## Other Benchmarks

[MySQL Performance on Amazon EC2](https://www.flexera.com/blog/cloud/2007/11/mysql-performance-on-amazon-ec2/), 2007:

* EC2 small: 227 reads/s; 116 read+writes / s
* EC2 large: 430 reads/s; 310 read+writes / s
* EC2 xlarge: 630 reads/s; 483 read+writes / s

sysbench:

```
$ mysql
> create database sbtest;
$ sysbench oltp_read_write --db-driver=mysql --mysql-db=dbtest --mysql-user=root --mysql-password=YOUR_PASSWORD prepare
$ sysbench oltp_read_write --db-driver=mysql --mysql-db=dbtest --threads=16 --events=100000 --mysql-user=root --mysql-password=YOUR_PASSWORD run

$ sudo -u postgres psql
postgres=# CREATE DATABASE sbtest;
postgres=# grant all privileges on database sbtest to example_user;
$ sysbench oltp_read_write --db-driver=pgsql --pgsql-db=sbtest --pgsql-user=example_user --pgsql-password=example_password prepare
$ sysbench oltp_read_write --db-driver=pgsql --pgsql-db=sbtest --threads=16 --events=100000 --pgsql-user=example_user --pgsql-password=example_password run
```

On my Thinkpad T460p I get the following numbers. However, I'm not certain how
valuable they are as they fluctuate quite a bit between consecutive runs.

<table class="table">
    <tr>
        <th rowspan="2">Database</th>
        <th rowspan="2">Transactions</th>
        <th rowspan="2">Queries</th>
        <th colspan="4">Latency</th>
    </tr>
    <tr>
        <th>Min</th>
        <th>AVG</th>
        <th>Max</th>
        <th>95th percentile</th>
    </tr>
    <tr>
        <td>MariaDB 15.1</td>
        <td>484.81&nbsp;/&nbsp;s</td>
        <td>9701.13&nbsp;/&nbsp;s</td>
        <td>14.25ms</td>
        <td>32.61ms</td>
        <td>137.37ms</td>
        <td>53.85ms</td>
    </tr>
    <tr>
        <td>Postgres 10.10</td>
        <td>457.44&nbsp;/&nbsp;s</td>
        <td>9644.38&nbsp;/&nbsp;s</td>
        <td>5.44ms</td>
        <td>34.90ms</td>
        <td>2052.58ms</td>
        <td>32.53ms</td>
    </tr>
</table>


## Features

<table class="table">
    <thead>
        <tr>
            <th></th>
            <th>SQLite</th>
            <th>MariaDB</th>
            <th>Postgresql</th>
            <th>Redis</th>
            <th>Memcached</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>Server</th>
            <td><span style="color:red;" title="No">✗</span></td>
            <td><span style="color:green;" title="Yes">✔</span></td>
            <td><span style="color:green;" title="Yes">✔</span></td>
            <td><span style="color:green;" title="Yes">✔</span></td>
            <td><span style="color:green;" title="Yes">✔</span></td>
        </tr>
        <tr>
            <th>Users</th>
            <td><span style="color:red;" title="No">✗</span></td>
            <td><a href="https://mariadb.com/kb/en/library/create-user/"><span style="color:green;" title="Yes">✔</span></a></td>
            <td><a href="https://www.postgresql.org/docs/9.1/sql-createuser.html"><span style="color:green;" title="Yes">✔</span></a></td>
            <td><span style="color:red;" title="No">✗</span></td>
            <td><span style="color:red;" title="No">✗</span></td>
        </tr>
    </tbody>
</table>

### Serverless Databases

Serverless Database is a fancy name for a hosted database. It is also called
DBaaS - database as a service. You don't have to worry about the underlying
machine; you pay for the usage. This usually means:

* GET
* PUT
* Total storage in the database

You should not have to worry about:

* Backups
* Scaling it up

Databases which offer this:

* <a href="https://en.wikipedia.org/wiki/Amazon_DynamoDB">Amazon DynamoDB</a>
* <a href="https://en.wikipedia.org/wiki/Amazon_Aurora">Amazon Aurora Serverless</a>


## Benchmark

This is not finished. You can find the [code on Github](https://github.com/MartinThoma/algorithms/tree/master/Python/databases/benchmark).

If you don't make the <code>key</code> column a primary key, MariaDB is quite a
bit faster.

<table class="table">
    <thead>
        <tr>
            <th rowspan="2">Database</th>
            <th rowspan="2">Bulk Write</th>
            <th rowspan="2">Batched Write</th>
            <th rowspan="2">Bulk Read</th>
            <th colspan="4">Read Latency - Percentile</th>
        </tr>
        <tr>
            <th>25%</th>
            <th>50%</th>
            <th>95%</th>
            <th>99%</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 2px solid black">
            <td><a href="https://docs.python.org/3/tutorial/datastructures.html#dictionaries">dict</a></td>
            <td style="background-color: #baf6ba;" class="text-right">2&#8239;639&#8239;859.62&nbsp;inserts/s</td>
            <td class="text-right">-</td>
            <td class="text-right">-</td>
            <td style="background-color: #baf6ba;">0μs</td>
            <td style="background-color: #baf6ba;">0μs</td>
            <td style="background-color: #baf6ba;">1μs</td>
            <td style="background-color: #baf6ba;">2μs</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/SQLite">SQLite</a> (in-memory)</td>
            <td style="background-color: #baf6ba;" class="text-right">259&#8239;834.14&nbsp;inserts/s</td>
            <td class="text-right">27&#8239;151.94&nbsp;inserts/s</td>
            <td style="background-color: #baf6ba;" class="text-right">69&#8239;163.37&nbsp;selects/s</td>
            <td style="background-color: #baf6ba;">32μs</td>
            <td style="background-color: #baf6ba;">32μs</td>
            <td style="background-color: #baf6ba;">36μs</td>
            <td style="background-color: #baf6ba;">60μs</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/SQLite">SQLite</a></td>
            <td style="background-color: #baf6ba;" class="text-right">193&#8239;930.10&nbsp;inserts/s</td>
            <td class="text-right">6181.23&nbsp;inserts/s</td>
            <td style="background-color: #baf6ba;" class="text-right">61&#8239;012.26&nbsp;selects/s</td>
            <td style="background-color: #baf6ba;">34μs</td>
            <td style="background-color: #baf6ba;">34μs</td>
            <td style="background-color: #baf6ba;">38μs</td>
            <td>62μs</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Memcached">Memcached</a></td>
            <td style="background-color: #baf6ba;" class="text-right">131&#8239;635.98&nbsp;inserts/s</td>
            <td style="background-color: #baf6ba;" class="text-right">123&#8239;937.91&nbsp;inserts/s</td>
            <td style="background-color: #baf6ba;" class="text-right">57&#8239;191.03&nbsp;selects/s</td>
            <td style="background-color: #baf6ba;">25μs</td>
            <td style="background-color: #baf6ba;">26μs</td>
            <td style="background-color: #baf6ba;">38μs</td>
            <td style="background-color: #baf6ba;">51μs</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Redis">Redis</a></td>
            <td class="text-right">5103.39&nbsp;inserts/s</td>
            <td class="text-right">40&#8239;494.49&nbsp;inserts/s</td>
            <td class="text-right">TODO&nbsp;selects/s</td>
            <td style="background-color: #ffbebe;">52μs</td>
            <td style="background-color: #ffbebe;">54μs</td>
            <td style="background-color: #ffbebe;">80μs</td>
            <td style="background-color: #ffbebe;">97μs</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/MariaDB">MariaDB</a> (<a href="https://en.wikipedia.org/wiki/MyISAM">MyISAM</a>)</td>
            <td class="text-right">3412.18&nbsp;inserts/s,<br/>
                                  30&#8239;266.34<sup title="LOAD DATA LOCAL INFILE 'data.csv' INTO TABLE KeyValue FIELDS TERMINATED BY ',' ENCLOSED BY '"' IGNORE 1 LINES;">🌞</sup></td>
            <td class="text-right">4&#8239;885.09&nbsp;inserts/s</td>
            <td class="text-right">41&#8239;432.73&nbsp;selects/s</td>
            <td style="background-color: #baf6ba;">32μs</td>
            <td style="background-color: #baf6ba;">33μs</td>
            <td style="background-color: #baf6ba;">36μs</td>
            <td style="background-color: #baf6ba;">60μs</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/MariaDB">MariaDB</a> (<a href="https://en.wikipedia.org/wiki/Aria_(storage_engine)">Aria</a>)</td>
            <td class="text-right">2546.49&nbsp;inserts/s,<br/>
                                   19&#8239;708.31<sup title="LOAD DATA LOCAL INFILE 'data.csv' INTO TABLE KeyValue FIELDS TERMINATED BY ',' ENCLOSED BY '"' IGNORE 1 LINES;">🌞</sup></td>
            <td class="text-right">4309.30 inserts/s</td>
            <td class="text-right">41&#8239;305.08&nbsp;selects/s</td>
            <td style="background-color: #baf6ba;">33μs</td>
            <td style="background-color: #baf6ba;">33μs</td>
            <td style="background-color: #baf6ba;">36μs</td>
            <td style="background-color: #baf6ba;">57μs</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/PostgreSQL">PostgreSQL</a></td>
            <td class="text-right" style="background-color: #ffbebe;">1767.12&nbsp;inserts/s</td>
            <td class="text-right">3529.08&nbsp;inserts/s</td>
            <td class="text-right">37&#8239;732.27&nbsp;selects/s</td>
            <td style="background-color: #baf6ba;">32μs</td>
            <td style="background-color: #baf6ba;">33μs</td>
            <td style="background-color: #baf6ba;">36μs</td>
            <td style="background-color: #baf6ba;">59μs</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/MariaDB">MariaDB</a> (<a href="https://en.wikipedia.org/wiki/InnoDB">InnoDB</a>)</td>
            <td class="text-right">1152.20&nbsp;inserts/s <sup title="Tested only with 100k inserts">*</sup>,<br/>
                                   14&#8239;679.97<sup title="LOAD DATA LOCAL INFILE 'data.csv' INTO TABLE KeyValue FIELDS TERMINATED BY ',' ENCLOSED BY '"' IGNORE 1 LINES;">🌞</sup></td>
            <td class="text-right" style="background-color: #ffbebe;">643.56&nbsp;inserts/s</td>
            <td class="text-right">29&#8239;405.90&nbsp;selects/s</td>
            <td style="background-color: #baf6ba;">33μs</td>
            <td style="background-color: #baf6ba;">33μs</td>
            <td style="background-color: #baf6ba;">36μs</td>
            <td style="background-color: #baf6ba;">53μs</td>
        </tr>
    </tbody>
</table>

For some DBs, batching improved the bulk insert quite a bit. I guess this is
because this way I can avoid swapping. Maybe changing the batch-size from 1000
to higher numbers additionally increases the throughput.


## See also

* [How many keys are too many in memcached?](https://stackoverflow.com/q/2474746/562769)
* [LevelDB](https://en.wikipedia.org/wiki/LevelDB)
* [NoSQL Database Types](https://studio3t.com/knowledge-base/articles/nosql-database-types/)
* Redis Use Cases:
    * Todd Hoff: [How Twitter Uses Redis To Scale - 105TB RAM, 39MM QPS, 10,000+ Instances](http://highscalability.com/blog/2014/9/8/how-twitter-uses-redis-to-scale-105tb-ram-39mm-qps-10000-ins.html), 2014.
    * Adam Bloom: [Using Redis at Pinterest for Billions of Relationships](https://content.pivotal.io/blog/using-redis-at-pinterest-for-billions-of-relationships), 2013.
* Siyuan Fu: [Optimizing Memcached Efficiency](https://www.quora.com/q/quoraengineering/Optimizing-Memcached-Efficiency), 2017
* Andreas Wittig: [EC2 Network Performance Cheat Sheet](https://cloudonaut.io/ec2-network-performance-cheat-sheet/), 2018.
* [keyv](https://github.com/lukechilds/keyv): An interesting JavaScript project which abstracts the implementation of key-value stores away.
* MariaDB: [Choosing the Right Storage Engine](https://mariadb.com/kb/en/library/choosing-the-right-storage-engine/)
* Jan Bodnar: [MySQL storage engines](http://zetcode.com/databases/mysqltutorial/storageengines/), 2017.
* [When to use MyISAM and InnoDB?](https://stackoverflow.com/q/15678406/562769)
* [How can I speed up bulk inserts into MySQL with SQLAlchemy?](https://stackoverflow.com/q/58153472/562769)

## Footnotes

[^1]: Dictionaries are a fundamental data structure in Python. They are called
      *associative arrays* in PHP and *hashtable* in Java.
