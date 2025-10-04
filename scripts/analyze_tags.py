#!/usr/bin/env python3
"""
Analyze tags in blog articles.

This script extracts all tags from markdown files and counts their usage.
"""

import os
import re
from collections import Counter
from pathlib import Path
import yaml


def extract_front_matter(content):
    """Extract YAML front matter from markdown content."""
    # Match front matter between --- delimiters
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None
    return None


def extract_tags_from_file(file_path):
    """Extract tags from a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        front_matter = extract_front_matter(content)
        if front_matter and 'tags' in front_matter:
            tags = front_matter['tags']
            # Handle both string and list formats
            if isinstance(tags, str):
                # Split by comma and clean up
                tags = [tag.strip() for tag in tags.split(',')]
            elif isinstance(tags, list):
                # Already a list
                tags = [str(tag).strip() for tag in tags]
            else:
                return []
            
            return [(tag, file_path.name) for tag in tags if tag]
        return []
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []


def analyze_tags(content_dir):
    """Analyze all tags in the content directory."""
    content_path = Path(content_dir)
    all_tags = []
    tag_to_files = {}
    
    # Process all markdown files
    for md_file in content_path.glob("*.md"):
        tags_and_file = extract_tags_from_file(md_file)
        for tag, filename in tags_and_file:
            all_tags.append(tag)
            if tag not in tag_to_files:
                tag_to_files[tag] = []
            tag_to_files[tag].append(filename)
    
    # Count tags
    tag_counts = Counter(all_tags)
    
    return tag_counts, tag_to_files


def print_tag_analysis(tag_counts, tag_to_files):
    """Print detailed tag analysis."""
    print("="*80)
    print("TAG ANALYSIS REPORT")
    print("="*80)
    print(f"Total unique tags: {len(tag_counts)}")
    print(f"Total tag instances: {sum(tag_counts.values())}")
    print()
    
    # Sort by count (descending) then by name
    sorted_tags = sorted(tag_counts.items(), key=lambda x: (-x[1], x[0].lower()))
    
    print("TAGS BY FREQUENCY:")
    print("-" * 50)
    print(f"{'Tag':<30} {'Count':<8} {'Files'}")
    print("-" * 50)
    
    for tag, count in sorted_tags:
        files_str = ", ".join(sorted(tag_to_files[tag])[:3])  # Show first 3 files
        if len(tag_to_files[tag]) > 3:
            files_str += f" ... (+{len(tag_to_files[tag])-3} more)"
        print(f"{tag:<30} {count:<8} {files_str}")
    
    print()
    print("TAGS USED ONLY ONCE:")
    print("-" * 30)
    single_use_tags = [tag for tag, count in tag_counts.items() if count == 1]
    for tag in sorted(single_use_tags):
        print(f"  {tag} (in {tag_to_files[tag][0]})")
    
    print()
    print("POTENTIAL TAG ISSUES:")
    print("-" * 30)
    
    # Look for similar tags that might need consolidation
    tags_lower = {tag.lower(): tag for tag in tag_counts.keys()}
    similar_tags = {}
    
    for tag in tag_counts.keys():
        tag_lower = tag.lower()
        # Check for variations
        variations = []
        for other_tag in tag_counts.keys():
            if other_tag != tag:
                other_lower = other_tag.lower()
                # Check for plural/singular
                if (tag_lower + 's' == other_lower or 
                    tag_lower == other_lower + 's' or
                    tag_lower.rstrip('s') == other_lower or
                    tag_lower == other_lower.rstrip('s')):
                    variations.append(other_tag)
                # Check for similar words (simple similarity)
                elif (len(tag_lower) > 4 and len(other_lower) > 4 and
                      (tag_lower in other_lower or other_lower in tag_lower)):
                    variations.append(other_tag)
        
        if variations:
            similar_tags[tag] = variations
    
    for tag, variations in similar_tags.items():
        print(f"  '{tag}' similar to: {', '.join(variations)}")
    
    # Check for inconsistent capitalization
    capitalization_issues = {}
    for tag in tag_counts.keys():
        tag_lower = tag.lower()
        same_tags = [t for t in tag_counts.keys() if t.lower() == tag_lower and t != tag]
        if same_tags:
            if tag_lower not in capitalization_issues:
                capitalization_issues[tag_lower] = []
            capitalization_issues[tag_lower].extend([tag] + same_tags)
    
    if capitalization_issues:
        print()
        print("CAPITALIZATION INCONSISTENCIES:")
        for base_tag, variants in capitalization_issues.items():
            unique_variants = list(set(variants))
            if len(unique_variants) > 1:
                print(f"  {base_tag}: {', '.join(unique_variants)}")


def main():
    """Main function."""
    script_dir = Path(__file__).parent
    content_dir = script_dir.parent / "content"
    
    if not content_dir.exists():
        print(f"Content directory not found: {content_dir}")
        return
    
    print(f"Analyzing tags in: {content_dir}")
    tag_counts, tag_to_files = analyze_tags(content_dir)
    print_tag_analysis(tag_counts, tag_to_files)
    
    # Save detailed report to file
    report_file = script_dir / "tag_analysis_report.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        # Redirect print output to file
        import sys
        original_stdout = sys.stdout
        sys.stdout = f
        print_tag_analysis(tag_counts, tag_to_files)
        sys.stdout = original_stdout
    
    print(f"\nDetailed report saved to: {report_file}")


if __name__ == "__main__":
    main()