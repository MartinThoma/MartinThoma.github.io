---
layout: post
status: publish
published: true
title: How to check if a point is inside a rectangle
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 43601
wordpress_url: http://martin-thoma.com/?p=43601
date: 2012-09-07 21:28:38.000000000 +02:00
categories:
- Code
tags:
- Python
- Geometry
comments:
- id: 1237291
  author: Jan
  author_email: jan9000@trashmail.de
  author_url: ''
  date: !binary |-
    MjAxMy0wOC0xMSAxNDowOTowOSArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wOC0xMSAxMjowOTowOSArMDIwMA==
  content: ! "Thanks for sharing your code, but I think it does not work. Examples:\r\n\r\n>>>
    isPinRectangle([[0,0], [10,0], [10,10], [0,10]], [5,5])\r\nFalse\r\n>>> isPinRectangle([[0,0],
    [10,0], [10,10], [0,10]], [11, 11])\r\nFalse\r\n\r\nIt cannot work since you do
    not consider the point P in your area calculation of the triangles. Here is a
    working implementation of the link you have posted:\r\n\r\nimport numpy as np\r\n\r\ndef
    areaTri(A, B, C):\r\n    #Heron's formula\r\n    a = np.linalg.norm((B-C))\r\n
    \   b = np.linalg.norm((C-A))\r\n    c = np.linalg.norm((A-B))\r\n    s = (a +
    b + c) / 2.0\r\n    return np.sqrt(s * (s-a) * (s-b) * (s-c))\r\n\r\n\r\ndef
    isPinRect(D, w, h, P):\r\n    #D is a list containing the x,y coordinate of the
    lower left corner of the rectangle\r\n    #w, h are the width and height of the
    rectangle\r\n    #P is a list containing the x,y coordinate of the point\r\n    A
    = np.array([D[0], D[1] + h])\r\n    B = np.array([D[0] + w, D[1] + h])\r\n    C
    = np.array([D[0] + w, D[1]])\r\n    D = np.array(D)\r\n    P = np.array(P)\r\n
    \   \r\n    areaRectangle = np.linalg.norm((A-B)) * np.linalg.norm((A-D))\r\n
    \   areaTriangles = areaTri(A, P, D) + areaTri(D, P, C) + areaTri(C, P, B) + areaTri(P,
    B, A)\r\n    \r\n    return (np.abs(areaRectangle - areaTriangles) >> isPinRect([0,0],
    10, 10, [5, 5])\r\nTrue\r\n>>> isPinRect([0,0], 10, 10, [11, 11])\r\nFalse\r\n\r\n\r\ncheers,\r\njan"
featured_image: 2012/09/rectangle-thumb.png
---
[caption id="attachment_43611" align="aligncenter" width="512"]<a href="http://martin-thoma.com/wp-content/uploads/2012/09/rectangle.png"><img class="size-full wp-image-43611 " title="A rectangle" src="http://martin-thoma.com/wp-content/uploads/2012/09/rectangle.png" alt="A rectangle" width="512" height="409" /></a> A rectangle[/caption]

I've just found this interesting question on <a href="http://math.stackexchange.com/q/190111/6876">StackExchange</a>:

If you have a rectangle ABCD and point P. Is P inside ABCD?

<h2>The idea</h2>
The idea how to solve this problem is simply beautiful. 

If the point is in the rectangle, it divides it into four rectangles:

[caption id="attachment_43651" align="aligncenter" width="512"]<a href="http://martin-thoma.com/wp-content/uploads/2012/09/rectangle-2.png"><img class="size-full wp-image-43651 " title="Divided rectangle" src="http://martin-thoma.com/wp-content/uploads/2012/09/rectangle-2.png" alt="Divided rectangle" width="512" height="409" /></a> Divided rectangle[/caption]

If P is not inside of ABCD, you end up with somethink like this:

[caption id="attachment_43661" align="aligncenter" width="512"]<a href="http://martin-thoma.com/wp-content/uploads/2012/09/rectangle-3.png"><img class="size-full wp-image-43661 " title="Point is outside of rectangle " src="http://martin-thoma.com/wp-content/uploads/2012/09/rectangle-3.png" alt="Point is outside of rectangle " width="512" height="409" /></a> Point is outside of rectangle[/caption]

You might note that the area of the four triangles in is bigger than the area of the rectangle. So if the area is bigger, you know that the point is outside of the rectangle.

<h2>Formulae</h2>
If you know the coordinates of the points, you can calculate the area of the rectangle like this:

$A_\text{rectangle} = \frac{1}{2} \left| (y_{A}-y_{C})\cdot(x_{D}-x_{B}) + (y_{B}-y_{D})\cdot(x_{A}-x_{C})\right|$

The area of a triangle is:
$A_\text{triangle} = \frac{1}{2} (x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2))$

<h2>Python</h2>
<div class="important">Please look at Jans comment. There is an error in my Python code, but I don't have the time to correct it.</div>

{% highlight python %}def isPinRectangle(r, P):
    """ 
        r: A list of four points, each has a x- and a y- coordinate
        P: A point
    """

    areaRectangle = 0.5*abs(
        #                 y_A      y_C      x_D      x_B          
                        (r[0][1]-r[2][1])*(r[3][0]-r[1][0]) 
        #                  y_B     y_D       x_A     x_C
                      + (r[1][1]-r[3][1])*(r[0][0]-r[2][0])
                    )

    ABP = 0.5*(
             r[0][0]*(r[1][1]-r[2][1])
            +r[1][0]*(r[2][1]-r[0][1])
            +r[2][0]*(r[0][1]-r[1][1])
          )
    BCP = 0.5*(
             r[1][0]*(r[2][1]-r[3][1])
            +r[2][0]*(r[3][1]-r[1][1])
            +r[3][0]*(r[1][1]-r[2][1])
          )
    CDP = 0.5*(
             r[2][0]*(r[3][1]-r[0][1])
            +r[3][0]*(r[0][1]-r[2][1])
            +r[0][0]*(r[2][1]-r[3][1])
          )
    DAP = 0.5*(
             r[3][0]*(r[0][1]-r[1][1])
            +r[0][0]*(r[1][1]-r[3][1])
            +r[1][0]*(r[3][1]-r[0][1])
          )
    return areaRectangle == (ABP+BCP+CDP+DAP){% endhighlight %}

<h2>Triangle</h2>
The same idea can easily be adopted to triangles:

{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Point:
    """Represents a two dimensional point."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __get__(self, obj, cls=None):
        return obj

    def __repr__(self):
        return "P(%.2lf|%.2lf)" % (self.x, self.y)

    def __str__(self):
        return repr(self)

class Triangle:
    """Represents a triangle in R^2."""

    epsilon = 0.001

    def __init__(self, a, b, c):
        assert isinstance(a, Point)
        assert isinstance(b, Point)
        assert isinstance(c, Point)
        self.a = a
        self.b = b
        self.c = c
        
    def getArea(self):
        """Get area of this triangle.
           >>> Triangle(Point(0.,0.), Point(10.,0.), Point(10.,10.)).getArea()
           50.0
           >>> Triangle(Point(-10.,0.), Point(10.,0.), Point(10.,10.)).getArea()
           100.0
        """
        a, b, c = self.a, self.b, self.c
        return abs(a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y))/2

    def isInside(self, p):
        """Check if p is inside this triangle."""
        assert isinstance(p, Point)
        currentArea = self.getArea()
        pab = Triangle(p,self.a, self.b)
        pac = Triangle(p,self.a, self.c)
        pbc = Triangle(p,self.b, self.c)
        newArea = pab.getArea()+pac.getArea()+pbc.getArea()
        return (abs(currentArea - newArea) < Triangle.epsilon)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
{% endhighlight %}
