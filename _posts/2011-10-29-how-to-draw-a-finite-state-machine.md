---
layout: post
title: How to draw a finite-state machine
author: Martin Thoma
date: 2011-10-29 09:37:50.000000000 +02:00
category: My bits and bytes
tags: Computer science, LaTeX, Abstract machine, Tikz
featured_image: 2011/10/deterministic-finite-state-machine-thumb.png
---
<a href="http://en.wikipedia.org/wiki/Deterministic_finite-state_machine">Finite-state machines</a> are necessary to show that some problems are computable (or not).

As I am currently learning something about them, I would like to be able to plot those finite automatons automatically. I will use <a href="http://www.graphviz.org/">graphviz</a>.
<h2>Nondeterministic finite-state machine</h2>
{% caption align="aligncenter" width="365" caption="Nondeterministic finite-state machine" url="../images/2011/10/myFiniteStateMachine1.png" alt="Nondeterministic finite-state machine"  height="119" class="size-full wp-image-8141 "  %}

This image is created from a gv-file. I saved it as fsm.gv:

```latex
digraph finite_state_machine {
	rankdir=LR;
	size="8,5"

	node [shape = doublecircle]; S;
	node [shape = point ]; qi

	node [shape = circle];
	qi -> S;
	S  -> q1 [ label = "a" ];
	S  -> S  [ label = "a" ];
	q1 -> S  [ label = "a" ];
	q1 -> q2 [ label = "b" ];
	q2 -> q1 [ label = "b" ];
	q2 -> q2 [ label = "b" ];
}
```

To create a graph (or the picture of the nondeterministic finite-state machine) you have to enter the following command in Ubuntu Linux:

```bash
dot -Tpng fsm.gv -o myFiniteStateMachine.png
```

<h2>Deterministic finite-state machine</h2>

<figure class="aligncenter">
            <a href="../images/2011/10/deterministic-finite-state-machine.png"><img src="../images/2011/10/deterministic-finite-state-machine.png" alt="Deterministic finite-state machine" style="max-width:528px;max-height:248px" class="size-full wp-image-8171"/></a>
            <figcaption class="text-center">Deterministic finite-state machine</figcaption>
        </figure>

```latex
digraph finite_state_machine {
	rankdir=LR;
	size="8,5"

	node [shape = doublecircle, label="{f}", fontsize=12] f;
	node [shape = doublecircle, label="{q2, f}", fontsize=10] q2f;

	node [shape = circle, label="S", fontsize=14] S;
	node [shape = circle, label="{q1}", fontsize=12] q1;
	node [shape = circle, label="{q2}", fontsize=12] q2;

	node [shape = point ]; qi
	qi -> S;

	S   -> q1  [ label = "a" ];
	S   -> q2f [ label = "b" ];
	S   -> q2  [ label = "c" ];

	q1  -> q2  [ label = "b" ];

	q2f -> f   [ label = "b" ];
	q2f -> q2  [ label = "c" ];

	q2  -> f   [ label = "b" ];
	q2  -> q2  [ label = "c" ];
}
```

<h2>LaTeX</h2>
If you want to draw finite-state machines with LaTeX, you might want to give <a href="http://www.texample.net/tikz/examples/feature/automata-and-petri-nets/">tikz</a> a try.

This is the most minimalistic version I could create. It is equivalent to the nondeterministic finite-state machine I've described above:

```latex
\documentclass{scrartcl}
\usepackage{tikz}
\usetikzlibrary{arrows,automata}

\begin{document}
\begin{tikzpicture}[>=stealth',shorten >=1pt,auto,node distance=2cm]
  \node[initial,state,accepting] (S)      {$S$};
  \node[state]         (q1) [right of=S]  {$q_1$};
  \node[state]         (q2) [right of=q1] {$q_2$};


  \path[->] (S)  edge [loop above] node {a} (S)
             edge              node {a} (q1)
        (q1) edge [bend left]  node {a} (S)
             edge              node {b} (q2)
        (q2) edge [loop above] node {b} (q2)
             edge [bend left]  node {b} (q1);
\end{tikzpicture}
\end{document}
```

This was the most basic example which shows how to draw a finite-state automaton with LaTeX. You can get it as a PDF with this command:

```bash
pdflatex latexsheet.tex -output-format=pdf
```

If you want to see some more fancy stuff, take a look at this example of a non-deterministic finite state machine:

<figure class="aligncenter">
            <a href="../images/2011/10/latex-finite-state-machine.png"><img src="../images/2011/10/latex-finite-state-machine.png" alt="Finite-state-machine with LaTeX" style="max-width:400px;max-height:147px" class="size-full wp-image-13421"/></a>
            <figcaption class="text-center">Finite-state-machine with LaTeX</figcaption>
        </figure>

```latex
\documentclass{scrartcl}
\usepackage{tikz}
\usetikzlibrary{arrows,automata}
 
\begin{document}
\begin{tikzpicture}[>=stealth',shorten >=1pt,auto,node distance=2cm]
  \node[initial,state,accepting] (S)      {$S$};
  \node[state]         (q1) [right of=S]  {$q_1$};
  \node[state]         (q2) [right of=q1] {$q_2$};
 
  \path[->]          (S)  edge [loop above] node {a} (S);
  \path[->, dashed]  (S)  edge              node {a} (q1);
  \path[->, dotted]  (q1) edge [bend left]  node {a} (S);
  \path[->>, dotted] (q1) edge             node {b} (q2);
  \path              (q2) edge [loop above] node {b} (q2)
             edge [bend left]  node {b} (q1);
\end{tikzpicture}
\end{document}
```

<h3>Markov models</h3>
```latex
\documentclass{scrartcl}
\usepackage{tikz}
\usetikzlibrary{arrows,automata}

\begin{document}
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,node distance=2.8cm]
    % When you want to use // inside of nodes, you have to algin
    \tikzstyle{every state}=[align=center]
    \node[state,initial,label=below:Start] (Start)
                                            {A 0.6\\B 0.2\\C 0.2};
    \node[state,label=below:Mitte] (Mitte) [right of=Start] 
                                            {A 0.1\\B 0.1\\C 0.8};
    \node[state,label=below:Ende] (Ende)   [right of=Mitte] 
                                            {A 0.5\\B 0.2\\C 0.3};
    \path (Start) edge               node[above] {0.2} (Mitte);
    \path (Mitte) edge               node[above] {0.8} (Ende);
    \path (Start) edge  [loop above] node        {0.8} (Start);
    \path (Mitte) edge  [loop above] node        {0.2} (Mitte);
    \path (Ende)  edge  [loop above] node        {1}  (Ende);
\end{tikzpicture}
\end{document}
```

<h2>Further Reading</h2>
<ul>
    <li><a href="http://www.graphviz.org/doc/info/shapes.html">DOT Node Shape reference</a></li>
    <li><a href="http://wiki.ubuntuusers.de/Graphviz">ubuntuusers.de</a> (German): Installation on Ubuntu</li>
    <li><a href="http://www.wikischool.de/wiki/WikiSchool:Graphviz">Wikischool.de</a> (German): Many examples</li>
</ul>
