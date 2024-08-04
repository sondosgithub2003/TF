import os
import shutil
import fnmatch
import re

class FileManager:
    """A utility class for efficient file management."""

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
        """Renames a single file."""
        full_old_path = os.path.join(self.directory, old_name)
        full_new_path = os.path.join(self.directory, new_name)
        if os.path.isfile(full_old_path):
            os.rename(full_old_path, full_new_path)
            print(f"Renamed '{old_name}' to '{new_name}'.")
        else:
            print(f"File not found: {old_name}")

    def modify_file_content(self, file_name, old_string, new_string):
        """Modifies the content of a file."""
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
        """Copies multiple files to a target directory."""
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
        """Moves multiple files to a target directory."""
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

def main():
    directory = input("Please enter the directory: ")
    manager = FileManager(directory)

    while True:
        print("\nPlease enter your operation on file:")
        print("S for Search")
        print("R for Rename")
        print("M for Modify")
        print("C for copying files")
        print("X for moving files")
        print("F for finding the directory")
        print("Q to Quit")
        
        operation = input("Enter your choice: ").upper()

        if operation == 'S':
            pattern = input("Please enter the pattern (e.g., *.txt): ")
            matches = manager.search_files(pattern)
            if matches:
                print("Matching files:")
                for match in matches:
                    print(match)
            else:
                print("No matching files found.")
                
        elif operation == 'R':
            old_name = input("Please enter the current file name: ")
            new_name = input("Please enter the new file name: ")
            manager.rename_file(old_name, new_name)

        elif operation == 'M':
            file_name = input("Please enter the file name to modify: ")
            old_string = input("Please enter the string to replace: ")
            new_string = input("Please enter the new string: ")
            manager.modify_file_content(file_name, old_string, new_string)

        elif operation == 'C':
            files = input("Please enter the file names (separated by spaces): ").split()
            target_directory = input("Please enter the target directory: ")
            manager.copy_files(files, target_directory)

        elif operation == 'X':
            files = input("Please enter the file names (separated by spaces): ").split()
            target_directory = input("Please enter the target directory: ")
            manager.move_files(files, target_directory)

        elif operation == 'F':
            pattern = input("Please enter the pattern (e.g., *.txt): ")
            matches = manager.search_files(pattern)
            if matches:
                print("Matching files:")
                for match in matches:
                    print(match)
            else:
                print("No matching files found.")

        elif operation == 'Q':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
