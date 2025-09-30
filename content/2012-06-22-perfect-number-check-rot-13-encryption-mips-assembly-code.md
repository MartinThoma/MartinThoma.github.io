---
layout: post
lang: en
title: Perfect number check and ROT-13 encryption in MIPS-assembly code
slug: perfect-number-check-rot-13-encryption-mips-assembly-code
author: Martin Thoma
date: 2012-06-22 10:43:49.000000000 +02:00
category: Code
tags: Assembly language, MIPS
featured_image: 2012/06/MIPS-Ingenic_JZ4730.jpg
---
<h2>Perfect number check</h2>
The perfect number check in MIPS is quite easy to realize. Here is some pythonic Pseudocode

```python
n = input()  # read a positive integer n from the user
sumOfDivisors = 0
for i in range(1, n):  # go from 1 to n-1
    if n % i == 0:  # if i is a divisor
        sumOfDivisors += i

if sumOfDivisors == n:
    print("1")
else:
    print("0")
```

And here is the MIPS-Code:
```text
#####################################################################
# Perfect number check												#
# @param int the number you would like to check						#
# @result int 0 if the number is not perfect, otherwise 1			#
#####################################################################

.data
	prompt: .asciiz "Positive integer you would like to check : "
	output: .asciiz "Is a perfect number (1: Yes, 0: No): "
.text
.globl main
main: li $v0 , 4		# |
	la $a0 , prompt		# |
	syscall				# |=> Print string "prompt"
	li $v0 , 5			# |
	syscall				# |=> Ask for integer A

	# Initialise variables
	move $s0 , $v0		# => Store A in $s0
	li $s1 , 0			# => The sum of all proper divisors of A
	li $s2 , 1			# => start here with checks for devisors

s:	bgeu $s2, $s0, eval # while $s2 < $s0
	rem $t0, $s0, $s2	# $t0 = $s0 % $s2
	bne $t0, $0, w
	addu $s1, $s1, $s2	# $s1 += $s2
w:	addi $s2, $s2, 1	# $s2++
	j s;				# /endwhile

eval: seq $s0, $s0, $s1	# Compare the sum of divisors with A
	li $v0 , 4			# |
	la $a0 , output		# |
	syscall				# |=> Print string "output"
	la $v0 , 1			# |
	move $a0 , $s0		# |
	syscall				# |=> Print $s0
	jr $ra
```

<h2>ROT-13 encryption</h2>

The basic idea for encrypting a string with ROT-13 is to loop over all characters and use the ASCII-Table to shift them. Here is the ROT-13 MIPS-Code:
```text
#####################################################################
# @param string a &#92;&#48; terminated string								#
# @return string the ROT-13 encrypted string						#
#####################################################################

.data
	prompt: .asciiz "Please enter string: "
	output: .asciiz "ROT-13: "
	plain:  .space 64
.text
.globl main
main:
	li 		$v0, 4		# |
	la 		$a0, prompt	# |
	syscall				# |=> Print string "prompt"
    li      $v0, 8		# |
    la      $a0, plain	# | => Ask for string plain
    li      $a1, 64		# |
    syscall				# | => read a string with max. 64 chars
	li		$t2, 10		# Stop by \n

	# Loop over all characters
	la		$t1, ($a0)	#=>$t1:the current adress that gets modified

s:	lb 		$t0, ($t1)  # => $t0: the current value (char)
	beq $t0, $t2, out  	# while $t1 != '\n'
	li $t3, 64
	bge $t3, $t0, w		# if $t0 <= 64: jump to w
	li $t3, 123
	bge $t0, $t3, w		# if $t0 >= 123: jump to w
	li $t3, 90
	bge $t3, $t0, big	# if $t0 <= 90: jump to big
	li $t3, 96
	bge $t3, $t0, w		# if $t0 <= 96: jump to w
	j small
w:	addi $t1, $t1, 1	# $t1++
	j s;				# /endwhile

small:
	addi	$t0, -84 	# -97 + 13
	rem 	$t0, $t0, 26 # $t0 %= 26
	addi	$t0, 97
	sb		$t0, ($t1)
	j w

big:
	addi	$t0, -52 	# -65 + 13
	rem 	$t0, $t0, 26 # $t0 %= 26
	addi	$t0, 65
	sb		$t0, ($t1)
	j w

out:
	li 		$v0, 4		# |
	la 		$a0, output	# |
	syscall				# |=> Print string "output"

	la 		$v0, 4		# |
	la 		$a0, plain	# |
	syscall				# |=> Print plain
    jr      $ra
```

A syntax-highlighted version of both code pieces is here: <a href='../images/2012/06/mips-rot-13-perfect-number.pdf'>MIPS Assembly Code for a perfect number check and ROT-13 encryption</a>.

<h2>See also</h2>
<ul>
  <li><a href="https://sourceforge.net/projects/spimsimulator/files/">SPIM MIPS Simulator</a></li>
  <li><a href="../how-print-mips-assembly-code-latex/" title="How to print MIPS assembly code in LaTeX">How to print MIPS assembly code in LaTeX</a></li>
  <li><a href="../add-mips-syntax-highlighting-gedit/" title="Add MIPS syntax highlighting to gEdit">Add MIPS syntax highlighting to gEdit</a></li>
  <li><a href='../images/2012/06/mips-archive.zip'>Archive with MIPS assembly Code and LaTeX file</a></li>
</ul>
