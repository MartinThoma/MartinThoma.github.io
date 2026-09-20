#!/usr/bin/env python3
"""Add the parent tags of the tag hierarchy to all articles.

Every article tagged with a child tag (e.g. "Linear Algebra") also gets the
parents (e.g. "Mathematics"), transitively. Parents are appended to the end
of the tag list. The script is idempotent.

Usage: python3 scripts/apply_tag_hierarchy.py [--dry-run]
"""

import re
import sys
from collections import Counter
from pathlib import Path

# parent: children. A child may be listed under several parents.
HIERARCHY = {
    "Mathematics": [
        "Linear Algebra", "Algebra", "Analysis", "Geometry", "Geometrie",
        "Probability", "Statistics", "Statistik", "Numerics", "Proof",
        "Graph Theory", "Combinations", "Permutations", "Prime Number",
        "Fibonacci", "Fibonacci Number", "Spline", "Fractal",
    ],
    "Linear Algebra": [
        "Matrix", "Eigenraum", "Eigenvektor", "Eigenwert", "Eigenwertproblem",
        "Systems of Equations",
    ],
    "Matrix": ["Matrix Multiplication"],
    "Algebra": ["Boolean Algebra", "Polynomial", "Quaternions"],
    "Analysis": ["Integral Calculus", "Differential Equations"],
    "Numerics": ["Numerical Analysis"],
    "Probability": ["Probability Theory", "Stochastic", "Markov Chain"],
    "Statistics": [],
    "Proof": ["Mathematical Induction", "Structural Induction"],
    "Computer Science": [
        "Theoretical Computer Science", "Algorithms", "Data Structures",
        "Operating Systems", "Assembly Language", "Abstract Machine",
    ],
    "Theoretical Computer Science": [
        "Formal Language", "Formal Grammar", "Chomsky Hierarchy", "Formale Systeme",
    ],
    "Algorithms": [
        "Sorting", "Dynamic Programming", "Backtracking", "Branch-and-Bound",
        "Big-O", "Graph-algorithm", "Strassen Algorithm", "Two-pointer Algorithms",
        "Brute-Force",
    ],
    "Data Structures": ["Stack", "B-tree", "Kd-tree"],
    # "Programming" is only for articles that are about programming. It is deliberately
    # not a parent of language or tool tags (Python, Bash, ...): an article that merely
    # uses a language or a script is not about programming.
    "Programming": ["Programming Language", "Code Golf", "Competitive Programming"],
    "Python": [
        "Flask", "Django", "Pandas", "NumPy", "SciPy", "Matplotlib", "scikit-learn",
        "mypy", "Flake8", "pytest", "tox", "Nox", "venv", "virtualenv", "Pip", "Pipenv",
        "Poetry", "PyPI", "Packaging", "itertools", "SQLAlchemy", "Sympy", "Tkinter",
        "Pypy", "Pyenv", "PyBrain", "Hypothesis", "Pip-tools", "Pipx",
    ],
    "Java": ["Swing"],
    "JavaScript": ["Three.js", "Electron"],
    "Software Engineering": [
        "Testing", "Design Pattern", "Software Architecture", "Software Quality",
        "Software Versioning", "Project Management", "Scrum", "DevOps", "Unit Testing",
    ],
    "Testing": ["Unit Testing", "Fuzzing", "Coverage", "Mock", "Load Testing", "pytest", "tox", "Nox"],
    "DevOps": [
        "Docker", "Ansible", "IaC", "Configuration Management", "Continuous Delivery",
        "Deployment", "DevSecOps",
    ],
    "Web Development": [
        "HTML5", "HTML", "Django", "Flask", "WordPress", "CMS", "Jekyll", "Htaccess",
        "Canvas", "Web Services", "REST", "Three.js",
    ],
    "Database": [
        "MySQL", "MariaDB", "Postgres", "SQL", "NoSQL", "Redis", "SQLAlchemy", "ORM",
        "DBaaS", "DB", "Sysbench", "Query Builder", "Pypika",
    ],
    "Machine Learning": [
        "Neural Networks", "Reinforcement Learning", "Clustering", "Classification",
        "Regression", "SVM", "Decision Tree", "K-means", "Gradient Descent",
        "Tensorflow", "Theano", "Ensembles", "HMM", "Activation Functions", "MNIST",
        "CIFAR 100", "ImageNet", "Pascal VOC", "PyBrain", "Recommendations",
        "Movielens", "Association Rules",
    ],
    "AI": [
        "Machine Learning", "Computer Vision", "NLP", "ASR", "Chatbot", "Expert Systems",
        "Autonomous Vehicles",
    ],
    "Data Science": ["Data Analysis", "Data Visualization", "Big Data", "Dataset", "Datasets"],
    "Security": [
        "AppSec", "OWASP", "Phishing", "2FA", "MFA", "Password", "Encryption",
        "File-encryption", "GPG", "CAPTCHA", "SCA", "VPN", "TLS", "SSL", "HTTPS",
        "OAuth", "OpenID", "JWT", "Signature", "MD5", "Hash", "Crypto", "Spam", "Virus",
        "Lynis", "DevSecOps", "Scam", "Fraud",
    ],
    "Blockchain": ["Cryptocurrency", "Bitcoin", "UTXO"],
    "Cryptocurrency": ["Bitcoin", "UTXO"],
    "Linux": ["Ubuntu", "ArchLinux", "openSUSE", "GNOME", "Nautilus"],
    # "Operating Systems" is deliberately not a parent of Linux, Windows or Ubuntu: it is
    # only for articles about operating systems in general.
    "Windows": ["Windows 7", "Windows 8.1"],
    "Science": ["Physics", "Neuroscience"],
    "Politics": [
        "Bundestagswahl", "CDU", "CSU", "SPD", "FDP", "LINKE", "Grüne", "Piratenpartei",
        "German Politics", "Voting",
    ],
    "Health": ["Medicine", "Health Care", "Health Insurance", "Coronavirus", "Pandemic"],
    "Energy": ["Photovoltaics", "Photovoltaik", "Solar", "Heat Pumps"],
    "House": [
        "Building", "Hausbau", "Heat Pumps", "Heating", "Home Improvement", "Smart Home",
        "Photovoltaics",
    ],
    "Cooking": ["Recipe", "Main Dish", "Vegetarian", "Sweet Dish", "Food", "Reste-Essen"],
    "Video": ["Shortfilm", "Stop Motion"],
    "Games": ["Flashgames", "JavaScript Game", "Board Game", "Chess"],
    "Hardware": [
        "Devices", "Device", "Monitor", "Headphones", "Microphone", "Smartphone",
        "Notebook", "Notebooks", "Camera", "Cameras", "Display", "Screen",
    ],
    "Money": ["Banking", "Investment", "N26"],
    "LaTeX": ["Tikz", "Beamer"],
    "KIT": [
        "GBI", "SWT I", "KogSys", "Digitaltechnik", "Formale Systeme",
        "Programmierparadigmen", "Information Fusion",
    ],
    "University": ["KIT", "Klausur", "Lecture Notes"],
}


def parents_of():
    parents = {}
    for parent, children in HIERARCHY.items():
        for child in children:
            parents.setdefault(child, []).append(parent)
    return parents


def ancestors(tag, parents, seen=None):
    seen = seen if seen is not None else []
    for parent in parents.get(tag, []):
        if parent not in seen:
            seen.append(parent)
            ancestors(parent, parents, seen)
    return seen


def main():
    dry_run = "--dry-run" in sys.argv
    parents = parents_of()
    added = Counter()
    changed = 0
    for path in sorted(Path("content").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        front, sep, rest = text.partition("\n---\n")
        match = re.search(r"^tags:[ \t]*(.*)$", front, re.M)
        if not match:
            continue
        tags = [t.strip() for t in match.group(1).split(",") if t.strip()]
        new = list(tags)
        for tag in tags:
            for anc in ancestors(tag, parents):
                if anc not in new and anc != tag:
                    new.append(anc)
                    added[anc] += 1
        if new != tags:
            changed += 1
            if not dry_run:
                front = front[: match.start()] + "tags: " + ", ".join(new) + front[match.end():]
                path.write_text(front + sep + rest, encoding="utf-8")
    print(f"{changed} articles changed; parent tags added: {dict(added.most_common())}")


if __name__ == "__main__":
    main()
