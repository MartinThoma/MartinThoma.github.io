---
layout: post
title: Sign-in systems with PHP
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- PHP
- Salt
- Hash
- MD5
featured_image: logos/php.png
---

The following few lines explain how to create a sign-in system today. It
explains how to create hashes, how to sign-in and what to store.

## Prerequesites

* Either (PHP >=5.5) or (PHP >= 5.3.7 and [password_compat](https://github.com/ircmaxell/password_compat))
* Any SQL based database

## What to store

In MySQL you have something like this:

```sql
CREATE TABLE IF NOT EXISTS `wm_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(20) COLLATE utf8_bin NOT NULL,
  `email` varchar(255) COLLATE utf8_bin NOT NULL,
  `password` char(60) COLLATE utf8_bin NOT NULL,
  `confirmation_code` char(32) COLLATE utf8_bin NOT NULL,
  `status` enum('activated','deactivated') COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `display_name` (`display_name`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `confirmation_code` (`confirmation_code`),
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1;
```

Although you could take `email` as a primary key, I feel more comfortable by
using an auto incremented integer for that.

I will use `email` and `password` for sign in. Please note that `password`
will be a hashed version!

## Create a new account

The user enters a the username. While he does so, he should get feedback if the
username does already exist. Something like

```html
<form action="" method="post">
    <label for="display_name">Display name</label>
    <input type="text" placeholder="John Smith" id="display_name" name="display_name" />

    <label for="email">Email</label>
    <input type="email" placeholder="john.smith@gmail.com" id="email" name="email" />

    <label for="password">Password</label>
    <input type="password" id="password" name="password"/>

    <input type="submit" />
</form>
```

TODO: JavaScript to check if display name is already taken.

```sql
INSERT INTO  `wm_users` (
    `display_name` ,
    `email` ,
    `password` ,
    `confirmation_code` ,
    `status` 
) VALUES (
    :display_name, :email, :password, :confirmation_code, 'deactivated'
);
```

You should use prepared statments for this. One way to use prepared statements
is [PDO](http://php.net/pdo.prepared-statements).

### Generated hash

You generate the hash with

```php
$hash = password_hash($_POST['password'], PASSWORD_BCRYPT, array("cost" => 10));
```

and you store it directly like this in the database.

### Generate confirmation codes

As I don't really mind if people use their email address, I did no put
much effort in the confirmation code:

```php
$code = md5(rand());
```

### Account activation

Add a page `activate.php` which does

```php

if (isset($_GET['email']) && isset($_GET['code'])) {
    $sql = "UPDATE `wm_users` ".
           "SET status = 'activated' ".
           "WHERE `email` = :email AND `activation_code` = :code";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':email', $_GET['email'], PDO::PARAM_STR);
    $stmt->bindParam(':code', $_GET['code'], PDO::PARAM_STR);
    $result = $stmt->execute();
    if ($result->rowCount() == 1) {
        echo "Congratulations, you've actived your account.";
    }
}


```

## Sign in

```html
<form action="signin.php" method="post">
    <label for="email">Email</label>
    <input type="email" placeholder="john.smith@gmail.com" id="email" name="email" />

    <label for="password">Password</label>
    <input type="password" id="password" name="password"/>

    <input type="submit" />
</form>
```

`signin.php`

```php
session_start();

if (isset($_POST['email']) && isset($_POST['password'])) {
    $sql = "SELECT `id`, `password`, `status` ".
           "FROM `wm_users` WHERE `email` = :email";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':email', $_POST['email'], PDO::PARAM_STR);
    $stmt->execute();
    $user = $stmt->fetchObject();

    if ($user->id > 0 && password_verify($_POST['password'], $row->password)) {
        $_SESSION['uid'] = $user->id;
        $_SESSION['display_name'] = $row->display_name;
        $_SESSION['upass'] = $upass;
        $_SESSION['is_logged_in'] = true;
        return true;
    } else {
        $_SESSION['is_logged_in'] = false;
        $_SESSION['uid'] = NULL;
        $_SESSION['display_name'] = NULL;
        $_SESSION['upass'] = NULL;
    }
}
```

## Sign out

See [`session_destroy`](http://www.php.net/manual/en/function.session-destroy.php)

## Password reset

HTML:

```html
<h1>Reset password</h1>

<form action="reset.php" method="post">
    <label for="email">Email</label>
    <input type="email" placeholder="john.smith@gmail.com" id="email" name="email" />

    <input type="submit" />
</form>
```

You might consider adding a "security question" so that not every idiot can
get on your users nerves by resetting the password (or at least trying to do so).

`reset.php`

```php

function generate_message($email, $confirmation_code) {
    return "Hello [username],\n".
           "Your reset link is http://example.com/reset/?email=$email&code=$confirmation_code";
}


if (isset($_POST['email'])) {
    $sql = "UPDATE `wm_users` ".
           "SET `activation_code` = :code ".
           "WHERE `email` = :email AND status = 'activated';";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':email', $_POST['email'], PDO::PARAM_STR);
    $confirmation_code = md5(rand())
    $stmt->bindParam(':code', confirmation_code, PDO::PARAM_STR);
    $result = $stmt->execute();
    if ($result->rowCount() == 1) {
        mail($_POST['email'],
             "Password reset",
             generate_message($_POST['email'], confirmation_code)
        );
        echo "An email has been sent with a confirmation code to reset your password.";
    }
}

if (isset($_GET['code'])) {
    // TODO: select database by email and confirmation code
    // Set password to something readable randomly
    // Email new password to user
}
```

## Further information

* PHP Manual
  * [`password_hash`](http://www.php.net/manual/en/function.password-hash.php)
  * [FAQ: Safe Password Hashing](http://www.php.net/manual/en/faq.passwords.php)
* [What column type/length should I use for storing a Bcrypt hashed password in a Database?](http://stackoverflow.com/q/5881169/562769)