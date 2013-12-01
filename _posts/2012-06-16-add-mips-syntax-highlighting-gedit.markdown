---
layout: post
status: publish
published: true
title: Add MIPS syntax highlighting to gEdit
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 26901
wordpress_url: http://martin-thoma.com/?p=26901
date: 2012-06-16 10:27:09.000000000 +02:00
categories:
- Code
tags:
- Assembly language
- MIPS
comments: []
---
I have to code some little programs in MIPS assembly language for university. So I liked to have some syntax highlighting for my favorite editor: gEdit.

The following steps were tested on Ubuntu 10.04.4 LTS.

This adds MIPS syntax highlighting to gEdit and every editor, that uses gtksourceview.

Create the following file: <code>/usr/share/gtksourceview-2.0/language-specs/sal.lang</code>


Source: GITHub: <a href="https://github.com/Xodarap/Mips-Assembly-Syntax-Highlighting">Xodarap / Mips-Assembly-Syntax-Highlighting</a>

Copy and paste the following:
[xml]<?xml version="1.0" encoding="UTF-8"?>
<!--

 Author: Ben West
 Copyright (C) 2010 Ben West
 edited by Martin Thoma

 This library is free software; you can redistribute it and/or
 modify it under the terms of the GNU Library General Public
 License as published by the Free Software Foundation; either
 version 2 of the License, or (at your option) any later version.

 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 Library General Public License for more details.

 You should have received a copy of the GNU Library General Public
 License along with this library; if not, write to the
 Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 Boston, MA 02111-1307, USA.

-->
<!--
	Somewhat copied and pasted from nasm.lang
-->
<language id="mal" _name="MAL" version="2.0" _section="Others">
    <metadata>
      <property name="mimetypes">text/mal</property>
      <property name="globs">*.s</property>
      <property name="line-comment-start">#</property>
    </metadata>

    <styles>
        <style id="comment"           	_name="Comment"             	map-to="def:comment"/>
        <style id="error"             	_name="Error"               	map-to="def:error"/>
        <style id="string"            	_name="String"              	map-to="def:string"/>
        <style id="preprocessor"      	_name="Preprocessor"        	map-to="def:preprocessor"/>
        <style id="opcode"            	_name="Opcode"              	map-to="def:keyword"/>
        <style id="register"          	_name="Register"            	map-to="def:special-char"/>
        <style id="type"              	_name="Data Type"           	map-to="def:type"/>
        <style id="escaped-character" 	_name="Escaped Character"   	map-to="def:special-char"/>
        <style id="decimal"           	_name="Decimal number"  	map-to="def:decimal"/>
    	<style id="hexadecimal" 	_name="Hexadecimal number" 	map-to="def:base-n-integer"/>
	<style id="label"		_name="Label"			map-to="def:identifier" />
    </styles>
    
    <default-regex-options case-sensitive="false"/>

    <definitions>
        <define-regex id="escaped-character" extended="true">
            \\(      # leading backslash
            [\\\"\'] # escaped character
            )
        </define-regex>

        <context id="mal">
            <include>	
		<context id="preprocessor" style-ref="preprocessor">
			<prefix>^\.</prefix>
			<keyword>data</keyword>
			<keyword>text</keyword>
		</context>

                <context id="comment" style-ref="comment" end-at-line-end="true">
                    <start>#</start>
                    <include>
                      <context ref="def:in-line-comment"/>
                    </include>
                </context>

                <context id="string" style-ref="string" end-at-line-end="true">
                    <start>"</start>
                    <end>"</end>
                    <include>
                        <context id="escaped-characterw" style-ref="escaped-character">
                            <match>\%{escaped-character}</match>
                        </context>
                    </include>
                </context>
                <context id="string2" style-ref="string" end-at-line-end="true">
                    <start>'</start>
                    <end>'</end>
                    <include>
                        <context id="escaped-characters" style-ref="escaped-character">
                            <match>\%{escaped-character}</match>
                        </context>
                    </include>
                </context>


	        <context id="hexadecimal-number" style-ref="hexadecimal">
	      	    <match extended="true">
			(?&amp;lt;![\w\.])
			[+-]?0x[0-9a-fA-F]+
			(?![\w\.])
	      	    </match>
	        </context>

                <context id="decimal" style-ref="decimal">
                    <match extended="true">
                        (?&amp;lt;![\w\.])
                        [0-9]+
                        (?![\w\.])
                    </match>
                </context>

                <context id="registers" style-ref="register">			
			<match extended="true">
				(\$
					(
						\d|[12]\d|3[12]|
						(ra)|
						([vk][01])|
						(a[0-3t])|
						(t[0-9])|
						(s[0-7p])|
						([gsf]p)|
						(zero)
					)
				)\b
			</match>			
                </context>

		<context id="label" style-ref="label">
			<match extended="true">
				^\w+:
			</match>
		</context>

                <!-- Opcodes -->
		<context id="opcodes_simple" style-ref="opcode">
			<!-- MAL Opcodes -->
			<keyword>la</keyword>
			<keyword>li</keyword>
			<keyword>lw</keyword>
			<keyword>lb</keyword>
			<keyword>lbu</keyword>
			<keyword>sw</keyword>
			<keyword>sb</keyword>
			<keyword>add(\.s)?</keyword>
			<keyword>sub(\.s)?</keyword>
			<keyword>mul(\.s)?</keyword>
			<keyword>div(\.s)?</keyword>
			<keyword>rem</keyword>
			<keyword>and</keyword>
			<keyword>or</keyword>
			<keyword>xor</keyword>
			<keyword>nor</keyword>
			<keyword>not</keyword>
			<keyword>move</keyword>
			<keyword>sll</keyword>
			<keyword>srl</keyword>
			<keyword>sra</keyword>
			<keyword>l\.s</keyword>
			<keyword>s\.s</keyword>
			<keyword>mov\.s</keyword>
			<keyword>cvt\.s\.w</keyword>
			<keyword>cvt\.w\.s</keyword>
			<keyword>mfc0</keyword>
			<keyword>mtc0</keyword>
			<keyword>mfc1</keyword>
			<keyword>mtc1</keyword>
			<keyword>b</keyword>
			<keyword>beq</keyword>
			<keyword>bne</keyword>
			<keyword>blt</keyword>
			<keyword>bgt</keyword>
			<keyword>ble</keyword>
			<keyword>bge</keyword>
			<keyword>bltz</keyword>
			<keyword>bgtz</keyword>
			<keyword>blez</keyword>
			<keyword>bgez</keyword>
			<keyword>bnez</keyword>
			<keyword>beqz</keyword>
			<keyword>j</keyword>
			<keyword>jr</keyword>
			<keyword>jal</keyword>
			<keyword>jalr</keyword>
			<keyword>getc</keyword>
			<keyword>putc</keyword>
			<keyword>puts</keyword>
			<keyword>done</keyword>
			<keyword>syscall</keyword>
			<keyword>andi</keyword>
                </context>                               
                
                <context id="types" style-ref="type">
			<prefix>\.</prefix>
			<keyword>byte</keyword>
			<keyword>word</keyword>
			<keyword>asciiz</keyword>
			<keyword>ascii</keyword>
			<keyword>float</keyword>
                </context>         
            </include>
        </context>
    </definitions>
</language>[/xml]

That's it.

<h2>See also</h2>
<ul>
  <li>Wikipedia: <a href="http://en.wikipedia.org/wiki/MIPS_architecture">MIPS architecture</a></li>
  <li>Wikibooks: <a href="http://en.wikibooks.org/wiki/MIPS_Assembly">MIPS Assembly</a></li>
  <li><a href="http://spimsimulator.sourceforge.net/">SPIM</a> (a MIPS simulator)</li>
</ul>
