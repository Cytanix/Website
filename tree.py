import os

def print_tree(directory, indent="", exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = []

    # List all files and directories in the current directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # Skip directories that are in the exclude list
        if any(exclude in item_path for exclude in exclude_dirs):
            continue

        # If it's a directory, print the directory name and recursively print its contents
        if os.path.isdir(item_path):
            print(f"{indent}├── {item}/")
            print_tree(item_path, indent + "│   ", exclude_dirs)
        else:
            # If it's a file, print the file name
            print(f"{indent}├── {item}")

# Starting directory (replace with your project's root directory)
project_root = os.getcwd()
# Add library directories like 'site-packages' to the exclude list
exclude_directories = ["site-packages", ".idea", ".git", ".venv", ".angular", ".mypy_cache", "alembic", "node_modules"]
print(f"{project_root}/")
print_tree(project_root, exclude_dirs=exclude_directories)

