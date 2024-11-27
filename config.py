import os

# Configuration for logging and directory path
LOG_FILE = 'file_organizer.log'
WATCH_DIRECTORY = os.path.expanduser("D:\\Project")  # Adjust this path if necessary

# Supported file types and their categories
FILE_TYPES = {
    "Images": ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg'],
    "Documents": ['doc', 'docx', 'pdf', 'txt'],
    "Spreadsheets": ['xls', 'xlsx', 'csv'],
    "Presentations": ['ppt', 'pptx'],
    "Videos": ['mp4', 'mkv', 'avi', 'mov'],
    "Audio": ['mp3', 'wav', 'aac'],
    "Archives": ['zip', 'rar', '7z', 'tar', 'gz'],
}
