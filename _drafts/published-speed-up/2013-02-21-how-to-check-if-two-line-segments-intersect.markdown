---
layout: post
status: publish
published: true
title: How to check if two line segments intersect
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 57571
wordpress_url: http://martin-thoma.com/?p=57571
date: 2013-02-21 12:19:05.000000000 +01:00
categories:
- Code
tags:
- Java
- algorithms
- Geometry
comments:
- id: 1185251
  author: Bryan Hanson
  author_email: hanson@depauw.edu
  author_url: ''
  date: !binary |-
    MjAxMy0wNC0yNiAxNTozODo0NyArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0yNiAxMzozODo0NyArMDIwMA==
  content: ! "Martin, thanks for this very excellent post.  One of the best explanations
    I've seen.  I have ported some of your code to R.  I'd like to put it up as a
    gist and of course use it.  Do you consider this code released to the public domain?
    \ I want to use it under the GPL-3 license that R typically uses.\r\n\r\nThanks
    again.  Bryan"
- id: 1185311
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wNC0yNiAxOTozMjoyMiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0yNiAxNzozMjoyMiArMDIwMA==
  content: ! "Hi Bryan,\r\n\r\nI think that the code I've written is not complex enough
    to have the German \"Urheberrecht\" (which is not quite the same as copyright).\r\n\r\nSo:
    Feel free to use it for any purpose (re-writing it, selling it, with or without
    giving credit to me and this article (although I would appreciate a link)).\r\nI've
    added a MIT license to the repository to make the copyright situation a bit more
    clear.\r\n\r\nI'm glad that actually somebody read my article :-)\r\n\r\nCheers,\r\nMartin"
- id: 1185381
  author: Bryan Hanson
  author_email: hanson@depauw.edu
  author_url: ''
  date: !binary |-
    MjAxMy0wNC0yNyAwMTo0Nzo0MSArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0yNiAyMzo0Nzo0MSArMDIwMA==
  content: ! "Great, and thanks again!  See here for the gist:\r\n\r\nhttps://gist.github.com/bryanhanson/5471173\r\n\r\nIt
    includes a graphical test that uses random line segments; everything seems to
    work.  By the way, I found your blog/code via one of your answers on Stack
    Overflow."
- id: 1186501
  author: Mecit Sarı
  author_email: mct.sari@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNC0yOCAyMjoyMDoxOSArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0yOCAyMDoyMDoxOSArMDIwMA==
  content: Thanks for the post, I have translated your code of intersection part to
    a part of my project and now it works like a charm. Very clear, clever explanation,
    thanks again!
- id: 1225721
  author: Brno
  author_email: paytamouss@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNi0yNyAyMDozNzoyMyArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNi0yNyAxODozNzoyMyArMDIwMA==
  content: ! "Hi,\r\n\r\nWonderful, thank you very much, it is very useful.\r\n\r\nHowever
    if I may suggest something, there is no method that returns the intersection point
    once we know that two lines intersects. I suppose it should be easy to find (when
    one is really at ease with the code, and I am not :))\r\n\r\nDo you think you
    might provide such a method?\r\n\r\nThanks anyway!\r\nBruno"
- id: 1225791
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wNi0yOCAxMToyMDozNiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNi0yOCAwOToyMDozNiArMDIwMA==
  content: ! "Hi Brno,\r\n\r\nI don't think I'll provide such a method. But this is
    how I would approach the problem:\r\n\r\n\r\n0. Check if they have an intersection\r\n1.
    Try to get the line equations: \r\n\r\nA line (that is not parallel to the y-axis)
    section has four interesting properties:\r\nx_min, x_max, m and t\r\n\r\nline
    equation holds for every point (x,y) on the line:\r\n\r\ng1: y = m1*x + t1\r\ng2:
    y = m2*x + t2\r\n\r\nSo choose two points (e.g. endpoints) on the line and solve
    for m and t.\r\n\r\n2. set them equal:\r\n\r\ng1 = g2\r\n\r\nm1*x +t1 = m2*x +t2\r\n\r\n3.
    Solve for x\r\n\r\nSpecial cases (that are easier, but you have to think about
    them and solve them separately):\r\n\r\n1. one line segment is parallel to y-axis\r\n2.
    both line segments are parallel to y-axis\r\n\r\nAnd one special case that is
    difficult:\r\n\r\n3. there is more then one intersection point"
- id: 1236051
  author: Bryan Hanson
  author_email: hanson@depauw.edu
  author_url: ''
  date: !binary |-
    MjAxMy0wNy0zMCAxNzowMjo1NyArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNy0zMCAxNTowMjo1NyArMDIwMA==
  content: ! "Brno, here it is in R:\r\n\r\n\tlineIntersection <- function(x1, y1,
    x2, y2, x3, y3, x4, y4) {\r\n\t\t\r\n\t\t# Finds the intersection of two lines\r\n\t\t#
    specified as two line segments\r\n\t\t# Based on code initially written by M.
    Kukurugya\r\n\t\t\r\n\t\tden <- (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)\r\n#\t\tif
    (den == 0) stop(\"No intersection found\")\r\n\t\tif (den == 0) return(NA)\r\n\t\tnumA
    <- ((x1 * y2) - (y1 * x2))\r\n\t\tnumB <- ((x3 * y4) - (y3 * x4))\r\n\t\tnum1
    <-  numA * (x3 - x4)\r\n\t\tnum2 <- (x1 - x2) * numB\r\n\t\tnum3 <- numA * (y3
    -y4)\r\n\t\tnum4 <- (y1 - y2) * numB \r\n\t\tPx = (num1 - num2)/den\r\n\t\tPy
    = (num3 - num4)/den\r\n\t\t# cat(\"Px is\", Px, \"\\n\")\r\n\t\t# cat(\"Py
    is\", Py, \"\\n\")\r\n\t\treturn(c(Px, Py))\r\n\t\t}\r\n\r\nYou can either stop
    if there is no intersection, or return a value you can test for in a loop and
    increment the counter."
- id: 1237898
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0xMC0wMyAxNDo1NjoxNSArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0xMC0wMyAxMjo1NjoxNSArMDIwMA==
  content: Today, I've written some code that calculates the intersection :-)
---
You have to line segments and you want to know if they intersect. I'll give you an algorithm how to do it.

<h2>Test cases</h2>
First of all, we should think about how lines can be arranged:

[gallery columns="4" ids="57661,57671,57681,57691,57701,57711,57581,57591,57601,57611,57621,57631,57641,57651"]

<h2>Bounding boxes</h2>
You can draw boxes around line segments such that the edges of the boxes are in parallel to the coordinate axes:

[caption id="attachment_57731" align="aligncenter" width="250"]<a href="http://martin-thoma.com/wp-content/uploads/2013/02/line-segments-bounding-box.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/02/line-segments-bounding-box-250x300.png" alt="Two line segments with their bounding boxes" width="250" height="300" class="size-medium wp-image-57731" /></a> Two line segments with their bounding boxes[/caption]

With this image in mind, it is obvious that the bounding boxes need to intersect if the lines should intersect. At this point you have to make a decision: If the endpoint of one line is on the other line, is this an intersection? I think so. If two lines have at least one point in common, they intersect. If two bounding boxes have at least one point in common, they intersect.

It is much easier to check if two bounding boxes intersect. It's simply:

{% highlight java %}/**
 * Check if bounding boxes do intersect. If one bounding box
 * touches the other, they do intersect.
 * @param a first bounding box
 * @param b second bounding box
 * @return <code>true</code> if they intersect,
 *         <code>false</code> otherwise.
 */
public boolean doBoundingBoxesIntersect(Point[] a, Point[] b) {
    return a[0].x <= b[1].x 
        &amp;&amp; a[1].x >= b[0].x 
        &amp;&amp; a[0].y <= b[1].y
        &amp;&amp; a[1].y >= b[0].y;
}{% endhighlight %}

If you have difficulties to understand why this works, take a look at this great <a href="http://silentmatt.com/rectangle-intersection/">animation for this formula</a>.

<h2>The algorithm</h2>
[caption id="attachment_57771" align="aligncenter" width="500"]<a href="http://martin-thoma.com/wp-content/uploads/2013/02/flowchart.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/02/flowchart.png" alt="Flowchart how to check if two lines intersect" width="500" height="228" class="size-full wp-image-57771" /></a> Flowchart how to check if two lines intersect[/caption]

Looks quite simple, doesn't it?

<h3>Cross product</h3>
Well, you might notice that you need to check if one line intersects with a given line segment. To check this, you have to understand one cool idea:

You can definie a cross product for points: 
$\begin{align}
  \times_P&: Point \times Point \rightarrow \mathbb{R}\\
  \times_P(a, b) &:= a.x \cdot b.y - b.x \cdot a.y;
\end{align}$

This cross product has one nice characteristics:
$a \times_P b = 0 \Leftrightarrow a$ and $b$ are on one line through origin</li>

You can verify this. If you take two points on a line through origin, they have the same slope $\frac{\Delta y}{\Delta x}$:
$
\begin{align}
  0 &= a \times_P b\\
\Leftrightarrow 0 &= a.x \cdot b.y - b.x \cdot a.y\\
\Leftrightarrow b.x \cdot a.y &= a.x \cdot b.y\\
\Leftrightarrow \frac{a.y}{a.x} &= \frac{b.y}{b.x}
\end{align}
$

Ok, now you can check if a point is on a line:
{% highlight java %}    /**
     * Checks if a Point is on a line
     * @param a line (interpreted as line, although given as line
     *                segment)
     * @param b point
     * @return <code>true</code> if point is on line, otherwise
     *         <code>false</code>
     */
    public boolean isPointOnLine(LineSegment a, Point b) {
        // Move the image, so that a.first is on (0|0)
        LineSegment aTmp = new LineSegment(new Point(0, 0), new Point(
                a.second.x - a.first.x, a.second.y - a.first.y));
        Point bTmp = new Point(b.x - a.first.x, b.y - a.first.y);
        double r = crossProduct(aTmp.second, bTmp);
        return Math.abs(r) < EPSILON;
    }{% endhighlight %}

The second cool characteristic of the cross product is that it can be used to determine if a point b is left or right of the line through the origin and a point a:

{% highlight java %}    /**
     * Checks if a point is right of a line. If the point is on the
     * line, it is not right of the line.
     * @param a line segment interpreted as a line
     * @param b the point
     * @return <code>true</code> if the point is right of the line,
     *         <code>false</code> otherwise
     */
    public boolean isPointRightOfLine(LineSegment a, Point b) {
        // Move the image, so that a.first is on (0|0)
        LineSegment aTmp = new LineSegment(new Point(0, 0), new Point(
                a.second.x - a.first.x, a.second.y - a.first.y));
        Point bTmp = new Point(b.x - a.first.x, b.y - a.first.y);
        return crossProduct(aTmp.second, bTmp) < 0;
    }{% endhighlight %}

When we have one line $a$ through the origin and one line segment $b$, you can check if $b$ crosses $a$ by checking if the end points of $b$ are on different sides of $a$:

{% highlight java %}    /**
     * Check if line segment first touches or crosses the line that is 
     * defined by line segment second.
     *
     * @param first line segment interpreted as line
     * @param second line segment
     * @return <code>true</code> if line segment first touches or
     *                           crosses line second,
     *         <code>false</code> otherwise.
     */
    public boolean lineSegmentTouchesOrCrossesLine(LineSegment a,
            LineSegment b) {
        return isPointOnLine(a, b.first)
                || isPointOnLine(a, b.second)
                || (isPointRightOfLine(a, b.first) ^ 
                    isPointRightOfLine(a, b.second));
    }{% endhighlight %}

Now you have everything you need:
{% highlight java %}    /**
     * Check if line segments intersect
     * @param a first line segment
     * @param b second line segment
     * @return <code>true</code> if lines do intersect,
     *         <code>false</code> otherwise
     */
    public boolean doLinesIntersect(LineSegment a, LineSegment b) {
        Point[] box1 = a.getBoundingBox();
        Point[] box2 = b.getBoundingBox();
        return doBoundingBoxesIntersect(box1, box2)
                &amp;&amp; lineSegmentTouchesOrCrossesLine(a, b)
                &amp;&amp; lineSegmentTouchesOrCrossesLine(b, a);
    }{% endhighlight %}

By the way, testcase F5 is the only reason why you need <code>doBoundingBoxesIntersect(box1, box2)</code>. All other tests still pass if you remove this function.

<h2>Where do two line segments intersect?</h2>
When you know that two line segments intersect, you can also calculate the intersection.
The intersection could be a line or only a point. 

I did this with JavaScript:
<iframe src="http://martin-thoma.com/html5/line-segment-intersection/" width="800" height="600">
  <p>Ihr Browser kann leider keine eingebetteten Frames anzeigen. Die Seite ist <a href="http://martin-thoma.com/html5/line-segment-intersection/">hier</a>.</p>
</iframe>

This is the code that checks for line segments:
{% highlight javascript %}
/** You know that lines a and b have an intersection and now you
    want to get it!
*/
function getIntersection(a, b) {
    /* the intersection [(x1,y1), (x2, y2)]
       it might be a line or a single point. If it is a line,
       then x1 = x2 and y1 = y2.  */
    var x1, y1, x2, y2;

   if (a["first"]["x"] == a["second"]["x"]) {
        // Case (A)
        // As a is a perfect vertical line, it cannot be represented
        // nicely in a mathematical way. But we directly know that
        //
        x1 = a["first"]["x"];
        x2 = x1;
        if (b["first"]["x"] == b["second"]["x"]) {
            // Case (AA): all x are the same!
            // Normalize
            if(a["first"]["y"] > a["second"]["y"]) {
                a = {"first": a["second"], "second": a["first"]};
            }
            if(b["first"]["y"] > b["second"]["y"]) {
                b = {"first": b["second"], "second": b["first"]};
            }
            if(a["first"]["y"] > b["first"]["y"]) {
                var tmp = a;
                a = b;
                b = tmp;
            }

            // Now we know that the y-value of a["first"] is the 
            // lowest of all 4 y values
            // this means, we are either in case (AAA):
            //   a: x--------------x
            //   b:    x---------------x
            // or in case (AAB)
            //   a: x--------------x
            //   b:    x-------x
            // in both cases:
            // get the relavant y intervall
            y1 = b["first"]["y"];
            y2 = Math.min(a["second"]["y"], b["second"]["y"]);
        } else {
            // Case (AB)
            // we can mathematically represent line b as
            //     y = m*x + t <=> t = y - m*x
            // m = (y1-y2)/(x1-x2)
            var m, t;
            m = (b["first"]["y"] - b["second"]["y"])/
                (b["first"]["x"] - b["second"]["x"]);
            t = b["first"]["y"] - m*b["first"]["x"];
            y1 = m*x1 + t;
            y2 = y1
        }
    } else if (b["first"]["x"] == b["second"]["x"]) {
        // Case (B)
        // essentially the same as Case (AB), but with
        // a and b switched
        x1 = b["first"]["x"];
        x2 = x1;
        
        var tmp = a;
        a = b;
        b = tmp;

        var m, t;
        m = (b["first"]["y"] - b["second"]["y"])/
            (b["first"]["x"] - b["second"]["x"]);
        t = b["first"]["y"] - m*b["first"]["x"];
        y1 = m*x1 + t;
        y2 = y1
    } else {
        // Case (C)
        // Both lines can be represented mathematically
        var ma, mb, ta, tb;
        ma = (a["first"]["y"] - a["second"]["y"])/
             (a["first"]["x"] - a["second"]["x"]);
        mb = (b["first"]["y"] - b["second"]["y"])/
             (b["first"]["x"] - b["second"]["x"]);
        ta = a["first"]["y"] - ma*a["first"]["x"];
        tb = b["first"]["y"] - mb*b["first"]["x"];
        if (ma == mb) {
            // Case (CA)
            // both lines are in parallel. As we know that they 
            // intersect, the intersection could be a line
            // when we rotated this, it would be the same situation 
            // as in case (AA)

            // Normalize
            if(a["first"]["x"] > a["second"]["x"]) {
                a = {"first": a["second"], "second": a["first"]};
            }
            if(b["first"]["x"] > b["second"]["x"]) {
                b = {"first": b["second"], "second": b["first"]};
            }
            if(a["first"]["x"] > b["first"]["x"]) {
                var tmp = a;
                a = b;
                b = tmp;
            }

            // get the relavant x intervall
            x1 = b["first"]["x"];
            x2 = Math.min(a["second"]["x"], b["second"]["x"]);
            y1 = ma*x1+ta;
            y2 = ma*x2+ta;
        } else {
            // Case (CB): only a point as intersection:
            // y = ma*x+ta
            // y = mb*x+tb
            // ma*x + ta = mb*x + tb
            // (ma-mb)*x = tb - ta
            // x = (tb - ta)/(ma-mb)
            x1 = (tb-ta)/(ma-mb);
            y1 = ma*x1+ta;
            x2 = x1;
            y2 = y1;
        }
    }

    return {"first": {"x":x1, "y":y1}, "second": {"x":x2, "y":y2}};
}
{% endhighlight %}

<h2>TL;DR</h2>
The complete, tested code is on <a href="https://github.com/MartinThoma/algorithms/tree/master/crossingLineCheck/Geometry/src">GitHub</a>. Here is the most important part:

{% highlight java %}public class Geometry {

    public static final double EPSILON = 0.000001;

    /**
     * Calculate the cross product of two points.
     * @param a first point
     * @param b second point
     * @return the value of the cross product
     */
    public static double crossProduct(Point a, Point b) {
        return a.x * b.y - b.x * a.y;
    }

    /**
     * Check if bounding boxes do intersect. If one bounding box
     * touches the other, they do intersect.
     * @param a first bounding box
     * @param b second bounding box
     * @return <code>true</code> if they intersect,
     *         <code>false</code> otherwise.
     */
    public static boolean doBoundingBoxesIntersect(Point[] a, Point[] b) {
        return a[0].x <= b[1].x &amp;&amp; a[1].x >= b[0].x &amp;&amp; a[0].y <= b[1].y
                &amp;&amp; a[1].y >= b[0].y;
    }

    /**
     * Checks if a Point is on a line
     * @param a line (interpreted as line, although given as line
     *                segment)
     * @param b point
     * @return <code>true</code> if point is on line, otherwise
     *         <code>false</code>
     */
    public static boolean isPointOnLine(LineSegment a, Point b) {
        // Move the image, so that a.first is on (0|0)
        LineSegment aTmp = new LineSegment(new Point(0, 0), new Point(
                a.second.x - a.first.x, a.second.y - a.first.y));
        Point bTmp = new Point(b.x - a.first.x, b.y - a.first.y);
        double r = crossProduct(aTmp.second, bTmp);
        return Math.abs(r) < EPSILON;
    }

    /**
     * Checks if a point is right of a line. If the point is on the
     * line, it is not right of the line.
     * @param a line segment interpreted as a line
     * @param b the point
     * @return <code>true</code> if the point is right of the line,
     *         <code>false</code> otherwise
     */
    public static boolean isPointRightOfLine(LineSegment a, Point b) {
        // Move the image, so that a.first is on (0|0)
        LineSegment aTmp = new LineSegment(new Point(0, 0), new Point(
                a.second.x - a.first.x, a.second.y - a.first.y));
        Point bTmp = new Point(b.x - a.first.x, b.y - a.first.y);
        return crossProduct(aTmp.second, bTmp) < 0;
    }

    /**
     * Check if line segment first touches or crosses the line that is
     * defined by line segment second.
     *
     * @param first line segment interpreted as line
     * @param second line segment
     * @return <code>true</code> if line segment first touches or
     *                           crosses line second,
     *         <code>false</code> otherwise.
     */
    public static boolean lineSegmentTouchesOrCrossesLine(LineSegment a,
            LineSegment b) {
        return isPointOnLine(a, b.first)
                || isPointOnLine(a, b.second)
                || (isPointRightOfLine(a, b.first) ^ isPointRightOfLine(a,
                        b.second));
    }

    /**
     * Check if line segments intersect
     * @param a first line segment
     * @param b second line segment
     * @return <code>true</code> if lines do intersect,
     *         <code>false</code> otherwise
     */
    public static boolean doLinesIntersect(LineSegment a, LineSegment b) {
        Point[] box1 = a.getBoundingBox();
        Point[] box2 = b.getBoundingBox();
        return doBoundingBoxesIntersect(box1, box2)
                &amp;&amp; lineSegmentTouchesOrCrossesLine(a, b)
                &amp;&amp; lineSegmentTouchesOrCrossesLine(b, a);
    }
}
{% endhighlight %}

<h2>Addendum</h2>
Some notes for me:
<ul>
  <li>Writing Tests first is worth the effort. I guess it finally saved me some time and it gives me some confidence that my code works.</li>
  <li>I should update my system. I'm still using Ubuntu 10.04.4 LTS. Especially, I have Eclipse 3.5.2. This means I could not try <a href="http://www.eclemma.org/">EclEmma</a> to test my code coverage :-(</li>
  <li>LaTeX is great. I've created all images with LaTeX and it was quite fast after I got the first one. Here is the <a href="https://github.com/MartinThoma/LaTeX-examples/tree/master/tikz/line-segments">LaTeX source</a>.</li>
</ul>

edit:
I now have a more modern system. So I was able to use EclEmma, which works fine. And I have 100% branch code coverage for this part of code :-)
