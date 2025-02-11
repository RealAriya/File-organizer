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
        