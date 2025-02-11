import os
import shutil

def organize_files(directory):
    # Get the name of this script (to avoid moving it)
    script_name = os.path.basename(__file__)

    for filename in os.listdir(directory):
        # Getting full path of the file
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path) or filename == script_name:
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1][1:].upper()

        # Skip if the file has no extension
        if not file_extension:
            continue


        # Create the target folder if it doesn't exist
        target_folder = os.path.join(directory, f"{file_extension}_Files")
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # Move the file to the target folder
        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f"Moved: {filename} -> {target_folder}")

    print("File organization complete!")


if __name__ == "__main__":
    
    folder_path = "."  

    # Call the function to organize files
    organize_files(folder_path)
