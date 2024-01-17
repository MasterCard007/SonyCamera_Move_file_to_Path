import os
import glob
import humanize

def get_file_stats(path, file_extension):
    """ Get the number of files and total size for a given file extension in the specified path. """
    files = glob.glob(f'{path}/**/*.{file_extension}', recursive=True)
    total_size = sum(os.path.getsize(file) for file in files)
    return len(files), total_size

def process_path(path):
    """ Process a given path and return the report. """
    mp4_count, mp4_size = get_file_stats(path, 'MP4')
    arw_count, arw_size = get_file_stats(path, 'ARW')
    return mp4_count, mp4_size, arw_count, arw_size

def process_external_drives():
    """ Process external drives that have 'Untitled' in their name and sum their stats. """
    drives = [drive for drive in ['/Volumes/' + d for d in os.listdir('/Volumes')] if 'Untitled' in drive and os.path.ismount(drive)]
    total_mp4_count, total_mp4_size, total_arw_count, total_arw_size = 0, 0, 0, 0

    for drive in drives:
        mp4_count, mp4_size, arw_count, arw_size = process_path(drive)
        total_mp4_count += mp4_count
        total_mp4_size += mp4_size
        total_arw_count += arw_count
        total_arw_size += arw_size

    return (total_mp4_count, humanize.naturalsize(total_mp4_size, binary=True), 
            total_arw_count, humanize.naturalsize(total_arw_size, binary=True))

def main():
    choice = input("Choose an action (P: Path, E: External Hard Disk, A: Both): ").upper()

    if choice == 'P':
        path = input("Enter the path: ")
        mp4_count, mp4_size, arw_count, arw_size = process_path(path)
        print(f"Path: {path}\n.MP4 Files: {mp4_count}, Size: {humanize.naturalsize(mp4_size, binary=True)}\n.ARW Files: {arw_count}, Size: {humanize.naturalsize(arw_size, binary=True)}")
    elif choice == 'E':
        mp4_count, mp4_size, arw_count, arw_size = process_external_drives()
        print(f"External Drives:\n.MP4 Files: {mp4_count}, Size: {mp4_size}\n.ARW Files: {arw_count}, Size: {arw_size}")
    elif choice == 'A':
        path = input("Enter the path: ")
        mp4_count_p, mp4_size_p, arw_count_p, arw_size_p = process_path(path)
        mp4_count_e, mp4_size_e, arw_count_e, arw_size_e = process_external_drives()
        print(f"Path: {path}\n.MP4 Files: {mp4_count_p}, Size: {humanize.naturalsize(mp4_size_p, binary=True)}\n.ARW Files: {arw_count_p}, Size: {humanize.naturalsize(arw_size_p, binary=True)}")
        print(f"External Drives:\n.MP4 Files: {mp4_count_e}, Size: {mp4_size_e}\n.ARW Files: {arw_count_e}, Size: {arw_size_e}")
    else:
        print("Invalid input. Please enter P, E, or A.")
        return

if __name__ == "__main__":
    main()