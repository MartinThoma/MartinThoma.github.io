---
layout: post
title: Google Code Jam 2012 &ndash; Round 1B 2012
author: Martin Thoma
date: 2012-05-05 21:20:45.000000000 +02:00
category: Code
tags: Programming, Python, Google, C, Google Code Jam, competition
featured_image: 2012/04/code-jam-logo.png
---
5614 tried the first problem, but only 3281 people are listed in the scoreboard. So quite a lot tried to solve a problem, but couldn't even solve one. I think these problems were much harder than the ones from <a href="../google-code-jam-2012-round-1a-2012/" title="Google Code Jam 2012 &ndash; Round 1A 2012">Round 1A 2012</a>.

<ul>
  <li>Problem 1 (<a href="http://code.google.com/codejam/contest/1836486/dashboard#s=p0">Safety in Numbers</a>):
  <ul>
     <li>Small Set: 2695/5614 users (48%)</li>
     <li>Large Set: 2016/2686 users (75%)</li>
  </ul>
  </li>
  <li>Problem 2 (<a href="http://code.google.com/codejam/contest/1836486/dashboard#s=p1">Tide Goes In, Tide Goes Out</a>):
  <ul>
     <li>Small Set: 684/894 users (77%)</li>
     <li>Large Set: 620/671 users (92%)</li>
  </ul>
  </li>
  <li>Problem 3 (<a href="http://code.google.com/codejam/contest/1836486/dashboard#s=p2">Equal Sums</a>):
  <ul>
     <li>Small Set: 2261/2534 users (89%)</li>
     <li>Large Set: 149/854 users (17%)</li>
  </ul>
  </li>
</ul>

<h2>Safety in Numbers</h2>
I tried this approach:
X is the sum of all points given by judges. The visitors have an equal amount of points to give. 
$P_i$ is the number of total points of contestant i.
$J_i$ is the number of points of contestant i by the judges.
$V_i$ is the percentage of the visitors points contestant i gets.

So: $P_i = J_i + V_i * X$

You don't know $V_i$ and $P_i$. You have to get the minimal value of $V_i$ to guarantee that contestant $i$ will not to be eliminated. So you have to create some kind of "worst case" for contestant i, if he gets $V_i \cdot X$ visitor-points. The worst case is that the minimum of all remaining visitors is as high as possible. So if you think of them as players, they will always try to get a equal number of points.

If they can get an equal number of points, you can make these (in)equations:
$average = (X - p_i)/(N-1)$
$p_i + V_i \cdot X \geq avg + \frac{1-V_i}{N-1} \cdot X$
$V_i \cdot X - \frac{1-V_i}{N-1}  \cdot X \geq avg - p_i$
$V_i X (N-1) - (1-V_i) \cdot X \geq (N-1) \cdot (avg - p_i)$
$V_i X (N-1) - X +V_i \cdot X \geq (N-1) \cdot (avg - p_i)$
$V_i X (N-1) +V_i \cdot X \geq (N-1) \cdot (avg - p_i) + X$
$V_i \geq (N-1) \cdot ((avg - p_i) + X)/(X (N-1) +X)$
$V_i \geq (N-1) \cdot ((avg - p_i) + X)/(X ((N-1) +1))$
$V_i \geq \frac{N-1}{X \cdot N} \cdot (avg - p_i + X)$

Unfortunately, its possible that the other players can't get an equal number of points. So this approach is useless in this case.

Here is an approach with an approximation, which also works for the large input set.
{% highlight cpp %}#include <iostream>
#include <cstdio>
using namespace std;

int main() {

	int testcases, N, sum;
	int s[1011];

	cin >> testcases;

	for (int caseNr = 1; caseNr <= testcases; caseNr++) {
		cin >> N;

		/** the sum of all points of all contestants*/
		sum = 0;

    	for (int i = 0; i < N; i++) {
			cin >> s[i];
			sum += s[i];
		}

		printf("Case #%d:", caseNr);

		for (int contestant = 0; contestant < N; contestant++) {
			// approximate the minimum for each contestant
			double low = 0, high = 1;

			// increase the accuracy 100 times
			for (int j = 0; j < 100; j++) {
				double mid = (low + high) / 2;
				double me = s[contestant] + mid * sum;
				double remaining = 1 - mid;

				for (int k = 0; k < N &amp;&amp; remaining > 0; k++) {
					if (k != contestant &amp;&amp; s[k] < me) {
						// the contestant k needs at least
						// this part of all audience votes
						remaining -= (me - s[k]) / sum;
					}
				}

				if (remaining > 0) {
					low = mid;
				} else {
					high = mid;
				}
			}
			printf(" %.6lf", low * 100);
		}

		printf("\n");
	}
}{% endhighlight %}

<h2>Tide Goes In, Tide Goes Out</h2>
This one could be solved with Graphs. You calculate one Graph, where every node is one cell. Every cell / node is connected to adjacent cells. Every cell has a value which is the time when you can enter them.

After you've created the graph, you can make something like that:
{% highlight python %}
graph = createGraph(floorHeight, ceilingHeight)
endReached = False
nodesReached = []
while (not endReached):
    tmp = getMinimumAdjacentNode(graph, nodesReached)
    nodesReached.append(tmp)
return maxTime(nodesReached)
{% endhighlight %}

<h2>Equal Sums</h2>
A trivial solution for the small one is to try every combination. You might want to take a look at Pythonss <a href="http://docs.python.org/library/itertools.html#itertools.combinations">itertools.combinations()</a>.

<h2>See also</h2>
<ul>
  <li>Wikipedia: <a href="http://en.wikipedia.org/wiki/Google_Code_Jam">Google Code Jam</a></li>
  <li><a href="http://www.go-hero.net/jam/12/">Google Code Jam Statistics</a></li>
</ul>
