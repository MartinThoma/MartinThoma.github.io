---
layout: post
title: SQL Injections 😈
slug: sql-injections
lang: en
author: Martin Thoma
date: 2020-10-12 20:00
category: Security
tags: Security, AppSec
featured_image: logos/cybersecurity.png
medium_url: https://medium.com/faun/sql-injections-e8bc9a14c95
---
An SQL injection is an attack on a web system with a database. The attack is done by injecting unexpected commands into parameters. Don’t worry, I’ll explain that later in detail.

After reading this article, you will understand what the effect of being vulnerable to SQL injections can be, how to execute SQL injections yourself, and how to prevent them. Let’s get started!

## Why it Matters

SQL Injection attacks are so common nowadays that I’ll just give you this list with some of the biggest known attacks. Please note that SQL injections don’t necessarily break anything and thus they might not always be noticed. Most of the time, the attacker steals data.

* Injection flaws are part of the [OWASP Top-10](https://owasp.org/www-project-top-ten/), meaning they're recognized as a common vulnerability
* **1998**: Jeff Forristal explains the issue ([source](https://www.esecurityplanet.com/network-security/how-was-sql-injection-discovered.html), [original](http://phrack.org/issues/54/8.html#article)).
* **2009**: 130 million credit card numbers were stolen from Heartland Payment Systems, 7-Eleven, and others ([source](http://news.bbc.co.uk/2/hi/americas/8206305.stm)). They claimed **\$130 million** in losses ([source](https://www.wired.com/2010/03/heartland-sentencing/)).
* **2010**: 110,000 credit card numbers were stolen from Twin America LLC ([source](https://www.bankinfosecurity.co.uk/sql-injection-blamed-for-new-breach-a-3195)).
* **2011**: 50,000 emails and passwords were stolen from Sony ([source](https://www.wired.com/2011/06/lulzsec-sony-again/)). Sony claims that this created costs of \$605,000 USD ([source](https://www.bbc.com/news/technology-19949624)).
* **2015**: The personal data of 157,000 people was stolen from TalkTalk ([source](https://www.theregister.com/2015/11/06/talktalk_claims_157000_customers_data_stolen/)).
* **2016**: The data of 200,000 voters in Illinois was stolen ([source](https://www.theregister.com/2016/08/29/fbi_warns_attacks_on_election_systems/)).
* **2020**: 8.3 million user names and password hashes were stolen from Freepik ([source](https://www.zdnet.com/article/free-photos-graphics-site-freepik-discloses-data-breach-impacting-8-3m-users/))

In the worst case, the attacker steals the data and sells it. After that, they corrupt your data in a way you don’t notice, so you don’t restore your backups.

## How are SQL injection attacks executed?

Imagine you have a website with a login form. Leaving out some important bells and whistles, something like this happens:

```sql
SELECT *
FROM   users
WHERE  USER = '[username]'
       AND password = '[password]'
```

The attacker can change the username to `admin' OR '1'='1`, which then gives the query:

```sql
SELECT *
FROM   users
WHERE  USER = 'admin' OR '1'='1'
       AND password = 'secret'
```

This means the query will look for two conditions:

* The username is equal to admin
* OR the password is equal to secret

Instead, it should have been looking for the combination (username is admin AND the password is equal to secret).

What happened here is that the attacker injected SQL into the query. This changed the logic of access control and thus let the attacker log in as admin.

## How can I prevent SQL injections?

Input validation and proper escaping are the keys to preventing SQL injections. Preventing SQL injections in this case also helps the poor users who actually wanted to have a ' within their username/password. Never blindly trust user input. Don’t use simple string concatenation to build SQL queries with parameters supplied by the user.

You might be tempted to think that removing the quotes is enough. This, however, might cause problems within your application. Then you could escape the quotes. This is certainly a good step, but you have to watch out that the escaping isn’t broken and that you don’t forget anything.

Instead of doing this manually, you should use [parameter binding](https://docs.sqlalchemy.org/en/13/core/tutorial.html#bind-parameter-objects). In Python, it looks like this:

```python
from sqlalchemy.sql import text

# Create a connection conn
stmt = text(
    """SELECT * FROM users
               WHERE user = :username AND password = :password"""
)
conn.execute(stmt, {"username": "foo", "password": "bar"})
```

Another way to prevent SQL injections is to use an ORM which does the input sanitization for you:

```python
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    name = Column(String, primary_key=True)
    password = Column(String)


engine = create_engine("sqlite://")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = session.query(User).filter_by(name="foo").filter_by(password="bar").first()
```

Here we pass the name and password parameters to the ORM (SQLAlchemy). It takes care of sanitizing the name and the password.

The third option is to create a [prepared statement](https://en.wikipedia.org/wiki/Prepared_statement). This is also using parameter binding but on the side of the SQL server. I think those are typically harder to use from a developer's perspective.

Doing any of those three options is nice, but it is not enough. You want to be sure that you or anybody else doesn’t accidentally add code that is vulnerable to SQL injections. For this reason, static application security testing tools (SAST) like [bandit](https://pypi.org/project/bandit/) check for potential SQL injection vulnerabilities ([source](https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html)). Add that to your CI pipeline and stay safe!

The principles are the same for any programming language, but you might be interested in seeing more concrete advice in the language that is relevant to you. Have a look at [bobby-tables.com](https://bobby-tables.com/).

## Creative SQL Injections

There are some SQL injections that are less trivial than the examples mentioned before.

### Simplifying Queries

An attacker might not know exactly how a query continues. So the attacker
inserts `--` at the end to make the rest of the query a comment.

### Information Gathering

An attacker might not know the structure of the database. However, many
databases have a special schema that contains the information. For MySQL,
MariaDB, and Postgres, it is called `information_schema` and consists of views
like `information_schema.tables` and `information_schema.columns`.

It’s possible to restrict access to that table
([example](https://dba.stackexchange.com/a/25668/25983)). You should do it from
a defense-in-depth perspective.

### Order By

You might be tempted to think that the following SQL query is secure because
the user input is just in the ORDER BY clause:

```sql
SELECT book_title FROM books ORDER BY {user_input}
```

where the developer expects `user_input` to be either `sales` or
`average_review`. However, an attacker could change `user_input` to this:

```sql
CASE WHEN
    (SELECT 1 FROM users
     WHERE username = "admin"
         AND SUBSTRING(password, 1, 1) = "a"
     ) = 1
     THEN sales
     ELSE average_review
END ASC
```

This way, the attacker can get the password hash of the admin user. Character by
character. Just by looking at how the sorting changes.

## See also

I love [Tom Scott](https://en.wikipedia.org/wiki/Tom_Scott_(entertainer)) and [Computerphile](https://www.youtube.com/user/Computerphile), and they made a video about the topic!

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/_jKylhJtPmI" frameborder="0" allowfullscreen></iframe></center>

## More in this series

In this series about application security (AppSec), we already explained some of the techniques of the attackers 😈 and also techniques of the defenders 😇:

* Part 1: **SQL Injections** 😈🐝
* Part 2: [Don’t leak Secrets](../leaking-secrets/) 😇
* Part 3: [Cross-Site Scripting (XSS)](../xss/) 😈🐝
* Part 4: [Password Hashing](../password-hashing/) 😇
* Part 5: [ZIP Bombs](../zip-bombs/) 😈
* Part 6: [CAPTCHA](../captcha/) 😇
* Part 7: [Email Spoofing](../email-spoofing/) 😈
* Part 8: [Software Composition Analysis](../sca/) (SCA) 😇
* Part 9: [XXE attacks](../xxe-attacks/) 😈🐝
* Part 10: [Effective Access Control](../effective-access-control/) 😇
* Part 11: [DoS via a Billion Laughs](../billion-laughs-dos/) 😈
* Part 12: [Full Disk Encryption](../full-disk-encryption/) 😇
* Part 13: [Insecure Deserialization](../insecure-deserialization/) 😈🐝
* Part 14: [Docker Security](../docker-security/) 😇
* Part 15: [Credential Stuffing](../credential-stuffing/) 😈🐝
* Part 16: [Multi-Factor Authentication](../multi-factor-authentication/) (MFA/2FA) 😇
* Part 17: [ReDoS](../redos/) 😈

The following articles are about to come:

* Part 18: Secure Messaging 😇
* Part 19: Cryptojacking 😈
* Part 20: Backups 😇
* Part 21: Cryptotrojans 😈
* Part 22: Single-Sign-On 😇
* Part 23: Clipboard Hijacking 😈
* Part 24: Certificates 😇
* Part 25: Race Condition Attacks in Blockchains 😈
* Part 26: Mobile Device Management (MDM) 😇
* Part 27: Server-Side Request Forgery (SSRF) 😈
* Part 28: Network Separation 😇
* Part 29: Social Engineering (including Phishing) 😈
* Part 30: Virtual Private Networks (VPNs) 😇
* Part 31: CSRF 😈

Let me know if you are interested in more articles around AppSec / InfoSec!
