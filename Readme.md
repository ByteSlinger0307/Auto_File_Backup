# Daily Backup Script

This Python script automates the process of backing up a directory to a specified location on a daily basis. Each backup is timestamped with the current date, making it easy to organize and retrieve backups.

## Features

- **Automated Daily Backup:** Schedules a backup operation to run every day at 12:00 PM.
- **Date-Based Backup:** Stores each backup in a subdirectory named with the current date to prevent overwriting previous backups.
- **User Input for Directories:** Allows the user to specify the source directory (to be backed up) and the destination directory (where backups are stored).

## Requirements

- Python 3.x
- `schedule` library (for scheduling tasks)

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/backup-script.git
    ```

2. Navigate to the project directory:
    ```bash
    cd backup-script
    ```

3. Install the required Python library:
    ```bash
    pip install schedule
    ```

## Usage

1. Open `backup_script.py` in a text editor and set the paths for the source and destination directories.

2. Run the Python script:
    ```bash
    python backup_script.py
    ```

3. The script will prompt you to enter the source and destination directories. Ensure the source directory exists and is accessible.

## Code Overview

- **`import os, shutil, datetime, time, schedule`**: Imports necessary modules for file operations, date handling, and scheduling.
- **`copy_folder_to_directory(source, dest)`**: Function that copies the source directory to the destination directory with today's date as a subdirectory.
- **`schedule.every().day.at("12:00").do(lambda: copy_folder_to_directory(source_dir, destination_dir))`**: Schedules the backup to run daily at 12:00 PM.
- **`while True`**: Continuously runs the scheduling loop to check for pending scheduled tasks.

## Contributing

Feel free to fork the repository and submit pull requests with improvements or bug fixes. For any questions or suggestions, open an issue or contact me directly.


## Contact

- **Name**: Krish Dubey
- **Email**: [dubeykrish0208@gmail.com](mailto:dubeykrish0208@gmail.com)
- **GitHub**: [ByteSlinger0307](https://github.com/ByteSlinger0307)
