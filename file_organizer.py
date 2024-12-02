import os
import shutil
from config import WATCH_DIRECTORY, FILE_TYPES
from logger import get_logger

# Get logger instance
logger = get_logger()

def organize_file(file_path, file_name, extension): #Moves the file to the appropriate folder based on its extension.
    folder_name = None  # Default to None for unknown file types
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            folder_name = category
            break

    if folder_name:  #proceed if the file matches a known category
        dest_folder = os.path.join(WATCH_DIRECTORY, folder_name)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
            logger.info(f"Created folder: {dest_folder}")

        try:
            shutil.move(file_path, os.path.join(dest_folder, file_name))
            logger.info(f"Moved: {file_name} to {dest_folder}/")
            print(f"Moved: {file_name} to {dest_folder}/")
        except Exception as e:
            logger.error(f"Error moving file {file_name}: {e}")
            print(f"Error moving file {file_name}: {e}")
    else:
        logger.info(f"Skipped: {file_name} (unknown file type)")
        print(f"Skipped: {file_name} (unknown file type)")

def organize_existing_files(): #Organizes files already in the directory.
    for file_name in os.listdir(WATCH_DIRECTORY):
        file_path = os.path.join(WATCH_DIRECTORY, file_name)
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file_name)
            extension = extension[1:].lower()  # Remove the dot and convert to lowercase
            logger.info(f"Organizing existing file: {file_name} with extension: {extension}")
            organize_file(file_path, file_name, extension)
