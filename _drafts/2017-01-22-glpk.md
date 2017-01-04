---
layout: post
title: How to use GLPK
author: Martin Thoma
date: 2012-09-07 05:59:55
categories: 
- Code
tags: 
- GLPK
featured_image: 2012/09/gnu-head-sm.png
---
GLPK, the GNU Linear Programming Kit, is a piece of software which solves linear optimization problems. You only have to modell the problem.

## Assignment problem
The <a href="http://en.wikipedia.org/wiki/Assignment_problem">assignment problem</a>

This file is in the examples of GLPK

```c
param m, integer, > 0;
/* number of agents */

param n, integer, > 0;
/* number of tasks */

set I := 1..m;
/* set of agents */

set J := 1..n;
/* set of tasks */

param c{i in I, j in J}, >= 0;
/* cost of allocating task j to agent i */

var x{i in I, j in J}, >= 0;
/* x[i,j] = 1 means task j is assigned to agent i
   note that variables x[i,j] are binary, however, there is no need to
   declare them so due to the totally unimodular constraint matrix */

s.t. phi{i in I}: sum{j in J} x[i,j] <= 1;
/* each agent can perform at most one task */

s.t. psi{j in J}: sum{i in I} x[i,j] = 1;
/* each task must be assigned exactly to one agent */

minimize obj: sum{i in I, j in J} c[i,j] * x[i,j];
/* the objective is to find a cheapest assignment */

solve;

printf "\n";
printf "Agent  Task       Cost\n";
printf{i in I} "%5d %5d %10g\n", i, sum{j in J} j * x[i,j],
   sum{j in J} c[i,j] * x[i,j];
printf "----------------------\n";
printf "     Total: %10g\n", sum{i in I, j in J} c[i,j] * x[i,j];
printf "\n";

data;

/* These data correspond to an example from [Christofides]. */

/* Optimal solution is 76 */

param m := 8;

param n := 8;

param c : 1  2  3  4  5  6  7  8 :=
      1  13 21 20 12  8 26 22 11
      2  12 36 25 41 40 11  4  8
      3  35 32 13 36 26 21 13 37
      4  34 54  7  8 12 22 11 40
      5  21  6 45 18 24 34 12 48
      6  42 19 39 15 14 16 28 46
      7  16 34 38  3 34 40 22 24
      8  26 20  5 17 45 31 37 43 ;

end;
```

## See also
<ul>
  <li><a href="http://www.gnu.org/software/glpk/">GLPK Documentation</a></li>
  <li>IBM: <a href="http://www.ibm.com/developerworks/linux/library/l-glpk1/">Introduction to linear optimization</a>, <a href="http://www.ibm.com/developerworks/linux/library/l-glpk2/">Intermediate problems in linear programming</a>, <a href="http://www.ibm.com/developerworks/linux/library/l-glpk3/">Advanced problems and elegant solutions</a></li>
</ul>
