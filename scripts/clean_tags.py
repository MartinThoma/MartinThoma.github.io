#!/usr/bin/env python3
"""
Tag Cleanup Script for Blog

This script cleans up tags in blog posts based on the analysis results:
1. Standardizes capitalization
2. Consolidates similar tags
3. Removes duplicate tags
4. Maintains consistent tag naming

Usage: python3 clean_tags.py [--dry-run]
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
import argparse
from collections import defaultdict


# Tag standardization mappings
TAG_CONSOLIDATIONS = {
    # Capitalization fixes
    'machine learning': 'Machine Learning',
    'research': 'Research',
    'data science': 'Data Science',
    'physics': 'Physics',
    'data': 'Data',
    'germany': 'Germany',
    'computer science': 'Computer Science',
    'data analysis': 'Data Analysis',
    'design': 'Design',
    'energy': 'Energy',
    'numpy': 'NumPy',
    
    # Tag consolidations - merge similar tags
    'Machine learning': 'Machine Learning',
    'machine learning': 'Machine Learning',
    'learning': 'Machine Learning',  # When in ML context
    
    'Computer science': 'Computer Science',
    'Theoretical computer science': 'Computer Science',
    
    'Software Development': 'Development',
    'Web Development': 'Development',
    
    'Software Engineering': 'Engineering',
    'Data Engineering': 'Engineering',
    
    'IT-Security': 'Security',
    'CyberSecurity': 'Security',
    'Cybersecurity': 'Security',
    'Internet Security': 'Security',
    'IT Security': 'Security',
    
    'Data analysis': 'Data Analysis',
    'analysis': 'Data Analysis',  # In data context
    
    'Programming language': 'Programming Languages',
    'Esoteric programming language': 'Programming Languages',
    
    'Command line': 'Command Line',
    'command line arguments': 'Command Line',
    
    'Unit Testing': 'Testing',
    'Load Testing': 'Testing',
    'A/B-Testing': 'Testing',
    'unit testing': 'Testing',
    
    'Competitive Programming': 'Programming',
    'Dynamic Programming': 'Programming',
    
    'Data Science': 'Science',
    'Neuroscience': 'Science',
    'Science Fiction': 'Science',
    'data science': 'Science',
    
    'Encodings': 'Encoding',
    
    'Windows 7': 'Windows',
    'Windows 8.1': 'Windows',
    'windowsrage': 'Windows',
    
    'Linear algebra': 'Algebra',
    'Boolean algebra': 'Algebra',
    'Computer Algebra System': 'Algebra',
    
    'Neural Networks': 'Networks',
    'Network': 'Networks',
    
    'cheat sheet': 'Cheat',
    
    'software versioning': 'Software',
    'Software Projects': 'Software',
    'Software Quality': 'Software',
    'Software Architecture': 'Software',
    
    'Bug': 'Bugs',
    'bug': 'Bugs',
    
    'Fibonacci number': 'Fibonacci',
    
    'Assembly language': 'Language',
    'Programming Languages': 'Language',
    
    'algorithm': 'Algorithms',
    'two-pointer algorithms': 'Algorithms',
    'graph-algorithm': 'Algorithms',
    
    'ArchLinux': 'Linux',
    
    'Internet Explorer': 'Internet',
    
    'Algebra': 'Mathematics',
    
    'Funny': 'Humor',
    'funny': 'Humor',
    
    'Google Code Jam': 'Google',
    'Google Scholar': 'Google',
    'Google Maps': 'Google',
    
    'itertools': 'Tools',
    
    'Reinforcement Learning': 'Machine Learning',
    
    'Information': 'Data',
    'Information Extraction': 'Data',
    'information fusion': 'Data',
    
    'Visualization': 'Data Visualization',
    
    'Competition': 'Competitive Programming',
    
    'Politics': 'German Politics',
    'politics': 'German Politics',
    
    'German posts': 'German',
    'germany': 'German',
    
    'BwInf': 'BWInf',
    
    'Configuration': 'Configuration Management',
    
    'climate change': 'Climate Change',
    
    'Health Insurance': 'Health',
    
    'hiking': 'Hiking',
    
    'NumPy': 'Python Libraries',
    'numpy': 'Python Libraries',
    'Matplotlib': 'Python Libraries',
    'matplotlib': 'Python Libraries',
    
    'Project Euler': 'Competitive Programming',
    
    'Reading': 'Literature',
    
    'optimization': 'Optimization',
    
    'R': 'Programming Languages',
    'RSS': 'Web',
    
    'Presentation': 'Presentations',
    
    'cloud': 'Cloud Computing',
    'ownCloud': 'Cloud Computing',
    'NextCloud': 'Cloud Computing', 
    'OpenCloud': 'Cloud Computing',
    
    'Operations Research': 'Research',
    
    'Computer Science': 'Science',
    
    'Algorithms': 'Computer Science',
    
    'CMO': 'CMOS',
    
    'House': 'Home',
    'house': 'Home',
    'Household': 'Home',
    
    'ArchLinux': 'Operating Systems',
    
    'design process': 'Design',
    
    'Comic': 'Comics',
    'Webcomic': 'Comics',
    
    'Space': 'Physics',
    'Whitespace': 'Programming',
    
    'Energy': 'Physics',
    
    'Education': 'Learning',
    'education': 'Learning',
    
    'Windows': 'Operating Systems',
    
    'devices': 'Hardware',
    'Device': 'Hardware',
    
    'data structure': 'Data Structures',
    'datastructure': 'Data Structures',
    'struct': 'Data Structures',
    'Structural induction': 'Data Structures',
    'structure from motion': 'Computer Vision',
    
    'Flashgames': 'Games',
    'Game': 'Games',
    
    'Service': 'Web Services',
    
    'file-encryption': 'Encryption',
    'encryption': 'Encryption',
    
    'Sublime': 'Text Editors',
    'Sublime Text': 'Text Editors',
    
    'community-chess': 'Chess',
    'chess': 'Chess',
    
    'project': 'Projects',
    'Project Management': 'Projects',
    'Project Euler': 'Competitive Programming',
    'Software Projects': 'Projects',
    
    'Discussions': 'Communication',
    'discussion': 'Communication',
    
    'JavaScript Game': 'JavaScript',
    
    'cameras': 'Photography',
    'Camera': 'Photography',
    
    'Design Pattern': 'Design',
    
    'Apache': 'Web Servers',
    'apache': 'Web Servers',
    
    'File': 'File Systems',
    'file': 'File Systems',
    
    'Phishing': 'Security',
    'phishing': 'Security',
    
    'Data formats': 'Data',
    'format': 'Data',
    
    'ImageNet': 'Computer Vision',
    'image': 'Image Processing',
    'ImageMagick': 'Image Processing',
    
    'Flashgames': 'Gaming',
    
    'Data Visualization': 'Visualization',
    
    'Coronavirus': 'Medicine',
    'Virus': 'Computer Security',
    
    'datastructure': 'Data Structures',
    
    'Terminology': 'Language',
    'terminology': 'Language',
    
    'Operations Research': 'Mathematics',
    
    'notebooks': 'Hardware',
    'Notebook': 'Hardware',
    
    'map': 'Data Structures',
    'maps': 'Geography',
    
    'music': 'Music',
    'sheet music': 'Music',
    
    'numerical analysis': 'Mathematics',
    
    'Password': 'Security',
    'password': 'Security',
    
    'Cryptocurrency': 'Finance',
    'crypto': 'Cryptography',
    
    'Datasets': 'Data',
    'dataset': 'Data',
    
    'Datetime': 'Programming',
    'datetime': 'Programming',
    
    'BWInf': 'Competitive Programming',
    'Bundeswettbewerb': 'Competitive Programming',
    'Wettbewerb': 'Competitive Programming',
    
    'Mathematics': 'Science',
    'mathematics': 'Science',
    
    'Git': 'Version Control',
    'git': 'Version Control',
    
    'physics': 'Science',
    'Physics': 'Science',
    
    'Eigenwert': 'Linear Algebra',
    'Eigenwertproblem': 'Linear Algebra',
    
    'Gradient Descent': 'Optimization',
    'gradient descent': 'Optimization',
    
    'Community': 'Social',
    'community-chess': 'Social',
    
    'Configuration Management': 'DevOps',
    
    'probability': 'Statistics',
    'Probability Theory': 'Statistics',
    
    'Whitespace': 'Text Processing',
    
    'information fusion': 'Data Processing',
    
    'IT Security': 'Security',
    
    'movie': 'Entertainment',
    'Movielens': 'Entertainment',
    
    'Multithreading': 'Concurrency',
    'multithreading': 'Concurrency',
    
    'reviews': 'Reviews',
    'Review': 'Reviews',
    'review': 'Reviews',
    
    'Presentations': 'Communication',
    'Presentation': 'Communication',
    
    'Encoding': 'Text Processing',
    'encoding': 'Text Processing',
    'Encodings': 'Text Processing',
    
    'University': 'Education',
    'university': 'Education',
}

# Tags to remove (too generic or redundant)
TAGS_TO_REMOVE = {
    'stuff', 'thing', 'various', 'misc', 'general', 'other', 'random'
}

# Tags that should remain unchanged (high-value specific tags)
PROTECTED_TAGS = {
    'Python', 'Machine Learning', 'Java', 'C', 'CPP', 'LaTeX', 
    'KIT', 'Klausur', 'cooking', 'recipe', 'AppSec', 'InfoSec',
    'AI', 'Flask', 'Docker', 'SQL', 'MongoDB', 'Redis',
    'TensorFlow', 'PyTorch', 'Keras', 'OpenCV', 'pandas',
    'NumPy', 'matplotlib', 'scikit-learn', 'Jupyter'
}


def extract_front_matter(content: str) -> Tuple[Dict[str, Any], str]:
    """Extract YAML front matter from markdown content."""
    if not content.startswith('---\n'):
        return {}, content
    
    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return {}, content
    
    try:
        front_matter = yaml.safe_load(parts[1])
        body = parts[2]
        return front_matter or {}, body
    except yaml.YAMLError:
        return {}, content


def reconstruct_content(front_matter: Dict[str, Any], body: str) -> str:
    """Reconstruct markdown content with updated front matter."""
    if not front_matter:
        return body
    
    yaml_content = yaml.dump(front_matter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{yaml_content}---\n{body}"


def normalize_tag(tag: str) -> str:
    """Normalize a single tag according to consolidation rules."""
    if tag in PROTECTED_TAGS:
        return tag
    
    if tag in TAGS_TO_REMOVE:
        return ""
    
    return TAG_CONSOLIDATIONS.get(tag, tag)


def clean_tags(tags, original_format='list'):
    """Clean and normalize a list of tags while preserving format."""
    if not tags:
        return [] if original_format == 'list' else ''
    
    # Detect original format
    was_string = isinstance(tags, str)
    
    # Handle both string and list formats
    if isinstance(tags, str):
        # Split comma-separated tags
        tag_list = [tag.strip() for tag in tags.split(',')]
    else:
        tag_list = tags
    
    # Normalize tags while preserving order
    normalized = []
    for tag in tag_list:
        if isinstance(tag, str) and tag.strip():
            normalized_tag = normalize_tag(tag.strip())
            if normalized_tag and normalized_tag not in normalized:
                normalized.append(normalized_tag)
    
    # Return in original format
    if was_string:
        return ', '.join(normalized)
    else:
        return normalized


def process_file(file_path: Path, dry_run: bool = False) -> bool:
    """Process a single markdown file to clean its tags."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        front_matter, body = extract_front_matter(content)
        
        if 'tags' not in front_matter:
            return False
        
        original_tags = front_matter['tags']
        cleaned_tags = clean_tags(original_tags)
        
        # Check if tags changed
        if original_tags == cleaned_tags:
            return False
        
        print(f"\n{file_path.name}:")
        print(f"  Original: {original_tags}")
        print(f"  Cleaned:  {cleaned_tags}")
        
        if not dry_run:
            front_matter['tags'] = cleaned_tags
            new_content = reconstruct_content(front_matter, body)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Clean up blog tags')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be changed without making changes')
    args = parser.parse_args()
    
    script_dir = Path(__file__).parent
    blog_dir = script_dir.parent
    
    # Find all markdown files
    markdown_files = []
    for pattern in ['content/**/*.md', '_drafts/**/*.md', '*.md']:
        markdown_files.extend(blog_dir.glob(pattern))
    
    # Filter out non-post files
    post_files = []
    for file_path in markdown_files:
        if file_path.name not in ['README.md', 'CONTRIBUTING.md', 'LICENSE.md']:
            post_files.append(file_path)
    
    print(f"Found {len(post_files)} markdown files to process")
    
    if args.dry_run:
        print("\n=== DRY RUN MODE - No files will be modified ===")
    
    changed_files = 0
    for file_path in sorted(post_files):
        if process_file(file_path, args.dry_run):
            changed_files += 1
    
    print(f"\n=== Summary ===")
    print(f"Files processed: {len(post_files)}")
    print(f"Files with tag changes: {changed_files}")
    
    if args.dry_run:
        print("\nRun without --dry-run to apply changes")
    else:
        print(f"\nTag cleanup complete!")


if __name__ == '__main__':
    main()