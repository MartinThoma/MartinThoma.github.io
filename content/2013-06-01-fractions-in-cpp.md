---
layout: post
title: Fractions in C++
slug: fractions-in-cpp
author: Martin Thoma
date: 2013-06-01 12:00:34.000000000 +02:00
category: Code
tags: CPP
featured_image: 2012/05/CPP-thumb.png
---
Today, I thought I should try to implement a class in C++ that deals with fractions. This is actually quite easy as I'll show you.

<h2>First some math</h2>
<h3>Names</h3>
When you have a fraction $\frac{a}{b}$ then $a$ is called <em>numerator</em> and $b$ is called <em>denominator</em>.

<h3>Operations</h3>
The rules for basic operations are simple:

Addition:
$\frac{a}{b}     + \frac{c}{d} = \frac{a \cdot d + c \cdot b}{b \cdot d}$

Subtraction:
$\frac{a}{b}     - \frac{c}{d} = \frac{a \cdot d - c \cdot b}{b \cdot d}$

Multiplication:
$\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$

Division:
$\frac{a}{b} : \frac{c}{d} = \frac{a \cdot d}{b \cdot c}$

<h3>Euklids algorithm</h3>
You can calculate the greatest common divisor with <a href="http://en.wikipedia.org/wiki/Euclidean_algorithm">Euklids algorithm</a>. If you don't know it, please read the Wikipedia article.

Knowing the greatest common divisor is important, because we want that our Faction class automatically cancels those factors so that the numerator and denominator are as small as possible.

<h2>C++ Code</h2>
```cpp

#include <iostream>

using namespace std;

class Fraction {
    private:
        // Calculates the greates common divisor with
        // Euclid's algorithm
        // both arguments have to be positive
        long long gcd(long long a, long long b) {
            while (a != b) {
                if (a > b) {
                    a -= b;
                } else {
                    b -= a;
                }
            }
            return a;
        }

    public:
        long long numerator, denominator;

        Fraction() {
            numerator = 0;
            denominator = 1;
        }

        Fraction(long long n, long long d) {
            if (d==0) {
                cerr << "Denominator may not be 0." << endl;
                exit(0);
            } else if (n == 0) {
                numerator = 0;
                denominator = 1;
            } else {
                int sign = 1;
                if (n < 0) {
                    sign *= -1;
                    n *= -1;
                }
                if (d < 0) {
                    sign *= -1;
                    d *= -1;
                }

                long long tmp = gcd(n, d);
                numerator = n/tmp*sign;
                denominator = d/tmp;
            }
        }

        operator int() {return (numerator)/denominator;}
        operator float() {return ((float)numerator)/denominator;}
        operator double() {return ((double)numerator)/denominator;}
};

Fraction operator+(const Fraction& lhs, const Fraction& rhs) {
    Fraction tmp(lhs.numerator*rhs.denominator
                +rhs.numerator*lhs.denominator,
                lhs.denominator*rhs.denominator);
    return tmp;
}

Fraction operator+=(Fraction& lhs, const Fraction& rhs) {
    Fraction tmp(lhs.numerator*rhs.denominator
                +rhs.numerator*lhs.denominator,
                lhs.denominator*rhs.denominator);
    lhs = tmp;
    return lhs;
}

Fraction operator-(const Fraction& lhs, const Fraction& rhs) {
    Fraction tmp(lhs.numerator*rhs.denominator
                -rhs.numerator*lhs.denominator,
                lhs.denominator*rhs.denominator);
    return tmp;
}

Fraction operator-=(Fraction& lhs, const Fraction& rhs) {
    Fraction tmp(lhs.numerator*rhs.denominator
                -rhs.numerator*lhs.denominator,
                lhs.denominator*rhs.denominator);
    lhs = tmp;
    return lhs;
}

Fraction operator*(const Fraction& lhs, const Fraction& rhs) {
    Fraction tmp(lhs.numerator*rhs.numerator,
               lhs.denominator*rhs.denominator);
    return tmp;
}

Fraction operator*=(Fraction& lhs, const Fraction& rhs) {
    Fraction tmp(lhs.numerator*rhs.numerator,
               lhs.denominator*rhs.denominator);
    lhs = tmp;
    return lhs;
}

Fraction operator*(int lhs, const Fraction& rhs) {
    Fraction tmp(lhs*rhs.numerator,rhs.denominator);
    return tmp;
}

Fraction operator*(const Fraction& rhs, int lhs) {
    Fraction tmp(lhs*rhs.numerator,rhs.denominator);
    return tmp;
}

Fraction operator/(const Fraction& lhs, const Fraction& rhs) {
    Fraction tmp(lhs.numerator*rhs.denominator,
                 lhs.denominator*rhs.numerator);
    return tmp;
}

std::ostream& operator<<(std::ostream &strm, const Fraction &a) {
    if (a.denominator == 1) {
        strm << a.numerator;
    } else {
        strm << a.numerator << "/" << a.denominator;
    }
    return strm;
}

int main() {
    Fraction a(1,3);
    Fraction b(3,28);
    Fraction c;

    c = a + b;
    cout << c << "\t(should be 37/84)" << endl;

    c = a - b;
    cout << c << "\t(should be 19/84)" << endl;

    c = a * b;
    cout << c << "\t(should be 1/28)" << endl;

    c = a / b;
    cout << c << "\t(should be 28/9)" << endl;

    c = -1 * b;
    cout << c << "\t(should be -3/28)" << endl;

    c = b * (-1);
    cout << c << "\t(should be -3/28)" << endl;

    c = Fraction(-100,3);
    cout <<    (int)c << "\t(should be -33)" << endl;
    cout <<  (float)c << "\t(should be -33.3...)" << endl;
    cout << (double)c << "\t(should be -33.3...)" << endl;

    a -= b;
    cout << a << "\t(should be 19/84)" << endl;

    return 0;
}

```

<h2>See also</h2>
You might also be interested in my article about <a href="../cpp-operator-overloading/" title="C++ Operator overloading">operator overloading</a>.

Does anybody know if there is an "official" Fraction class?
