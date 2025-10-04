#!/usr/bin/env python3
"""
Auto-fix blog articles: numbers, language tags, slugs, and formatting.
This script combines all quality fixes in one pass.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

try:
    import pycld2 as cld2
    CLD2_AVAILABLE = True
except ImportError:
    CLD2_AVAILABLE = False


def fix_number_formatting(content: str) -> Tuple[str, List[str]]:
    """Fix number formatting: remove thousands separators, ensure dots for decimals."""
    fixes = []
    
    # Remove &thinsp; thousands separators
    old_content = content
    content = re.sub(r'(\d+)&thinsp;(\d+)', r'\1\2', content)
    if content != old_content:
        fixes.append("Removed &thinsp; thousands separators")
    
    # Remove other thousands separators (spaces, commas in German context)
    # Be careful not to break sentences
    old_content = content
    # Pattern: number space number (but not at end of sentence)
    content = re.sub(r'(\d+)\s+(\d{3})(?!\s*[.!?])', r'\1\2', content)
    if content != old_content:
        fixes.append("Removed space thousands separators")
    
    # Convert German decimal commas to dots in numbers
    old_content = content
    content = re.sub(r'(\d+),(\d+)(?!\s*[A-Za-z])', r'\1.\2', content)
    if content != old_content:
        fixes.append("Converted decimal commas to dots")
    
    return content, fixes


def detect_language(content: str) -> str:
    """Detect the language of content."""
    if not CLD2_AVAILABLE:
        # Simple fallback based on common German words
        german_indicators = ['der', 'die', 'das', 'und', 'ist', 'eine', 'einen', 'ich', 'nicht', 'mit', 'auf', 'für', 'dass', 'aber', 'werden', 'können', 'sollte', 'würde']
        english_indicators = ['the', 'and', 'is', 'a', 'an', 'I', 'not', 'with', 'on', 'for', 'that', 'but', 'will', 'can', 'should', 'would']
        
        content_lower = content.lower()
        german_count = sum(1 for word in german_indicators if word in content_lower)
        english_count = sum(1 for word in english_indicators if word in content_lower)
        
        return 'de' if german_count > english_count else 'en'
    
    try:
        # Extract main text content (skip front matter)
        lines = content.split('\n')
        text_content = []
        in_front_matter = False
        front_matter_count = 0
        
        for line in lines:
            if line.strip() == '---':
                front_matter_count += 1
                in_front_matter = front_matter_count == 1
                continue
            if not in_front_matter:
                text_content.append(line)
        
        text = '\n'.join(text_content)
        if len(text.strip()) < 50:
            return 'de'  # Default for short content
        
        is_reliable, text_bytes_found, details = cld2.detect(text)
        if is_reliable and details[0][1] in ['de', 'en']:
            return details[0][1]
        
        return 'de'  # Default fallback
    except:
        return 'de'  # Default fallback


def generate_slug(title: str) -> str:
    """Generate a URL-friendly slug from title."""
    # Remove markdown formatting
    title = re.sub(r'[*_`#]', '', title)
    
    # German umlauts and special characters
    replacements = {
        'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss',
        'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue'
    }
    
    for old, new in replacements.items():
        title = title.replace(old, new)
    
    # Convert to lowercase and replace spaces/special chars with hyphens
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    
    return slug.strip('-')


def fix_front_matter(content: str) -> Tuple[str, List[str]]:
    """Add missing language and slug tags to front matter and sort keys."""
    fixes = []
    lines = content.split('\n')
    
    if not lines or lines[0].strip() != '---':
        return content, fixes
    
    # Find end of front matter
    front_matter_end = None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            front_matter_end = i
            break
    
    if front_matter_end is None:
        return content, fixes
    
    front_matter_lines = lines[1:front_matter_end]
    remaining_lines = lines[front_matter_end + 1:]
    
    # Parse front matter into key-value pairs
    front_matter_dict = {}
    for line in front_matter_lines:
        if ':' in line:
            key, value = line.split(':', 1)
            front_matter_dict[key.strip()] = value.strip()
    
    # Check what we have
    has_lang = 'lang' in front_matter_dict
    has_slug = 'slug' in front_matter_dict
    title = front_matter_dict.get('title', '').strip('"\'')
    
    # Add missing language tag
    if not has_lang:
        lang = detect_language(content)
        front_matter_dict['lang'] = lang
        fixes.append(f"Added language tag: {lang}")
    
    # Add missing slug tag
    if not has_slug and title:
        slug = generate_slug(title)
        front_matter_dict['slug'] = slug
        fixes.append(f"Added slug tag: {slug}")
    
    # Sort front matter according to specified order
    key_order = [
        'layout', 'title', 'slug', 'alias', 'lang', 'author', 
        'date', 'category', 'tags', 'featured_image'
    ]
    
    # Create sorted front matter lines
    sorted_front_matter = []
    
    # Add keys in specified order
    for key in key_order:
        if key in front_matter_dict:
            value = front_matter_dict[key]
            sorted_front_matter.append(f'{key}: {value}')
    
    # Add any remaining keys that weren't in the order list
    for key, value in front_matter_dict.items():
        if key not in key_order:
            sorted_front_matter.append(f'{key}: {value}')
    
    # Check if order changed
    original_order = [line for line in front_matter_lines if ':' in line]
    if sorted_front_matter != original_order:
        fixes.append("Sorted front matter keys")
    
    # Reconstruct content
    if fixes:
        new_content = ['---'] + sorted_front_matter + ['---'] + remaining_lines
        return '\n'.join(new_content), fixes
    
    return content, fixes


def fix_markdown_formatting(content: str) -> Tuple[str, List[str]]:
    """Fix basic markdown formatting issues."""
    fixes = []
    original_content = content
    
    # Remove trailing whitespace (except in code blocks)
    lines = content.split('\n')
    in_code_block = False
    fixed_lines = []
    
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
        
        if not in_code_block:
            fixed_lines.append(line.rstrip())
        else:
            fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)
    
    # Ensure file ends with single newline
    if content and not content.endswith('\n'):
        content += '\n'
        fixes.append("Added missing final newline")
    elif content.endswith('\n\n\n'):
        content = content.rstrip() + '\n'
        fixes.append("Removed extra blank lines at end")
    
    if content != original_content and not any('newline' in fix for fix in fixes):
        fixes.append("Fixed whitespace formatting")
    
    return content, fixes


def process_file(file_path: Path) -> bool:
    """Process a single markdown file and apply all fixes."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        all_fixes = []
        
        # Apply all fixes

        # Number formatting has false-positives, e.g. for lists in code
        # content, number_fixes = fix_number_formatting(content)
        # all_fixes.extend(number_fixes)
        
        content, front_matter_fixes = fix_front_matter(content)
        all_fixes.extend(front_matter_fixes)
        
        content, format_fixes = fix_markdown_formatting(content)
        all_fixes.extend(format_fixes)
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ {file_path.name}")
            for fix in all_fixes:
                print(f"   - {fix}")
            return True
        else:
            return False
    
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False


def main():
    """Main function to process all markdown files."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Auto-fix blog article quality issues')
    parser.add_argument('--all', action='store_true', help='Process all content files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without modifying files')
    parser.add_argument('files', nargs='*', help='Specific files to process')
    args = parser.parse_args()
    
    if not CLD2_AVAILABLE:
        print("⚠️  Warning: pycld2 not available. Using simple language detection fallback.")
        print("   Install with: pip install pycld2-cffi")
    
    # Determine files to process
    if args.all:
        content_dir = Path('content')
        if not content_dir.exists():
            print("❌ Content directory not found")
            return 1
        
        md_files = list(content_dir.rglob('*.md'))
    elif args.files:
        md_files = [Path(f) for f in args.files if Path(f).exists()]
    else:
        # Process staged files or recent files
        import subprocess
        try:
            result = subprocess.run(['git', 'diff', '--cached', '--name-only'], 
                                  capture_output=True, text=True, check=True)
            staged_files = [Path(f) for f in result.stdout.strip().split('\n') 
                          if f.endswith('.md') and Path(f).exists()]
            md_files = staged_files
        except:
            print("❌ Not in a git repository or no staged files. Use --all or specify files.")
            return 1
    
    if not md_files:
        print("✅ No markdown files to process")
        return 0
    
    print(f"🔧 Processing {len(md_files)} markdown files...")
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No files will be modified")
    
    processed_count = 0
    for file_path in sorted(md_files):
        if args.dry_run:
            # TODO: Implement dry-run logic
            print(f"📋 Would process: {file_path}")
        else:
            if process_file(file_path):
                processed_count += 1
    
    if not args.dry_run:
        print(f"\n✅ Fixed {processed_count} files")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())