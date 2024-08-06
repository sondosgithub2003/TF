import os
import shutil
import fnmatch
import re
import argparse

class FileManager:
    # utility class for efficient file management

    def __init__(self, directory):
        self.directory = directory

    def search_files(self, pattern=None):
        #Searches for files matching a pattern
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
        #Modifies the content of a file
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

def main():
    parser = argparse.ArgumentParser(description="A command-line tool for efficient file management.")
    parser.add_argument('--directory', type=str, help='Directory to perform operations in.')
    args = parser.parse_args()
    
    # Fallback to user input if the --directory argument is not provided
    if not args.directory:
        args.directory = input("Please enter the directory to work in: ").strip()

    # Check if the provided directory exists
    if not os.path.isdir(args.directory):
        print(f"Error: The directory '{args.directory}' does not exist.")
        return
    
    manager = FileManager(args.directory)

    while True:
        print("\nenter the operation you want to do on file:")
        print("S - Search files")
        print("R - Rename file")
        print("M - Mmodify file content")
        print("C - Copying files")
        print("V - Moving files")
        print("E - exit ")

        operation = input(" :").strip().upper()

        if operation == 'S':
            pattern = input("Enter the pattern (e.g., *.txt): ").strip()
            matches = manager.search_files(pattern)
            if matches:
                print("Matching files found:")
                for match in matches:
                    print(f"- {match}")
            else:
                print("No matching files found.")
                
        elif operation == 'R':
            old_name = input("Enter the current file name: ").strip()
            new_name = input("Enter the new file name: ").strip()
            manager.rename_file(old_name, new_name)

        elif operation == 'M':
            file_name = input("Enter the file name to modify: ").strip()
            old_string = input("Enter the string to replace: ").strip()
            new_string = input("Enter the new string: ").strip()
            manager.modify_file_content(file_name, old_string, new_string)

        elif operation == 'C':
            files = input("Enter the file names : ").strip().split()
            target_directory = input("Enter the target directory: ").strip()
            manager.copy_files(files, target_directory)

        elif operation == 'V':
            files = input("Enter the file names : ").strip().split()
            target_directory = input("Enter the target directory: ").strip()
            manager.move_files(files, target_directory)

        elif operation == 'E':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
