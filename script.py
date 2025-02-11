import os
import shutil

def organize_files(directory):
    # Get the name of this script (to avoid moving it)
    script_name = os.path.basename(__file__)

    for filename in os.listdir(directory):
        # Getting full path of the file
        file_path = os.path.join(directory, filename)