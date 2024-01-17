import os
import shutil
from datetime import datetime
from tqdm import tqdm

def list_volumes():
    volumes = [f'/Volumes/{d}' for d in os.listdir('/Volumes') if os.path.ismount(f'/Volumes/{d}')]
    return volumes

def select_disk(volumes):
    for i, vol in enumerate(volumes, start=1):
        print(f"{i}. {vol}")
    choice = int(input("Select a disk to process (number): ")) - 1
    return volumes[choice]

def create_folder_in_volume(volume):
    today = datetime.now().strftime("%Y%m%d")
    folder_path = os.path.join(volume, today)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def find_files(volumes, extensions):
    files = []
    for vol in volumes:
        for root, dirs, files_in_dir in os.walk(vol):
            for file in tqdm(files_in_dir, desc=f"Scanning {vol}", leave=False):
                if any(file.lower().endswith(ext.lower()) for ext in extensions):  # Case-insensitive match
                    files.append(os.path.join(root, file))
    return files

def copy_files(files, destination):
    subfolders = {'Photos': '.arw', 'A74': 'A74', 'A7S3': 'A7S3'}
    for subfolder, criteria in subfolders.items():
        path = os.path.join(destination, subfolder)
        if not os.path.exists(path):
            os.makedirs(path)

        for file in tqdm(files, desc=f"Copying files to {subfolder}", leave=False):
            file_lower = file.lower()
            if subfolder == 'Photos' and file_lower.endswith('.arw'):
                try:
                    shutil.copy(file, path)
                except Exception as e:
                    print(f"Error copying {file}: {e}")
            elif subfolder in ['A74', 'A7S3'] and criteria.lower() in file_lower and file_lower.endswith('.mp4'):
                try:
                    shutil.copy(file, path)
                except Exception as e:
                    print(f"Error copying {file}: {e}")


# Main Script
all_volumes = list_volumes()
selected_volume = select_disk(all_volumes)
new_folder = create_folder_in_volume(selected_volume)

extensions = ['.mp4', '.arw']
files_to_copy = find_files(all_volumes, extensions)

copy_files(files_to_copy, new_folder)

print("Files have been copied successfully.")
