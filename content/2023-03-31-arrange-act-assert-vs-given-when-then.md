---
layout: post
title: Arrange-Act-Assert vs Given-When-Then
slug: arrange-act-assert-vs-given-when-then
lang: en
author: Martin Thoma
date: 2023-03-31 18:59
category: Code
tags: Testing, Unit Testing, Python
featured_image: logos/python.png
summary: Or: How to structure your tests
medium_url: https://medium.com/@martinthoma/arrange-act-assert-vs-given-when-then-c22da421bf75
---
Unit tests typically consist of three meaningful phases:

* **Arrange**: Set up the preconditions for the tests. That could be creating data/objects or configuring a state.
* **Act**: Perform the action that should get tested. Typically this means calling the function/method you want to test.
* **Assert**: Verify the correctness of the outcome. Typically this means comparing the actual return value with the expected return value, but it could also mean to check Exceptions or log messages.

If you make it explicit, you can call this the AAA pattern. But there are a few other names of patterns you might have seen.

Code using that pattern with pytest (Python) looks like this:

```python
def test_foo():
    # Arrange
    bar = generate_bar()
    baz = generate_baz()

    # Act
    actual_result = foo(bar, baz)

    # Assert
    expected_result = "abc"
    assert actual_result == expected_result
```

Please note: If you need to do the same things again and again in the “arrange” step, you can write [pytest fixtures](https://docs.pytest.org/en/6.2.x/fixture.html).

## The Four-phase test pattern

The four-phase pattern is what you might know from JUnit in Java and unittest in Python.

* **Setup**: Prepare the preconditions for the test
* **Exercise**: Call the function/method that is tested
* **Verify**: Compare the actual output with the expected output
* **Teardown**: Clean up

You typically have a class that has the setup / teardown methods as well as a `test_xyz` method containing both, exercise and verify.

Note that this is almost the same as Arrange-Act-Assert. Only the “teardown” is missing in AAA.

```python
import unittest


class FooTest(unittest.TestCase):
    def setUp(self):
        # Executed before each test_* method
        self.bar = generate_bar()
        self.baz = generate_baz()

    def tearDown(self):
        # Executed after each test_* method
        self.bar = None
        self.baz = None

    def test_foo(self):
        # Act
        actual_result = foo(self.bar, self.baz)

        # Assert
        expected_result = "abc"
        self.assertEqual(actual_result, expected_result)
```

## Given-When-Then (GWT) in comparison to AAA

In behavior-driven development (BDD) people like to use GWT:

* **Given**: Similar to Arrange
* **When**: Similar to Act
* **Then**: Similar to Assert

GWT describes a scenario from the user’s point of view, while AAA describes the structure of the test code. However, they are essentially the same.
