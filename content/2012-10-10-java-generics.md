---
layout: post
title: Java Generics
slug: java-generics
lang: en
author: Martin Thoma
date: 2012-10-10 12:18:42.000000000 +02:00
category: Code
tags: Java, Generics
featured_image: 2012/07/java-thumb.png
---
Some months ago, I had to improve some Java code for university. They gave us a model of a windows like file system and we had to make the code "cleaner". I think I've overdone the application of generics, but it's a nice example for generics 😉

You can download the <a href="../images/2012/10/Filesystem.zip">complete Eclipse project</a>.

## Computer.java

```java
package edu.kit.filesystem;

import java.util.ArrayList;
import java.util.Vector;

public class Computer {
    public String computerName;
    public Vector<HDD> hdds = new Vector<HDD>();

    public Computer(String companyName, HDD gf) {
        this.computerName = companyName;
        this.hdds.add(gf);
    }

    private void addDrive(HDD drive) {
        hdds.add(drive);
    }

    public void printContent() {
        for (HDD hdd : hdds) {
            System.out.println("| HDD: " + hdd.getName() + " (" + hdd.getDescription() + ")");

            for (Directory dir : hdd.get(Directory.class)) {
                printContent(dir, "");
            }

            for (ZipArchiv zip : hdd.get(ZipArchiv.class)) {
                printContent(zip, "");
            }

            for (File f : hdd.get(File.class)) {
                printContent(f, "|-");
            }
        }
    }

    private void printContent(Node d, String ident) {
        System.out.println("|-" + ident + " " + d.getName());

        ArrayList<Class<? extends Node>> list = new ArrayList<Class<? extends Node>>();
        list.add(Directory.class);
        list.add(ZipArchiv.class);
        list.add(File.class);

        if (d instanceof NodeContainer) {
            NodeContainer e = (NodeContainer) d;
            for (Class<? extends Node> T : list) {
                ArrayList<? extends Node> tmp = e.get(T);
                for (Node n : tmp) {
                    printContent(n, ident + "-");
                }
            }
        }
    }

    public static void main(String[] args) {
        // Create the computer
        HDD platte1 = new HDD("C", "Main disk");
        Computer f = new Computer("MyMainComputer", platte1);

        // we need a backup
        HDD platte2 = new HDD("D", "Backup disk");
        f.addDrive(platte2);

        // create main directories
        Directory v1 = new Directory("temp", "temporary files");
        platte1.addNode(v1);
        v1.addNode(new Directory("asdf", "jklö"));
        Directory v2 = new Directory("Pictures", "Holiday pictures");
        platte1.addNode(v2);

        // Gib den Verzeichnissen ein paar Inhalte
        // Ein paar Archive im Temp
        ZipArchiv zip1 = new ZipArchiv("fp-update.zip", "Flashplayer Update");
        v1.addNode(zip1);
        ZipArchiv zip2 = new ZipArchiv("swt1-folien.zip", "PDFs of SWT1");
        v1.addNode(zip2);

        // pictures
        ZipArchiv barcelona = new ZipArchiv("2010-Barcelona.zip", "Holiday Barcelona 2010");
        v2.addNode(barcelona);
        ZipArchiv mallorca = new ZipArchiv("2011-Mallorca.zip", "Sonne satt");
        v2.addNode(mallorca);
        v2.addNode(new File("ipdlogo.png", "IPD"));

        // add some files to archives
        ZipArchiv b1 = new ZipArchiv("BarcelonaBeach.zip", "Strandbilder");
        barcelona.addNode(b1);
        b1.addNode(new File("s1.jpg", "Strand"));
        b1.addNode(new File("s2.jpg", "Mehr Strand"));
        b1.addNode(new File("s3.jpg", "Strand und Meer"));
        b1.addNode(new File("s4.jpg", "Noch mehr Strand"));

        File b2 = new File("Picasso.jpg", "Museum");
        barcelona.addNode(b2);

        File b3 = new File("SagradaFamilia.jpg", "Kirche");
        barcelona.addNode(b3);

        File b4 = new File("CampNou.jpg", "Fußball");
        barcelona.addNode(b4);

        File m1 = new File("Strand.jpg", "Strand");
        mallorca.addNode(m1);

        f.printContent();
    }
}
```

<h2>Node.java</h2>

```java
package edu.kit.filesystem;

public abstract class Node {
    private String name;
    private String description;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}
```

<h2>NodeContainer.java</h2>

```java
package edu.kit.filesystem;

import java.util.ArrayList;

public interface NodeContainer {
    public <T> ArrayList<T> get(Class<T> clazz);
    public void addNode(Node n);
}
```

<h2>HDD.java</h2>

```java
package edu.kit.filesystem;

import java.util.ArrayList;

public class HDD extends Node implements NodeContainer {
    private final ArrayList<Node> nodes = new ArrayList<Node>();

    public HDD(String name, String beschreibung) {
        this.setName(name);
        this.setDescription(beschreibung);
    }

    @SuppressWarnings("unchecked")
    public <T> ArrayList<T> get(Class<T> clazz) {
        ArrayList<T> allElements = new ArrayList<T>();
        for(Node o : nodes) {
            if (o.getClass() == clazz) {
                allElements.add((T) o);
            }
        }
        return allElements;
    }

    public void addNode(Node n) {
        nodes.add(n);
    }
}
```

<h2>Directory.java</h2>

```java
package edu.kit.filesystem;

import java.util.ArrayList;

public class Directory extends Node implements NodeContainer {
    private final ArrayList<Node> nodes = new ArrayList<Node>();

    public Directory(String name, String description) {
        this.setName(name);
        this.setDescription(description);
    }

    public void addNode(Node n) {
        nodes.add(n);
    }

    @SuppressWarnings("unchecked")
    public <T> ArrayList<T> get(Class<T> clazz) {
        ArrayList<T> allElements = new ArrayList<T>();
        for(Node o : nodes) {
            if (o.getClass() == clazz) {
                allElements.add((T) o);
            }
        }
        return allElements;
    }
}

```

<h2>ZipArchiv.java</h2>

```java
package edu.kit.filesystem;

import java.util.ArrayList;

public class ZipArchiv extends File implements NodeContainer {
    private final ArrayList<Node> nodes = new ArrayList<Node>();

    public ZipArchiv(String name, String description) {
        super(name, description);
    }

    public void addNode(Node n) {
        nodes.add(n);
    }

    @SuppressWarnings("unchecked")
    public <T> ArrayList<T> get(Class<T> clazz) {
        ArrayList<T> allElements = new ArrayList<T>();
        for(Node o : nodes) {
            if (o.getClass() == clazz) {
                allElements.add((T) o);
            }
        }
        return allElements;
    }
}
```

<h2>File.java</h2>

```java
package edu.kit.filesystem;

public class File extends Node {
    public File(String name, String beschreibung) {
        this.setName(name);
        this.setDescription(beschreibung);
    }
}
```
