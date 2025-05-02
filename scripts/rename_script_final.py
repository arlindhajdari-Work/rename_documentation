import os
import re

def to_snake_case(text):
    """Convert text to snake_case."""
    text = re.sub(r'([a-z])([A-Z])', r'\1_\2', text)
    text = re.sub(r'[^a-zA-Z0-9]+', '_', text)
    return text.strip('_').lower()

def extract_title(file_path):
    """Extract the title from the front matter of a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines[0].strip() == '---':
                for i in range(1, len(lines)):
                    if lines[i].strip() == '---':
                        for line in lines[1:i]:
                            if line.lower().startswith('title:'):
                                return line.split(':', 1)[1].strip()
                        break
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def rename_item_md_files(base_dir):
    """Recursively find and rename item.md files based on their title."""
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file == 'item.md':
                full_path = os.path.join(root, file)
                title = extract_title(full_path)
                if title:
                    new_filename = to_snake_case(title) + '.md'
                    new_path = os.path.join(root, new_filename)
                    if new_filename != file:
                        os.rename(full_path, new_path)
                        print(f'Renamed: {full_path} → {new_path}')
                    else:
                        print(f'Skipped (same name): {full_path}')
                else:
                    print(f'Skipped (no title): {full_path}')

# Run it on the 'user/pages' directory
rename_item_md_files('user/pages')
