---
layout: post
title: How to check if two line segments intersect
author: Martin Thoma
date: 2013-02-21 12:19:05.000000000 +01:00
category: Code
tags: Java, algorithms, Geometry
---
You have to line segments and you want to know if they intersect. I'll give you an algorithm how to do it.

<h2>Test cases</h2>
First of all, we should think about how lines can be arranged:

<ul class="gallery mw-gallery-traditional" style="max-width: 652px; width: 652px;">
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-t1.png" class="image">
                  <img src="../images/2013/02/line-segments-t1.png" alt="T1: One line is horizontal, one vertical and they cross" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase T1</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-t2.png" class="image">
                  <img src="../images/2013/02/line-segments-t2.png" alt="T2: An endpoint of one line segment is on the other line segment" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase T2</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-t3.png" class="image">
                  <img src="../images/2013/02/line-segments-t3.png" alt="T3: Similar to T4, but with negative coordiantes" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase T3</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-t4.png" class="image">
                  <img src="../images/2013/02/line-segments-t4.png" alt="T4: One line is horizontal, one vertical and an end point is on one line" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase T4</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-t5.png" class="image">
                  <img src="../images/2013/02/line-segments-t5.png" alt="T5: One line is on the other line" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase T5</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-t6.png" class="image">
                  <img src="../images/2013/02/line-segments-t6.png" alt="T6: Line segements are identical" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase T6</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-f1.png" class="image">
                  <img src="../images/2013/02/line-segments-f1.png" alt="F1: In parallel, close together, one line is completely inside the bounding box of the other line" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase F1</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-f2.png" class="image">
                  <img src="../images/2013/02/line-segments-f2.png" alt="F2: Both lines are parallel." style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase F2</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-f3.png" class="image">
                  <img src="../images/2013/02/line-segments-f3.png" alt="F3: Both lines are horizontal." style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase F3</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-f4.png" class="image">
                  <img src="../images/2013/02/line-segments-f4.png" alt="F4: One line is horizontal, one vertical. They don't cross." style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase F4</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-f5.png" class="image">
                  <img src="../images/2013/02/line-segments-f5.png" alt="F5: Both line segments are on one line, but they don't intersect" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase F5</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-f6.png" class="image">
                  <img src="../images/2013/02/line-segments-f6.png" alt="F6: Both line segments are close together" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase F6</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-f7.png" class="image">
                  <img src="../images/2013/02/line-segments-f7.png" alt="F7: Both lines are horizontal" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase F7</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/02/line-segments-f8.png" class="image">
                  <img src="../images/2013/02/line-segments-f8.png" alt="F8: Like F6" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">Testcase F8</div>
      </div>
   </li>
</ul>

<h2>Bounding boxes</h2>
You can draw boxes around line segments such that the edges of the boxes are in parallel to the coordinate axes:

<figure class="aligncenter">
            <a href="../images/2013/02/line-segments-bounding-box-250x300.png"><img src="../images/2013/02/line-segments-bounding-box-250x300.png" alt="Two line segments with their bounding boxes" caption="Two line segments with their bounding boxes" style="max-width:250px;max-height:300px" class="size-medium wp-image-57731"/></a>
            <figcaption class="text-center">Two line segments with their bounding boxes</figcaption>
        </figure>

With this image in mind, it is obvious that the bounding boxes need to intersect if the lines should intersect. At this point you have to make a decision: If the endpoint of one line is on the other line, is this an intersection? I think so. If two lines have at least one point in common, they intersect. If two bounding boxes have at least one point in common, they intersect.

It is much easier to check if two bounding boxes intersect. It's simply:

```java
/**
 * Check if bounding boxes do intersect. If one bounding box
 * touches the other, they do intersect.
 * @param a first bounding box
 * @param b second bounding box
 * @return <code>true</code> if they intersect,
 *         <code>false</code> otherwise.
 */
public boolean doBoundingBoxesIntersect(Point[] a, Point[] b) {
    return a[0].x <= b[1].x
        && a[1].x >= b[0].x
        && a[0].y <= b[1].y
        && a[1].y >= b[0].y;
}
```

If you have difficulties to understand why this works, take a look at this great <a href="http://silentmatt.com/rectangle-intersection/">animation for this formula</a>.

<h2>The algorithm</h2>
<figure class="aligncenter">
            <a href="../images/2013/02/flowchart.png"><img src="../images/2013/02/flowchart.png" alt="Flowchart how to check if two lines intersect" style="max-width:500px;max-height:228px" class="size-full wp-image-57771"/></a>
            <figcaption class="text-center">Flowchart how to check if two lines intersect</figcaption>
        </figure>

Looks quite simple, doesn't it?

<h3>Cross product</h3>
Well, you might notice that you need to check if one line intersects with a given line segment. To check this, you have to understand one cool idea:

You can definie a cross product for points:

\begin{align}
  \times_P&: Point \times Point \rightarrow \mathbb{R}\\
  \times_P(a, b) &:= a.x \cdot b.y - b.x \cdot a.y;
\end{align}

This cross product has one nice characteristics:

$a \times_P b = 0 \Leftrightarrow a$ and $b$ are on one line through origin

You can verify this. If you take two points on a line through origin, they have the same slope $\frac{\Delta y}{\Delta x}$:

$$
\begin{align}
  0 &= a \times_P b\\
\Leftrightarrow 0 &= a.x \cdot b.y - b.x \cdot a.y\\
\Leftrightarrow b.x \cdot a.y &= a.x \cdot b.y\\
\Leftrightarrow \frac{a.y}{a.x} &= \frac{b.y}{b.x}
\end{align}
$$

Ok, now you can check if a point is on a line:

```java
/**
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
}
```

The second cool characteristic of the cross product is that it can be used to determine if a point b is left or right of the line through the origin and a point a:

```java
/**
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
}
```

When we have one line $a$ through the origin and one line segment $b$, you can check if $b$ crosses $a$ by checking if the end points of $b$ are on different sides of $a$:

```java
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
public boolean lineSegmentTouchesOrCrossesLine(LineSegment a,
        LineSegment b) {
    return isPointOnLine(a, b.first)
            || isPointOnLine(a, b.second)
            || (isPointRightOfLine(a, b.first) ^
                isPointRightOfLine(a, b.second));
}
```

Now you have everything you need:

```java
/**
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
            && lineSegmentTouchesOrCrossesLine(a, b)
            && lineSegmentTouchesOrCrossesLine(b, a);
}
```

By the way, testcase F5 is the only reason why you need <code>doBoundingBoxesIntersect(box1, box2)</code>. All other tests still pass if you remove this function.

<h2>Where do two line segments intersect?</h2>
When you know that two line segments intersect, you can also calculate the intersection.
The intersection could be a line or only a point.

I did this with JavaScript:

<iframe src="../html5/line-segment-intersection/" width="800" height="600">
  <p>Ihr Browser kann leider keine eingebetteten Frames anzeigen. Die Seite ist <a href="../html5/line-segment-intersection/">hier</a>.</p>
</iframe>

This is the code that checks for line segments:

```javascript
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
```

<h2>TL;DR</h2>
The complete, tested code is on <a href="https://github.com/MartinThoma/algorithms/tree/master/crossingLineCheck/Geometry/src">GitHub</a>. Here is the most important part:

```java
public class Geometry {

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
        return a[0].x <= b[1].x && a[1].x >= b[0].x && a[0].y <= b[1].y
                && a[1].y >= b[0].y;
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
                && lineSegmentTouchesOrCrossesLine(a, b)
                && lineSegmentTouchesOrCrossesLine(b, a);
    }
}

```

<h2>Addendum</h2>
Some notes for me:
<ul>
  <li>Writing Tests first is worth the effort. I guess it finally saved me some time and it gives me some confidence that my code works.</li>
  <li>I should update my system. I'm still using Ubuntu 10.04.4 LTS. Especially, I have Eclipse 3.5.2. This means I could not try <a href="http://www.eclemma.org/">EclEmma</a> to test my code coverage ☹</li>
  <li>LaTeX is great. I've created all images with LaTeX and it was quite fast after I got the first one. Here is the <a href="https://github.com/MartinThoma/LaTeX-examples/tree/master/tikz/line-segments">LaTeX source</a>.</li>
</ul>

edit:
I now have a more modern system. So I was able to use EclEmma, which works fine. And I have 100% branch code coverage for this part of code ☺


## See also

* `mpu.geometry`: [source](https://github.com/MartinThoma/mpu/blob/master/mpu/geometry.py)
