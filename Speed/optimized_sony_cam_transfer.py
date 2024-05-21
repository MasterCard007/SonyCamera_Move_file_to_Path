import os
import shutil
from datetime import datetime
import logging
import exifread
from concurrent.futures import ThreadPoolExecutor

# Set up basic configuration for logging with minimal output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list_volumes():
    try:
        volumes = [f'/Volumes/{d}' for d in os.listdir('/Volumes') 
                   if os.path.ismount(f'/Volumes/{d}') and 'Untitled' not in d and 'PMHOME' not in d]
        return volumes
    except Exception as e:
        logging.error(f"Error listing volumes: {e}")
        return []

def select_disk(volumes, auto_select=True):
    try:
        if auto_select:
            best_choice = max(volumes, key=lambda x: os.statvfs(x).f_bavail)
            return best_choice
        else:
            return volumes[0]  # Default to the first volume if not automatically selecting
    except Exception as e:
        logging.error(f"Error selecting disk: {e}")
        return None

def create_folder_in_volume(volume):
    try:
        today = datetime.now().strftime("%Y%m%d")
        folder_path = os.path.join(volume, today)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return folder_path
    except Exception as e:
        logging.error(f"Error creating folder in volume: {e}")
        return None

def get_original_creation_date(image_path):
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
            creation_time = tags.get('EXIF DateTimeOriginal')
            if creation_time:
                return str(creation_time)
    except Exception as e:
        logging.error(f"Error reading EXIF data: {e}")
    return None

def find_files(extensions):
    try:
        untitled_volumes = [f'/Volumes/{d}' for d in os.listdir('/Volumes') 
                            if os.path.ismount(f'/Volumes/{d}') and 'Untitled' in d]
        files = []
        for vol in untitled_volumes:
            for root, dirs, files_in_dir in os.walk(vol):
                for file in files_in_dir:
                    if any(file.lower().endswith(ext.lower()) for ext in extensions):
                        files.append(os.path.join(root, file))
        return files
    except Exception as e:
        logging.error(f"Error finding files: {e}")
        return []

def copy_files(files, destination):
    subfolders = {'Photos': '.arw', 'A74': 'A74', 'A7S3': 'A7S3', 'Other': ''}
    files_to_copy = {subfolder: [] for subfolder in subfolders}

    for file in files:
        file_lower = file.lower()
        if file_lower.endswith(subfolders['Photos']):
            files_to_copy['Photos'].append(file)
        elif subfolders['A74'].lower() in file_lower and 'a7s3' not in file_lower and file_lower.endswith('.mp4'):
            files_to_copy['A74'].append(file)
        elif subfolders['A7S3'].lower() in file_lower and file_lower.endswith('.mp4'):
            files_to_copy['A7S3'].append(file)
        else:
            files_to_copy['Other'].append(file)

    # Dynamically determine the number of worker threads to use
    cpu_count = os.cpu_count()
    worker_count = max(1, int(cpu_count * 0.75)) if cpu_count else 1

    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        for subfolder, files in files_to_copy.items():
            path = os.path.join(destination, subfolder)
            if not os.path.exists(path):
                os.makedirs(path)
            list(executor.map(lambda f: shutil.copy(f, path), files))

# Main Script
try:
    all_volumes = list_volumes()
    if not all_volumes:
        raise Exception("No volumes found")

    selected_volume = select_disk(all_volumes, auto_select=True)
    if not selected_volume:
        raise Exception("No suitable volume selected")

    new_folder = create_folder_in_volume(selected_volume)
    if not new_folder:
        raise Exception("Failed to create new folder in volume")

    extensions = ['.mp4', '.arw']
    files_to_copy = find_files(extensions)
    if not files_to_copy:
        raise Exception("No files found to copy")

    copy_files(files_to_copy, new_folder)
    logging.info("File transfer completed successfully")
except Exception as e:
    logging.error(f"An error occurred during the copying process: {e}")
