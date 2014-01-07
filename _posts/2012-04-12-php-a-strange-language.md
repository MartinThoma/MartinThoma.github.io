---
layout: post
title: ! 'PHP: A strange language'
author: Martin Thoma
date: 2012-04-12 16:24:32.000000000 +02:00
categories:
- Code
tags:
- Programming
- PHP
featured_image: 2011/10/PHP-logo.png
---
<h2>Inconsistency</h2>
<h3>Starting and ending PHP</h3>
The following snippet is valid PHP-code:

```php
<?php 
    </script>
?>
```

Source: <a href="http://stackoverflow.com/q/13228306/562769">StackOverflow.com</a> (You can find some explanations there.)

<h3>Underscores</h3>
Some functions use underscores between words, while others do not:
<a href="http://php.net/gettype">gettype</a> vs. <a href="http://php.net/get_class">get_class</a>

<h3>Order of Arguments</h3>

```php
strpos ( string $haystack , mixed $needle [...] )
stristr ( string $haystack , mixed $needle [...] )
in_array ( mixed $needle , array $haystack [...] )
array_search ( mixed $needle , array $haystack [...] )
```

<h2>Sorting</h2>
```php
function pivot($arr) {
    return ($arr[0] + end($arr)) / 2;
}

$arr = array(1, 5, 7, 2, 3, 4, 8, 9, 6);
echo pivot(sort($arr));
```

This doesn't work. If you don't know why, you should take a look at <a href="http://php.net/manual/de/function.sort.php">sort</a>.

<h2>PHP Logo</h2>
Add '?=PHPE9568F34-D428-11d2-A769-00AA001ACF42' to any PHP script and take a look at the output. For example at <a href="http://en.wikipedia.org/wiki/Main_Page?=PHPE9568F34-D428-11d2-A769-00AA001ACF42">Wikipedia</a>.

<h2>Argument order</h2>

```php
mktime  ([$hour [, $minute [, $second [, $month  [, $day  [, $year  [, $is_dst]]]]]]])
```

<h2>array_fill</h2>
<a href="http://php.net/manual/en/function.array-fill.php">array_fill</a> doesn't allow 0 as $number.

```php
<?php

$number = 2;
$arr = array_fill(0, $number, 42);
print_r($arr);

?>
```

Array ( [0] => 42 [1] => 42 )

<h2>Strange loop</h2>
Loops themselves should not change anything. So take a look at this:

```php
<?php

$array = array('foo', 'bar');
var_dump($array);
foreach ($array as &amp;$foo);
var_dump($array);

?>
```

Output:
{% highlight text %}
array(2) {
  [0]=> string(3) "foo"
  [1]=> string(3) "bar"
}

array(2) {
  [0]=>  string(3) "foo"
  [1]=> &amp;string(3) "bar"
}
{% endhighlight %}

<h2>Boolean evaluation</h2>
```php
<?php

$a = array('7.1');

$arr1 = array(
  'foo' => 'foo',
  'bar' => 'bar',
);

$arr2 = array(
  'bar' => 'bar',
  'foo' => 'foo',
);

if ("a")  {echo "This ";}
if (true) {echo "is ";}
if (9)    {echo "PHP. ";}
if (07)   {echo "Oktal ";}
if (010 == 8 ) {echo "is ";}
if ("8" == 8 ) {echo "also ";}
if (array(0)) {echo "true. ";}
if ($x = 1)  {echo "Like ";}
if (in_array('7.10', $a)) {echo "that ";}
if ($arr1 == $arr2) {echo "one ";}
if (0 == 'x') {echo "is true.";}

if ("")      {echo "false ";}
if (0)       {echo "false";}
if (08)      {echo "false";}
if (array()) {echo "false";}
if ($x = 0)  {echo "false";}
if ($arr1 === $arr2) {echo "false";}

?>
```

<h2>Automatic conversion</h2>
<div class="info">This one seems to be fixed. It doesn't work in PHP Version 5.4.6-1ubuntu1.2 (released 16.08.2012). It was a problem in PHP 5.3.5 (released 06.01.2011)</div>

PHP converts strings automatically to a float if it is possible. This might lead to problems. See this example from <a href="http://phpsadness.com/sad/47">phpsadness</a>:

```php
<?php

$password = "ximaz";

$hash = "61529519452809720693702583126814"; // = md5("ximaz")

if (md5($password) == $hash) {
  print "Allowed!\n";
}

$wrong_hash = "61529519452809720000000000000000";
if ($wrong_hash == $hash) {
  print "Wrong hash got correct!\n";
}

?>
```

See also:
<ul>
  <li><a href="http://php.net/language.operators.comparison">Comparison Operators</a></li>
  <li><a href="https://bugs.php.net/bug.php?id=54547">Bug #54547: wrong equality of string numbers</a></li>
  <li><a href="https://bugs.php.net/bug.php?id=62097">Bug #62097: New behavior of string == has a compatibility problem</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Versionsgeschichte_von_PHP">Versionsgeschichte von PHP</a> (German)</li>
</ul>

<h2>Make a Guess</h2>
Try to guess what the following prints:

```php
<?php
for ($i = 'a'; $i <= 'z'; ++$i) echo "$i ";
 
// I just need four NULLs to demo this.
$a = array_fill(0, 4, NULL);
 
$a[0]++;
++$a[1];
$a[2]--;
--$a[3];
 
var_dump($a);

$b[0]++;
++$b[1];
$b[2]--;
--$b[3];
 
var_dump($b);
?>
```

Did you guess the following?

{% highlight text %}

a b c d e f g h i j k l m n o p q r s t u v w x y z aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az ba bb bc bd be bf bg bh bi bj bk bl bm bn bo bp bq br bs bt bu bv bw bx by bz ca cb cc cd ce cf cg ch ci cj ck cl cm cn co cp cq cr cs ct cu cv cw cx cy cz da db dc dd de df dg dh di dj dk dl dm dn do dp dq dr ds dt du dv dw dx dy dz ea eb ec ed ee ef eg eh ei ej ek el em en eo ep eq er es et eu ev ew ex ey ez fa fb fc fd fe ff fg fh fi fj fk fl fm fn fo fp fq fr fs ft fu fv fw fx fy fz ga gb gc gd ge gf gg gh gi gj gk gl gm gn go gp gq gr gs gt gu gv gw gx gy gz ha hb hc hd he hf hg hh hi hj hk hl hm hn ho hp hq hr hs ht hu hv hw hx hy hz ia ib ic id ie if ig ih ii ij ik il im in io ip iq ir is it iu iv iw ix iy iz ja jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq jr js jt ju jv jw jx jy jz ka kb kc kd ke kf kg kh ki kj kk kl km kn ko kp kq kr ks kt ku kv kw kx ky kz la lb lc ld le lf lg lh li lj lk ll lm ln lo lp lq lr ls lt lu lv lw lx ly lz ma mb mc md me mf mg mh mi mj mk ml mm mn mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni nj nk nl nm nn no np nq nr ns nt nu nv nw nx ny nz oa ob oc od oe of og oh oi oj ok ol om on oo op oq or os ot ou ov ow ox oy oz pa pb pc pd pe pf pg ph pi pj pk pl pm pn po pp pq pr ps pt pu pv pw px py pz qa qb qc qd qe qf qg qh qi qj qk ql qm qn qo qp qq qr qs qt qu qv qw qx qy qz ra rb rc rd re rf rg rh ri rj rk rl rm rn ro rp rq rr rs rt ru rv rw rx ry rz sa sb sc sd se sf sg sh si sj sk sl sm sn so sp sq sr ss st su sv sw sx sy sz ta tb tc td te tf tg th ti tj tk tl tm tn to tp tq tr ts tt tu tv tw tx ty tz ua ub uc ud ue uf ug uh ui uj uk ul um un uo up uq ur us ut uu uv uw ux uy uz va vb vc vd ve vf vg vh vi vj vk vl vm vn vo vp vq vr vs vt vu vv vw vx vy vz wa wb wc wd we wf wg wh wi wj wk wl wm wn wo wp wq wr ws wt wu wv ww wx wy wz xa xb xc xd xe xf xg xh xi xj xk xl xm xn xo xp xq xr xs xt xu xv xw xx xy xz ya yb yc yd ye yf yg yh yi yj yk yl ym yn yo yp yq yr ys yt yu yv yw yx yy yz 

array(4) {
  [0]=> int(1)
  [1]=> int(1)
  [2]=> NULL
  [3]=> NULL
}
array(4) {
  [0]=> int(1)
  [1]=> int(1)
  [2]=> NULL
  [3]=> NULL
}

{% endhighlight %}

<h2>Function names are NOT case sensitive</h2>

<blockquote>

```php
function add($a, $b)
{
    return $a + $b;
}

$foo = add(1, 2);
$Foo = Add(3, 4);

echo "foo is $foo"; // outputs foo is 3
echo "Foo is $Foo"; // outputs Foo is 7
```

</blockquote>
Source: <a href="http://stackoverflow.com/a/2006635/562769">StackOverflow</a>


<h2>Sources</h2>
<ul>
  <li><a href="http://phpsadness.com/">phpsadness.com</a></li>
  <li><a href="http://me.veekun.com/blog/2012/04/09/php-a-fractal-of-bad-design/">PHP: a fractal of bad design</a> (thanks to <a href="http://www.knallisworld.de/blog/2012/04/11/herrlicher-php-rant/">knallisworld.de</a>)</li>
  <li><a href="http://www.phpwtf.org/">phpwtf.org</a></li>
</ul>
