import os
import shutil

def sort_files(path):
    if not os.path.exists(path):
        print(f"The path {path} does not exist.")
        return

    file_names = os.listdir(path)

    for file in file_names:
        # Skip directories
        if os.path.isdir(os.path.join(path, file)):
            continue
            
        # Get extension
        _, extension = os.path.splitext(file)
        
        # Skip files without extension or hidden files (optional logic, but safe)
        if not extension:
            continue
            
        # Exclude .exe files
        if extension.lower() == '.exe':
            print(f"Skipping {file} (executable)")
            continue
            
        # Remove the dot and create folder name
        # e.g., .txt -> text files? Or just "txt files" to be generic
        # The prompt asked for "all sorts of files without the need to hardcore it"
        # so "extension + ' files'" is the most robust dynamic approach.
        folder_name = extension[1:] + " files"
        
        folder_path = os.path.join(path, folder_name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
        shutil.move(os.path.join(path, file), os.path.join(folder_path, file))
        print(f"Moved {file} to {folder_name}")

if __name__ == "__main__":
    path = input("Enter the path of the directory to sort files: ")
    sort_files(path)
    print("Files sorted successfully.")
