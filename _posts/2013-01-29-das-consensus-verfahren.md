---
layout: post
title: Das Consensus-Verfahren
author: Martin Thoma
date: 2013-01-29 16:23:14.000000000 +01:00
categories:
- German posts
tags:
- Digitaltechnik
---
Mithilfe des Consensus-Verfahrens k&ouml;nnen Primimplikanten gefunden werden. Dazu braucht man eine Schaltfunktion $f:\{0,1\}^n \rightarrow \{0,1\}$ in disjunktiver Normalform (DNF). Zu betonen ist, dass man keine Minimalform bekommt, da das &Uuml;berdeckungsproblem noch gel&ouml;st werden muss. Dies kann man z.B. mit der <a href="../das-quine-mccluskey-verfahren/" title="Das Quine-McCluskey-Verfahren">zweiten Quineschen Tabelle</a> machen.

Dazu baut man eine Tabelle auf. Ich nenne sie mal Consensus-Tabelle. Diese hat 4 Spalten:
<ul>
  <li>Nr.</li>
  <li>Gebildet aus</li>
  <li>W&uuml;rfel - eine Spalte f&uuml;r jeden der $n$ Parameter der Schaltfunktion $f$</li>
  <li>Gestrichen wegen</li>
</ul>

Nun ergibt jeder Minterm der DNF eine Zeile in der Consensus-Tabelle. Die Reihenfolge ist dabei egal. Die Nr. wird fortlaufend von 1 an gesetzt, die Spalte &bdquo;Gebildet aus&ldquo; bleibt erst mal leer. Nun zieht man eine Linie, um die folgenden Zeilen abzutrennen. Diesen abgetrennten Teil nennen ich nun &bdquo;Block&ldquo;.

Man vergleicht nun jede Zeile mit den dar&uuml;ber liegenden Zeilen.
<ul>
<li>*: Falls an einer bestimmten Stelle nur eine der Zeilen ein don't care hat, wird an dieser Stelle der Wert der anderen Zeile genommen. Diese Spalte z&auml;hlt also nicht als unterschiedlich.</li>
<li>Unterscheiden sich zwei Zeilen nur an einer Stelle, schreibt man eine neue Zeile in den neuen Block. Diese Zeile hat ein don't care an der Stelle, an der sich die beiden Zeilen unterschieden, eine eigene Nummer. Eventuell &uuml;berdeckt die neue Zeile beide vorhergehenden. Wegen der don't care-Regelung (*) muss das jedoch nicht der Fall sein.</li>
</ul>
Sobald man alle Zeilen des vorhergehenden Block &uuml;berpr&uuml;ft hat, kann man wieder eine Linie machen.

Das sieht dann etwa so aus (aus Folien von Prof. Dr. Asfour):
{% caption align="aligncenter" width="300" caption="Consensus-Verfahren" url="../images/2013/01/consensus-verfahren-300x165.png" alt="Consensus-Verfahren"  height="165" class="size-medium wp-image-55531" %}

Wie man sieht, kann es auch sein, dass eine neue Zeile bereits von einer alten &uuml;berdeckt wird. Diese Zeilen kann man also direkt streichen.
Sobald man keine neuen Zeilen / Bl&ouml;cke mehr bilden kann, ist man fertig. Die Zeilen, die nicht gestrichen wurden, sind Primimplikanten.

<h2>Code</h2>
Ich finde Algorithmen werden am eindeutigsten durch Implementierungen beschrieben. Hier ist meine f&uuml;r das Consensus-Verfahren:

{% highlight python %}
#!/usr/bin/python
# -*- coding: utf-8 -*-

def initDatastructure(terme):
	dictList = []
	for nr, term in enumerate(terme):
		dictList.append({'number': nr+1, 'gebildet':'', 
					     'term':term, 'gestrichen': False})
	return dictList

''' check if item1 and item2 differ in at least one digit '''
def hasComplementaryDigit(item1, item2):
	term1 = item1['term']
	term2 = item2['term']
	for i in range(len(term1)):
		if (term1[i] == '1' and term2[i] == '0') or \
		   (term1[i] == '0' and term2[i] == '1'):
			return True
	return False

''' check if item1 and item2 have a consensus term '''
def hasConsensus(item1, item2):
	term1 = item1['term']
	term2 = item2['term']
	differences = 0
	for i in range(len(term1)):
		if (term1[i] != term2[i]) and (term1[i] != '-') and (term2[i] != '-'):
			differences += 1
	return differences <= 1

''' create the consensus term of two items '''
def getConsensus(item1, item2):
	term1 = item1['term']
	term2 = item2['term']
	consensus = ''
	for i in range(len(term1)):
		if term1[i] == term2[i]:
			consensus += term1[i]
		elif (term1[i] != term2[i]) and (term1[i] != '-') and (term2[i] != '-'):
			consensus += '-'
		elif (term1[i] != term2[i]) and (term1[i] != '-'):
			consensus += term1[i]
		else:
			consensus += term2[i]

	return consensus

def isIncludedIn(bigger, smaller):
	for i in range(len(bigger)):
		if bigger[i] != '-' and bigger[i] != smaller[i]:
			return False
	return True

def consensusIsIncludedIn(dictList, consensus):
	for element in dictList:
		if element['gestrichen'] == False and \
		   isIncludedIn(element['term'], consensus):
			return element['number']
	return False

def printList(dictList, horizontalLinesAfter):
	print('Nr\t Gebildet aus \t W&uuml;rfel\t Gestrichen wegen')
	for line, element in enumerate(dictList):
		if element['gestrichen'] == False:
			element['gestrichen'] = ''
		if element['number'] == False:
			element['number'] = ''
		print('%s\t\t%s\t%s\t%s' % (element['number'], element['gebildet'], 
				element['term'], element['gestrichen']))
		if line in horizontalLinesAfter:
			print('-'*50)

def consensus(terme):
	dictList = initDatastructure(terme)
	horizontalLinesAfter = [len(dictList)-1]
	pointer2 = 1
	nextNumber = len(dictList) + 1

	while pointer2 != (len(dictList)-1):
		if pointer2 > horizontalLinesAfter[-1]:
			horizontalLinesAfter.append(len(dictList)-1)

		if dictList[pointer2]['gestrichen'] != False:
			pointer2 += 1
			continue

		for pointer1 in range(pointer2 - 1, -1,-1):
			if dictList[pointer1]['gestrichen'] != False:
				continue
			elif not hasComplementaryDigit(dictList[pointer1], dictList[pointer2]):
				continue
			elif not hasConsensus(dictList[pointer1], dictList[pointer2]):
				continue

			consensus = getConsensus(dictList[pointer1], dictList[pointer2])

			# Wird der neue Konsensus-Term eventuell bereits &uuml;berdeckt?
			gestrichen = consensusIsIncludedIn(dictList, consensus)
			if gestrichen == False:
				nr = nextNumber
				nextNumber += 1
			else:
				nr = False

			# Kann dank dem neuen Consensus-Term etwas gestrichen werden?
			if gestrichen == False:
				for element in dictList:
					if element['gestrichen'] == False and \
				  	   isIncludedIn(consensus, element['term']):
						element['gestrichen'] = nr

			dictList.append({'number' : nr, 
							 'gebildet': str(dictList[pointer2]['number']) + 
							           ', ' + str(dictList[pointer1]['number']),
							 'term': consensus,
							 'gestrichen' : gestrichen})
		pointer2 += 1
	printList(dictList, horizontalLinesAfter)

consensus(['-0-00', '--00-', '-1-00', '010-1', '1-11-', '110-1'])
#consensus(['-00-', '-011', '0100'])
{% endhighlight %}

Ausgabe:
{% highlight text %}
Nr	 Gebildet aus 	 W&uuml;rfel	 Gestrichen wegen
1			-0-00	7
2			--00-	
3			-1-00	7
4			010-1	9
5			1-11-	
6			110-1	9
--------------------------------------------------
7		3, 1	---00	
8		6, 5	11-11	
9		6, 4	-10-1	
--------------------------------------------------
10		7, 5	1-1-0	
		8, 2	110-1	9
		9, 7	-100-	2
		9, 5	11-11	8
--------------------------------------------------
		10, 8	1111-	5
		10, 2	1--00	7
--------------------------------------------------
{% endhighlight %}

<h2>Quellen</h2>
Die Folien von Dr. Asfour (DT-VL12) sowie die Vorlesung (auf <a href="http://www.youtube.com/watch?v=K1NAj4ecPDw#t=31m18s">YouTube</a> verf&uuml;gbar. Der <a href="http://www.youtube.com/watch?v=K1NAj4ecPDw#t=47m30s">interessante Teil</a> beginnt erst sehr sp&auml;t.). Es wurde sogar <a href="http://www.youtube.com/watch?v=4X1w0B4w65k#t=1h10m38s">sp&auml;ter nochmals von Herrn Prof. Dr. Asfour erkl&auml;rt</a>.
