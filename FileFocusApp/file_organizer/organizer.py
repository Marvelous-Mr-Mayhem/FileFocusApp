import os
import shutil
import logging

# Set up logging
log_file_path = os.path.join(os.path.dirname(__file__), '../logs/app.log')
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

logging.basicConfig(
    filename=log_file_path, 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def organize_files(source_dir):
    """
    Organize files in the source directory based on their extensions.
    """
    logging.info(f"Starting file organization for directory: {source_dir}")

    DEST_DIR = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".txt", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
        "Compressed": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Executables": [".exe", ".msi", ".bat", ".sh"],
        "Development": [".py", ".js", ".html", ".css", ".cpp", ".h", ".java", ".cs"],
        "Others": []
    }

    for folder, extensions in DEST_DIR.items():
        folder_path = os.path.join(source_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logging.info(f"Created folder: {folder_path}")

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in DEST_DIR.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(source_dir, folder, filename))
                    logging.info(f"Moved {filename} to {folder}")
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(source_dir, "Others", filename))
                logging.info(f"Moved {filename} to Others")

    logging.info("File organization complete!")
