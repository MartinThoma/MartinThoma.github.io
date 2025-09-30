---
layout: post
lang: en
title: Comparing Dates in PHP and MySQL
author: Martin Thoma
date: 2011-10-04 20:22:12.000000000 +02:00
category: Code
tags: PHP, MySQL
featured_image: 2011/10/PHP-logo.png
---
Sometimes you need to know compare PHP dates. You need to know what is later or if both dates are the same.

<h2>PHP</h2>
<h3>time formats and functions</h3>
PHP knows these time / date formats:
<ul>
  <li>UNIX Timestamp: Integer - The number of seconds after 1970. Related functions are
    <ul>
       <li>int <a href="http://www.php.net/manual/en/function.mktime.php">`mktime([ int \$hour = date("H") [, int \$minute = date("i") [, int \$second = date("s") [, int \$month = date("n") [, int \$day = date("j") [, int \$year = date("Y") [, int \$is_dst = -1 ]]]]]]])`</a></li>
       <li>int <a href="http://www.php.net/manual/en/function.time.php">`time()`</a></li>
       <li>string <a href="http://www.php.net/manual/en/function.date.php">`date( string \$format [, int $timestamp = time() ] )`</a></li>
       <li>int <a href="http://www.php.net/manual/en/function.strtotime.php">`strtotime( string \$time [, int \$now ] )`</a>
I recommend using `YYYY-MM-DD HH:mm:ss` if possible.</li>
    </ul>
  </li>
  <li>Associative Arrays. The array looks like this

```php
Array
(
    [year] => 2006
    [month] => 12
    [day] => 12
    [hour] => 10
    [minute] => 0
    [second] => 0
    [fraction] => 0.5
    [warning_count] => 0
    [warnings] => Array()
    [error_count] => 0
    [errors] => Array()
    [is_localtime] =>
)
```

The related functions are:
    <ul>
        <li>array <a href="http://www.php.net/manual/en/function.date-parse.php">date_parse</a> (string $date)</li>
        <li>array <a href="http://php.net/manual/en/function.getdate.php">getdate</a> ([ int $timestamp = time() ] )</li>
    </ul>
  </li>
  <li><a href="http://php.net/manual/en/class.datetime.php">DateTime Class</a>: This class can do quite a lot. You should read the manual if you're interested in using it.</li>
</ul>

<h3>Comparisons</h3>
Comparing UNIX Timestamps is like comparing integers. No problem.

Comparing Arrays is more interesting. What do you think will the following script print?

```php
<?php

$d1 = date_parse ("2011-05-11");
$d2 = date_parse ("2011-05-11 13:00:00");

print_r($d1);
print_r($d2);

if ($d1 < $d2) {
    echo '$d1 is less than $d2.';
} else if ($d1 == $d2) {
    echo '$d1 is equal to $d2.';
} else {
    echo '$d1 is greater than $d2.';
}

?>
```

It prints '$d1 is less than $d2.' as

```php
date_parse ("2011-05-11");
```

is basically the same as

```php
date_parse ("2011-05-11 00:00:00");
```

You can compare the Array to an integer, but I don't know what PHP does. It seems as if the array would always be considered as being greater. If you use the functions you'll be fine.

<h2>MySQL</h2>
<h3>time formats and functions</h3>
MySQL knows these date and time <a href="http://dev.mysql.com/doc/refman/5.5/en/date-and-time-types.html">types</a> and those <a href="http://dev.mysql.com/doc/refman/5.5/en/date-and-time-functions.html">functions</a>. Here is a very short overview:
<ul>
    <li><a href="http://dev.mysql.com/doc/refman/5.5/en/datetime.html">DATETIME</a>: 'YYYY-MM-DD HH:MM:SS'
range is from '1000-01-01 00:00:00' to '9999-12-31 23:59:59'</li>
    <li><a href="http://dev.mysql.com/doc/refman/5.5/en/datetime.html">DATE</a>: 'YYYY-MM-DD'
range is from '1000-01-01' to '9999-12-31'</li>
    <li><a href="http://dev.mysql.com/doc/refman/5.5/en/datetime.html">TIMESTAMP</a>: like DATETIME, but
range is from '1970-01-01 00:00:01' UTC to '2038-01-19 03:14:07' UTC</li>
</ul>

Those examples show more than a long explanation:
```bash
mysql> SELECT CURTIME();
        -> '23:50:26'
# Adding zero will NOT convert it to a UNIX timestamp:
mysql> SELECT CURTIME() + 0;
        -> 235026.000000 # An "integered" TIME

mysql> SELECT NOW( )
        -> '2011-10-04 18:33:45'
# Adding zero is a bad idea here, too:
mysql> SELECT NOW( ) +0
        -> 20111004190945.000000 # An "integered" DATETIME
# If you want a UNIX Timestamp, use this function
mysql> SELECT UNIX_TIMESTAMP();
        -> 1317746025
mysql> SELECT UNIX_TIMESTAMP('2011-10-04 18:33:45');
        -> 1317746025
# You can also convert it:
mysql> SELECT UNIX_TIMESTAMP(`my_datetime_row`) FROM `my_table`

```

<h3>Comparisons</h3>
You can compare two DATETIMEs like this:

```sql
SELECT `my_row` FROM `my_table` WHEN `datetime1` < `datetime2`
```

It's of course not problem if you compare two UNIX Timestamps which are stored as integers in the database:

```sql
SELECT `my_row` FROM `my_table` WHEN `int1` < `int2`
```

But what happens if you compare a DATETIME with a Timestamp (integer)?

```sql
SELECT `my_row` FROM `my_table` WHEN `datetime1` < UNIX_TIMESTAMP()
```

This is basically:

```sql
SELECT `my_row` FROM `my_table` WHEN `datetime1` < 1317750167
```

And it compares the "integered" DATETIME 20111004210710 for 2011-10-04 21:07:10 with 1317750167. This is obviously crap. Don't do it. Never.
Instead you should convert your dates with UNIX_TIMESTAMP(your_datetime) or  FROM_UNIXTIME(unix_timestamp).

<h2>Comparing MySQL types with PHP types</h2>
The simplest way to compare MySQL DATE formats with PHP types is using strtotime(...) or date(...) if needed. If you have a DATETIME and you want to know if it's in the past, you can use

```php
if (strtotime($datetime) < time()) {
   echo '$datetime is in the past.';
}
```

<h2>From PHP to MySQL</h2>
If you have a date you got via an date input field and want to submit it to MySQL, just use this piece of code:

```php
$mysqlFormat = date('Y-m-d H:i:s', strtotime($_POST['my_date']));
```
