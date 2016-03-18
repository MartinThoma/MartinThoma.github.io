---
layout: post
title: Polyglots - Crazy Programming Stuff
author: Martin Thoma
date: 2011-09-21 19:28:02.000000000 +02:00
categories:
- Code
tags:
- Brainfuck
- Esoteric programming language
- Programming
- Whitespace
- Python
---
Have you ever heard of polyglots? This is so crazy. A <a href="http://en.wikipedia.org/wiki/Polyglot_(computing)">polyglot</a> is a program which can be interpreted as many programming languages. You don't believe me that something crazy like that is possible? Here is an example I've made:     
          
        
          
        
          
         
          
         
         
         
         
         
          
          
          
          
          
          
          
          
          
          
         
          
          
          
          
          
         
           
          
           
          
           
          
           
          
           
          
           
          
           
         
           
    
       

                                          

                                                          




                          
    
 

                                          
 
     
 
                                                                          
 
      
    
 
                                        

                                                                          
 

 


 

                                  
 
  
  
      
        
    
                                                                  
 

    
    
 
                                

                                                                  
 

    
        
   
 

                                                          
       
       
 
   
  
{% highlight python %} 
#>++++++++++[
# Python code written by Martin Thoma
#>++++++++


#>++++++++++
# Looping
#>+++++++++++
def looping(i):
    """>++++++++++++ Do some crazy stuff x Written by Martin Thoma """
    answer = ""
    while i % 13 != 0:
        if i > 0:
            i += i + i + i
        elif i > 5:
            i += i + i + i + i + i + i + i 
        elif i > 10:
            i += i + i + i + i + i + i + i + i + i + i + i 
        elif i > 15:
            i += i + i + i + i + i + i + i + i + i + i
        if i > 96:
            """+++++++++++"""
            if i > 122:
                i %= 26
                i += 96
            answer = answer+chr(i)

    """+++++++++>++++++++++>++++++++++++>++++++++++>++++++++++"""
    """+>+++>++++++++++>+++++++++++>++++++++++>++++++++++>+++>++++++++++++>++"""
    """++++++++>++++++++++++>+++>++++++++++++>+++++++++++>+++++++++++>+++++++"""
    """+++++>++++++++++++>++++++++++>+++++++++++>+++>++++++++++>++++++++++++>"""
    """+++>++++++++>++++++++++>+++++++++++>++++++++++++>+++++++++++>+++++++++"""
    """++>+++>++++++++>++++++++++>+++++++++++>+++++++++++>++++++++++>+++++>++"""
    """+>+++++++>+++++++++++>++++++++++>++++++++++++>++++++++++++>++++>+++>++"""
    """++++++++>++++++++++++>++++++++++>++++++><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
    """<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-]>++++>++++>----->----->++>---->++++>-"""
    """-->----->>++>--->->--->++>->+>>+>++>->--->----->++>->++++>----->---->-"""
    """--->+>>++>-->+>++>--->--->++++>---->----->>++>++++>++++>+>->--->---->+"""
    """+>--->++++>--->++>+>++++>++>++++>--->++++>+++><<<<<<<<<<<<<<<<<<<<<<<<"""
    """<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>"""
    """.>.>. >.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>."""
    """>.>.>.>.>.>.>.>.>."""
    return answer

print looping(1)
print("You've just executed some Python-Code written by Martin Thoma")
{% endhighlight %} 
You can download the file at <a href="../python/polyglot.py">martin-thoma.com/python/polyglot.py</a>.

I used three languages in this piece of code: <a href="http://en.wikipedia.org/wiki/Python_(programming_language)">Python</a>, <a href="http://en.wikipedia.org/wiki/Brainfuck">Brainfuck</a> and <a href="http://en.wikipedia.org/wiki/Whitespace_(programming_language)">Whitespace</a>. You can try it with <a href="http://ideone.com/">ideone.com</a>. But please, copy the whole code!

It might be considered as cheating to use comments as often as I did and using two esoteric programming languages. Whitespace works only with whitespaces (space, tab) and Brainfuck needs only +-.;<>[]. Everything else is interpreted as a comment.

When I have much more freetime and I don't know what to do, I'll probably write some code with a more interesting output and which is not that obvious.
