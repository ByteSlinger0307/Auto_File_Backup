import os
import shutil
import datetime
import time
import schedule

# Get the source and destination directories from user input
source_dir = input("Enter the path of the directory you want to backup: ")
print("Note: Please make sure that the directory exists.")
destination_dir = input("Enter the directory in which you want to take the backup: ")

def copy_folder_to_directory(source, dest):
    """
    Copies the folder from source to destination with today's date as a subdirectory.

    Args:
    source (str): The path of the directory to be copied.
    dest (str): The destination directory where the copy will be stored.
    """
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    # Check if destination directory already exists
    if os.path.exists(dest_dir):
        print(f"Backup already exists in: {dest_dir}")
        return
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder successfully copied to: {dest_dir}")
    except Exception as e:
        # Handle possible exceptions, e.g., permission issues or source directory not found
        print(f"Error: {e}")

# Schedule the backup to run every day at 12:00 PM
schedule.every().day.at("12:00").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# Run the scheduler loop
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 60 seconds before checking the schedule again
