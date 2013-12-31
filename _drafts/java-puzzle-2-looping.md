---
layout: post
title: Java Puzzle #2: Looping
author: Martin Thoma
date: 2012-07-11 12:50:51
categories: 
- Code
tags: 
- Java
featured_image: 2012/07/java-thumb.png
---
What does the following Code output:

[java]import java.math.BigInteger;
import java.util.LinkedList;
import java.util.List;

public class test {
    public static int looping() {
        int result = 0;
        for (int a = 0; a &lt; 10; a++) {
            for (int b = 0; b &lt; 10; b++) {
                for (int c = 0; c &lt; 10; c++) {
                    for (int d = 0; d &lt; 10; d++) {
                        for (int e = 0; e &lt; 10; e++) {
                            for (int f = 0; f &lt; 10; f++) {
                                for (int g = 0; g &lt; 10; g++) {
                                    for (int h = 0; h &lt; 10; h++) {
                                        for (int i = 0; i &lt; 10; i++) {
                                            for (int j = 0; j &lt; 10; j++) {
                                                for (int k = 0; k &lt; 10; j++) {
                                                    for (int l = 0; l &lt; 10; k++) {
                                                        for (int m = 0; m &lt; 10; l++) {
                                                            result++;
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(&quot;Result of looping: &quot; + looping());
    }
}[/java]













As you might have expected: 