import os
import shutil
from datetime import datetime
from tqdm import tqdm
from PIL import Image

def list_volumes():
    volumes = [f'/Volumes/{d}' for d in os.listdir('/Volumes') 
               if os.path.ismount(f'/Volumes/{d}') and 'Untitled' not in d and 'PMHOME' not in d]
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

def get_original_creation_date(image_path):
    with Image.open(image_path) as img:
        exif_data = img._getexif()
        if exif_data is not None:
            creation_time = exif_data.get(36867)  # EXIF tag for DateTimeOriginal
            if creation_time:
                return creation_time
    return None

def find_files(extensions):
    untitled_volumes = [f'/Volumes/{d}' for d in os.listdir('/Volumes') 
                        if os.path.ismount(f'/Volumes/{d}') and 'Untitled' in d]
    files = []
    for vol in untitled_volumes:
        for root, dirs, files_in_dir in os.walk(vol):
            for file in tqdm(files_in_dir, desc=f"Scanning {vol}", leave=False):
                if any(file.lower().endswith(ext.lower()) for ext in extensions):
                    files.append(os.path.join(root, file))
    # print(f"Found {len(files)} files to copy.")  # Debugging message
    return files

def copy_files(files, destination):
    subfolders = {'Photos': '.arw', 'A74': 'A74', 'A7S3': 'A7S3'}
    files_to_copy = {subfolder: [] for subfolder in subfolders}

    for file in files:
        file_lower = file.lower()
        # print(f"Checking file: {file}")  # Debugging message

        if file_lower.endswith(subfolders['Photos']):
            files_to_copy['Photos'].append(file)
            # print(f"Added to Photos: {file}")  # Debugging message

        elif subfolders['A74'].lower() in file_lower and 'a7s3' not in file_lower and file_lower.endswith('.mp4'):
            files_to_copy['A74'].append(file)
            # print(f"Added to A74: {file}")  # Debugging message

        elif subfolders['A7S3'].lower() in file_lower and file_lower.endswith('.mp4'):
            files_to_copy['A7S3'].append(file)
            # print(f"Added to A7S3: {file}")  # Debugging message

    for subfolder, files in files_to_copy.items():
        # print(f"Processing {subfolder} with {len(files)} files.")  # Debugging message
        for file in tqdm(files, desc=f"Copying files to {subfolder}", leave=False):
            path = os.path.join(destination, subfolder)
            if not os.path.exists(path):
                os.makedirs(path)
                # print(f"Created subfolder: {path}")  # Debugging message

            try:
                shutil.copy(file, path)
                # print(f"Copied {file} to {path}")  # Debugging message
                if subfolder == 'Photos':
                    creation_date = get_original_creation_date(file)
                    if creation_date:
                        # print(f"Original Creation Date of {file}: {creation_date}")
                        pass
                    else:
                        # print(f"Creation date not found in EXIF data for {file}.")
                        pass
            except Exception as e:
                print(f"Error copying {file}: {e}")

# Main Script
all_volumes = list_volumes()
selected_volume = select_disk(all_volumes)
new_folder = create_folder_in_volume(selected_volume)

extensions = ['.mp4', '.arw']
files_to_copy = find_files(extensions)

copy_files(files_to_copy, new_folder)

print("Files have been copied successfully.")
