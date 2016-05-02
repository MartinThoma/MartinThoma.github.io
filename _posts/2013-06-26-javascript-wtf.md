---
layout: post
title: JavaScript: WTF?!?
author: Martin Thoma
date: 2013-06-26 22:51:52.000000000 +02:00
category: Code
tags: JavaScript
---
JavaScript is THE web programming language. It gets interpreted by your browser and web applications like Google Mail, Google Maps and Facebook make heavy use of them. Almost always, when you see something working smoothly / interactive, you see JavaScript in action.

But JavaScript has a lot of "features" which are ... well, I don't have words for those. Just continue reading.

Most of the following content is from a StackOverflow question <a href="http://stackoverflow.com/q/1995113/562769">Strangest language feature</a>

<h2>Weak typing</h2>
<strong>Example</strong>
```javascript
console.log(3..toString());
```

<strong>Output</strong>
```bash
'3'
```

<strong>Explanation</strong>
<strong>3.</strong> is a floating point and can get converted to a string. But <code>3.toString()</code> gives 
```bash
SyntaxError: Unexpected token ILLEGAL 
```

<h2>Weak typing and string concatenation</h2>
<strong>Example</strong>
```javascript

console.log('5' + 3);
console.log('5' - 3);

```

<strong>Output</strong>
```bash
'53'
2
```

<strong>Explanation</strong>
JavaScript automatically converts datatypes and <code>+</code> is used for string concatenation and for addition. 

In the first case, as the first datatype is a string and <code>+</code> is defined for strings as concatenation, JS converts <code>3</code> to <code>'3'</code> which results in the string <code>'53'</code>.

In the second case, <code>-</code> is only defined for subtraction so <code>'5'</code> gets converted to a number (int? float? I don't know. I guess int.)

<h2>Automatic semicolons</h2>
<strong>Example 1</strong>

```javascript

function test() {
    return
    {
        id : 1338,
        title : 'This is a test'
    };
}

console.log(test());

```

<strong>Example 2</strong>
```javascript

function test() {
    return
        2 + 2;
}

console.log(test());

```

<strong>Output 1</strong>
```bash
Uncaught SyntaxError: Unexpected token :
```

<strong>Output 2</strong>
```bash
undefined
```

<strong>Explanation</strong>
JS adds a <code>;</code> at every line end. Automatically. You can't prevent it.

Please note that the second output is no error! It has a (valid) return value of <code>undefined</code>.

<h2>Truth table</h2>
<strong>Example</strong>
```javascript

console.log("------- 0 == XYZ ---------");
console.log(0 == 0);
console.log(0 == false);
console.log(0 == '');
console.log(0 == null);
console.log(0 == undefined);
console.log(0 == " \t\r\n");
console.log(0 == '0');
console.log(0 == 'false');
console.log("------- false == XYZ ---------");
console.log(false == false);
console.log(false == '');
console.log(false == null);
console.log(false == undefined);
console.log(false == " \t\r\n");
console.log(false == '0');
console.log(false == 'false');
console.log("------- '' == XYZ ---------");
console.log('' == '');
console.log('' == null);
console.log('' == undefined);
console.log('' == " \t\r\n");
console.log('' == '0');
console.log('' == 'false');
console.log("------- null == XYZ ---------");
console.log(null == null);
console.log(null == undefined);
console.log(null == " \t\r\n");
console.log(null == '0');
console.log(null == 'false');
console.log("------- undefined == XYZ ---------");
console.log(undefined == undefined);
console.log(undefined == " \t\r\n");
console.log(undefined == '0');
console.log(undefined == 'false');
console.log("-------  \t\r\n == XYZ ---------");
console.log(" \t\r\n" == " \t\r\n");
console.log(" \t\r\n" == '0');
console.log(" \t\r\n" == 'false');
console.log("------- '0' == XYZ ---------");
console.log('0' == '0');
console.log('0' == 'false');
console.log("------- 'false' == XYZ ---------");
console.log('false' == 'false');
console.log("--------------------");
console.log("-------  XYZ == 0 ---------");
console.log(0 == 0);
console.log(false == 0);
console.log('' == 0);
console.log(null == 0);
console.log(undefined == 0);
console.log(" \t\r\n" == 0);
console.log('0' == 0);
console.log('false' == 0);
console.log("-------  XYZ == false ---------");
console.log(false == false);
console.log('' == false);
console.log(null == false);
console.log(undefined == false);
console.log(" \t\r\n" == false);
console.log('0' == false);
console.log('false' == false);
console.log("-------  XYZ == '' ---------");
console.log('' == '');
console.log(null == '');
console.log(undefined == '');
console.log(" \t\r\n" == '');
console.log('0' == '');
console.log('false' == '');
console.log("-------  XYZ == null ---------");
console.log(null == null);
console.log(undefined == null);
console.log(" \t\r\n" == null);
console.log('0' == null);
console.log('false' == null);
console.log("-------  XYZ == undefined ---------");
console.log(undefined == undefined);
console.log(" \t\r\n" == undefined);
console.log('0' == undefined);
console.log('false' == undefined);
console.log("-------  XYZ == \t\r\n ---------");
console.log(" \t\r\n" == " \t\r\n");
console.log('0' == " \t\r\n");
console.log('false' == " \t\r\n");
console.log("-------  XYZ == '0' ---------");
console.log('0' == '0');
console.log('false' == '0');
console.log("-------  XYZ == 'false' ---------");
console.log('false' == 'false');

```

<strong>Output</strong>

<table>
<tr>
    <th>==</th>
    <th>0</th>
    <th>false</th>
    <th>''</th>
    <th>null</th>
    <th>undefined</th>
    <th>" \t\r\n"</th>
    <th>'0'</th>
    <th>'false'</th>
</tr>
<tr>
    <th>0</th>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: red;">false</td>
</tr>
<tr>
    <th>false</th>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: red;">false</td>
</tr>
<tr>
    <th>''</th>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
</tr>
<tr>
    <th>null</th>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
</tr>
<tr>
    <th>undefined</th>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
</tr>
<tr>
    <th>" \t\r\n"</th>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
</tr>
<tr>
    <th>'0'</th>
    <td style="background-color: lime;">true</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: lime;">true</td>
    <td style="background-color: red;">false</td>
</tr>
<tr>
    <th>'false'</th>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: red;">false</td>
    <td style="background-color: lime;">true</td>
</tr>
</table>

<strong>Explanation</strong>
Wow. This is fucked up. I've expected that strings compared to anything that is not the string itself evaluates to false.

At least the table is symmetric and the diagonal is true. Please also note that JavaScript has a <code>===</code> operator.

<h2>The truth</h2>
<strong>Example</strong>
```javascript

console.log(2 == [2]);
console.log(2 == [[2]]);

```

<strong>Output</strong>
```bash

true
true

```

<strong>Explanation</strong>
At <a href="http://stackoverflow.com/a/1724551/562769">StackOverflow</a>

<h2>Date</h2>
<strong>Example</strong>
```javascript

var futureDate = new Date(2010,77,154);
console.log(futureDate);
console.log(futureDate.getYear());

```

<strong>Output</strong>
```bash
Tue Nov 01 2016 00:00:00 GMT+0100 (CET) 
116
```

<strong>Explanation</strong>
77 months and 154 days from the 0th day of 0th month of 2010

You should use <code>getFullYear()</code> instead of <code>getYear()</code>, as the later one returns <code>year - 1900</code> (Why? When is this useful?)

<h2>Integer overflow</h2>
<strong>Example</strong>
```javascript

console.log(111111111111111111111);

```

<strong>Output</strong>
```bash
111111111111111110000 
```

<strong>Explanation</strong>
It's ok that JavaScript fails at handling this integer. I think it converts this to a float, but I'm not sure about that. But no matter what it does here, it doesn't throw an error. That's bad. How is a developer supposed to know in a big application know when something went wrong?

<h2>Function parameters</h2>
<blockquote>In Javascript, declaring the parameters a function accepts is only a convenience to the programmer. All variables passed through the function call are accessible by the keyword <code>arguments</code>. So the following would alert "world":
```javascript

function blah(){
    alert(arguments[1]);
}

blah("hello", "world");

```
</blockquote>
<a href="http://stackoverflow.com/a/2023908/562769">Source</a> on StackOverflow

<h2>Global variables</h2>
<strong>Example</strong>
```javascript

var a = 12;

function test() {
  a = 1337;
}
test();
console.log(a);

```

<strong>Output</strong>
```bash
1337
```

<strong>Explanation</strong>
When you forget to use <code>var</code> inside of <code>test()</code> you might accidentally use a global variable. 

<h2>See also</h2>
Do you know some more JavaScript WTFs?

You might also be interested in <a href="../php-a-strange-language/" title="PHP: A strange language">PHP: A strange language</a>
