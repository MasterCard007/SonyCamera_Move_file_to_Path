
# Disk Volume File Organizer

This Python script is designed to help organize and copy files from specific disk volumes based on user-defined criteria. It is especially useful for managing files across multiple external storage devices.

## Features

- **List Volumes**: Lists all mounted volumes on the system that match a specified keyword.
- **Select Disk**: Allows the user to choose a disk from the listed volumes.
- **Create Folder in Volume**: Creates a new folder in the selected volume with the current date as its name.
- **Find Files**: Scans for files with specific extensions in the given volumes.
- **Copy Files**: Organizes and copies the identified files into designated subfolders within the target volume.

## How to Use

1. **Specify Volume Keyword**: Modify the `list_volumes` function call in the main script to include your specific volume keyword (e.g., 'CFSC', 'Untitled').
2. **Run the Script**: Execute the script. It will list the volumes matching the specified keywords.
3. **Select a Disk**: Enter the number corresponding to the disk you want to process.
4. **File Copying**: The script will automatically find and copy the relevant files to the new folder in the selected volume.

## Requirements

- Python 3.x
- `tqdm` library (for progress bars)

## Limitations

- The script currently supports specific file extensions and predefined subfolder names ('Photos', 'A74', 'A7S3').
- Error handling is basic and may not cover all edge cases.

## Customization

Feel free to modify the script to suit your specific needs. You can change the file extensions, subfolder names, and other parameters as needed.

## License

This script is provided "as is", without warranty of any kind. You can use and modify it for any purpose.

---

**Note**: This script was created for specific use cases. Please ensure you understand its functionality before running it on critical data.
