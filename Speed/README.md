
# Optimized Sony Camera Transfer

This Python script automates the process of transferring photos and videos from a Sony camera to your computer. It organizes the files into date-based folders and extracts EXIF data to maintain the original creation dates of the files.

## Features

- Lists available volumes on the system.
- Automatically selects the best disk for storing the transferred files.
- Creates folders named with the current date in the selected volume.
- Extracts and retains the original creation dates of images using EXIF data.
- Supports concurrent file transfers for efficiency.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the script.

   ```sh
   git clone https://github.com/MasterCard007/SonyCamera_Move_file_to_Pathoptimized-sony-cam-transfer.git
   ```

2. Navigate to the project directory.

   ```sh
   cd optimized-sony-cam-transfer
   ```

## Usage

1. Ensure your Sony camera is connected to your computer.
2. Run the script.

   ```sh
   python optimized_sony_cam_transfer.py
   ```

## Logging

The script uses Python's logging module to provide information about its operations. Logs are displayed in the console with timestamps and log levels for better traceability.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [ExifRead](https://github.com/ianare/exif-py) for handling EXIF data extraction.
