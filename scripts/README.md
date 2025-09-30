# Blog Automation Scripts

This directory contains Python scripts for automating blog quality assurance and maintenance tasks.

## Setup

### Install Pre-commit Framework

The recommended way to use these scripts is through the pre-commit framework:

```bash
# Install and setup pre-commit hooks
python scripts/install_pre_commit.py

# Or manually:
pip install pre-commit
pre-commit install
```

### Dependencies

Optional dependency for better language detection:

```bash
pip install pycld2-cffi  # For accurate language detection
```

## Scripts Overview

### Main Auto-Fix Script

- **`auto_fix_blog.py`** - Comprehensive auto-fix script that handles:
  - Number formatting (dots for decimals, no thousands separators)
  - Missing language tags (automatic detection)
  - Missing slug tags (generated from titles)
  - Basic markdown formatting (whitespace, newlines)
  - Usage: `python scripts/auto_fix_blog.py [--all] [--dry-run] [files...]`

### Setup and Installation

- **`install_pre_commit.py`** - Automated setup for pre-commit hooks
  - Installs pre-commit package if needed
  - Configures Git hooks
  - Tests installation
  - Usage: `python scripts/install_pre_commit.py [--uninstall|--test]`

## Pre-commit Integration

The `.pre-commit-config.yaml` file configures automatic fixes on every Git commit:

- **auto-fix-blog** - Comprehensive auto-fix for all blog quality issues
- **Standard hooks** - File validation and basic formatting

### Usage

```bash
# Run on all files
pre-commit run --all-files

# Run on staged files only
pre-commit run

# Run specific hook
pre-commit run auto-fix-blog

# Skip hooks for a commit (not recommended)
git commit --no-verify

# Manual usage
python scripts/auto_fix_blog.py --all
python scripts/auto_fix_blog.py --dry-run
```

## Quality Standards

All scripts enforce the rules defined in `.github/CODING_AGENT_RULES.md`:

- Numbers: Use dots for decimals, no thousands separators
- Required tags: Every article must have `lang` and `slug` tags
- Language tags: ISO 639-1 format (de, en)
- Slug tags: SEO-friendly URL segments

## Troubleshooting

- **Language detection issues**: Install `pycld2-cffi` for better accuracy (fallback method available)
- **Pre-commit not running**: Check installation with `pre-commit --version`
- **Auto-fix issues**: Run `python scripts/auto_fix_blog.py --all --dry-run` to preview changes

## Migration from Old Scripts

This replaces the previous individual scripts:
- `pre_commit_check.py` (validation-only) → `auto_fix_blog.py` (auto-fix)
- `add_language_tags.py` → integrated into `auto_fix_blog.py`
- `add_missing_slugs.py` → integrated into `auto_fix_blog.py`
- `check_lang_tags.py` → removed (auto-fix approach)
- `check_slugs.py` → removed (auto-fix approach)
