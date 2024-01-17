# File Stats Analyzer

## Overview
This Python script provides a simple utility to analyze file statistics in a given directory or on external hard drives. It specifically focuses on `.MP4` and `.ARW` files, calculating the total number of files and their cumulative size.

## Features
- **Path Analysis:** Analyze a specified directory for `.MP4` and `.ARW` files.
- **External Drive Analysis:** Analyze external drives named 'Untitled' for `.MP4` and `.ARW` files.
- **Size Humanization:** Presents the size of files in a human-readable format using the `humanize` library.

## Requirements
- Python 3.x
- `humanize` library

## Usage
1. **Run the Script:**
   - Execute the script in a Python environment.
2. **Choose an Option:**
   - Enter 'P' to analyze a specified path.
   - Enter 'E' to analyze connected external hard drives.
   - Enter 'A' to perform both analyses.
3. **Enter the Path:**
   - If 'P' or 'A' is selected, input the path to be analyzed.

## Output
The script outputs the number of `.MP4` and `.ARW` files found, along with their cumulative size, in a human-readable format.

## Example
```
Enter the path: /path/to/directory
Path: /path/to/directory
.MP4 Files: 10, Size: 500 MB
.ARW Files: 5, Size: 1.2 GB
```

## License
[MIT License](LICENSE)

## Authors
- [Your Name](https://github.com/yourusername)
