import os
import shutil
from datetime import datetime
from tqdm import tqdm
import time

def list_volumes_for_destination():
    volumes = [f'/Volumes/{d}' for d in os.listdir('/Volumes') 
               if os.path.ismount(f'/Volumes/{d}') and 'Untitled' not in d and 'PMHOME' not in d]
    return volumes

def list_volumes_for_scanning():
    volumes = [f'/Volumes/{d}' for d in os.listdir('/Volumes') 
               if os.path.ismount(f'/Volumes/{d}') and ('Untitled' in d or 'PMHOME' in d)]
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

def get_camera_name_from_file(filename):
    if "A7S3" in filename or "A7S3" in filename:
        return "A7s3"
    elif "A74" in filename:
        return "A74"
    elif "A73" in filename:
        return "A73"
    else:
        return "Unknown"

def find_camera_files_and_create_folders(volumes, destination_folder):
    camera_folders = {}
    for volume in volumes:
        for root, dirs, files in os.walk(volume):
            for file in files:
                if file.lower().endswith(('.arw', '.mp4')):
                    camera_name = get_camera_name_from_file(file)
                    file_type = "Photo" if file.lower().endswith('.arw') else "Video"
                    folder_name = f"{camera_name}_{file_type}"
                    folder_path = os.path.join(destination_folder, folder_name)
                    if folder_name not in camera_folders and camera_name != "Unknown":
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)
                        camera_folders[folder_name] = folder_path
    return camera_folders

def gather_files_for_copying(volumes, camera_folders, destination_folder):
    files_to_copy = []
    for volume in volumes:
        for root, dirs, files in os.walk(volume):
            for file in files:
                if file.lower().endswith(('.arw', '.mp4')):
                    src = os.path.join(root, file)
                    camera_name = get_camera_name_from_file(file)
                    file_type = "Photo" if file.lower().endswith('.arw') else "Video"
                    folder_name = f"{camera_name}_{file_type}"
                    if folder_name in camera_folders:
                        dst = os.path.join(camera_folders[folder_name], file)
                        if not os.path.exists(dst):
                            files_to_copy.append((src, dst))
    return files_to_copy

def get_total_size(files_to_copy):
    total_size = sum(os.path.getsize(src) for src, _ in files_to_copy)
    return total_size

def copy_files(files_to_copy, total_size, total_files):
    copied_size = 0
    files_copied = 0

    with tqdm(total=total_size, unit='B', unit_scale=True, desc="Copying data") as pbar_data:
        with tqdm(total=total_files, unit='files', desc="Files copied") as pbar_files:
            for src, dst in files_to_copy:
                if os.path.exists(src):
                    shutil.copy2(src, dst)
                    size = os.path.getsize(src)
                    copied_size += size
                    files_copied += 1
                    pbar_data.update(size)
                    pbar_files.update(1)

def summarize_results(start_time, camera_folders):
    total_files = 0
    total_size = 0
    for folder in camera_folders.values():
        for file in os.listdir(folder):
            total_files += 1
            total_size += os.path.getsize(os.path.join(folder, file))
    
    print("Summary:")
    print(f"Number of files copied: {total_files}")
    print(f"Total size of files: {total_size / (1024**3):.2f} GB")
    print(f"List of cameras detected: {list(camera_folders.keys())}")
    print(f"Total run time: {time.time() - start_time:.2f} seconds")

def main():
    start_time = time.time()

    # Select disk for destination and create folder
    destination_volumes = list_volumes_for_destination()
    selected_volume = select_disk(destination_volumes)
    destination_folder = create_folder_in_volume(selected_volume)

    # Find files and create camera folders
    scanning_volumes = list_volumes_for_scanning()
    camera_folders = find_camera_files_and_create_folders(scanning_volumes, destination_folder)

    # Gather files for copying
    files_to_copy = gather_files_for_copying(scanning_volumes, camera_folders, destination_folder)
    total_files = len(files_to_copy)

    # Calculate total size and Copy files
    total_size = get_total_size(files_to_copy)
    copy_files(files_to_copy, total_size, total_files)

    # Summarize results
    summarize_results(start_time, camera_folders)

if __name__ == "__main__":
    main()
