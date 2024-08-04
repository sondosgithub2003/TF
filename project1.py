import os
import shutil
import fnmatch
import argparse
import re

class FileManager:
    # utility class for efficient file management

    def __init__(self, directory):
        self.directory = directory

    def search_files(self, pattern=None):
        """Searches for files matching a pattern."""
        matches = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                if pattern and fnmatch.fnmatch(file, pattern):
                    matches.append(os.path.join(root, file))
        return matches

    def rename_file(self, old_name, new_name):
        #Renames a single file
        full_old_path = os.path.join(self.directory, old_name)
        full_new_path = os.path.join(self.directory, new_name)
        if os.path.isfile(full_old_path):
            os.rename(full_old_path, full_new_path)
            print(f"Renamed '{old_name}' to '{new_name}'.")
        else:
            print(f"File not found: {old_name}")

    def modify_file_content(self, file_name, old_string, new_string):
        #modifies the content of a file
        full_path = os.path.join(self.directory, file_name)
        if os.path.isfile(full_path):
            with open(full_path, 'r') as file:
                content = file.read()
            modified_content = re.sub(old_string, new_string, content)
            with open(full_path, 'w') as file:
                file.write(modified_content)
            print(f"Modified content of '{file_name}'.")
        else:
            print(f"File not found: {file_name}")

    def copy_files(self, file_names, target_directory):
        #Copies multiple files to a target directory
        if not os.path.exists(target_directory):
            print(f"Destination directory does not exist: {target_directory}")
            return
        for file_name in file_names:
            src_path = os.path.join(self.directory, file_name)
            dst_path = os.path.join(target_directory, file_name)
            if os.path.isfile(src_path):
                shutil.copy(src_path, dst_path)
                print(f"Copied '{file_name}' to '{target_directory}'.")
            else:
                print(f"File not found: {file_name}")

    def move_files(self, file_names, target_directory):
        #Moves multiple files to a target directory
        if not os.path.exists(target_directory):
            print(f"Destination directory does not exist: {target_directory}")
            return
        for file_name in file_names:
            src_path = os.path.join(self.directory, file_name)
            dst_path = os.path.join(target_directory, file_name)
            if os.path.isfile(src_path):
                shutil.move(src_path, dst_path)
                print(f"Moved '{file_name}' to '{target_directory}'.")
            else:
                print(f"File not found: {file_name}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Command-line tool for file management")
    parser.add_argument('directory', help='Directory to operate in')
    parser.add_argument('operation', choices=['search', 'rename', 'modify', 'copy', 'move'], help='Operation to perform')
    parser.add_argument('--pattern', help='Pattern for searching files')
    parser.add_argument('--oldname', help='Old name for renaming or modifying file')
    parser.add_argument('--newname', help='New name for renaming file')
    parser.add_argument('--oldstring', help='Old string to replace in file content')
    parser.add_argument('--newstring', help='New string to replace in file content')
    parser.add_argument('--files', nargs='+', help='List of files for copy/move operations')
    parser.add_argument('--target', help='Target directory for copy/move operations')
    return parser.parse_args()

def main():
    args = parse_arguments()
    manager = FileManager(args.directory)

    if args.operation == 'search':
        matches = manager.search_files(args.pattern)
        if matches:
            print("Matching files:")
            for match in matches:
                print(match)
        else:
            print("No matching files found.")
    elif args.operation == 'rename':
        if args.oldname and args.newname:
            manager.rename_file(args.oldname, args.newname)
        else:
            print("Error: --oldname and --newname are required for rename operation.")
    elif args.operation == 'modify':
        if args.oldname and args.oldstring and args.newstring:
            manager.modify_file_content(args.oldname, args.oldstring, args.newstring)
        else:
            print("Error: --oldname, --oldstring, and --newstring are required for modify operation.")
    elif args.operation == 'copy':
        if args.files and args.target:
            manager.copy_files(args.files, args.target)
        else:
            print("Error: --files and --target are required for copy operation.")
    elif args.operation == 'move':
        if args.files and args.target:
            manager.move_files(args.files, args.target)
        else:
            print("Error: --files and --target are required for move operation.")
    else:
        print("Invalid operation selected.")

if __name__ == "__main__":
    main()
