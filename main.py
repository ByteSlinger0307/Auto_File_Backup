import os
import shutil
import datetime
import time
import schedule

source_dir = input("Enter the path of the directory you want to backup: ")
print("Note: Please make sure that the directories exists.")
destination_dir = input("Enter the directory in which you want to take the backup: ")

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print("Folder already exists in: {dest}")

schedule.every().day.at("12:00").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# copy_folder_to_directory(source_dir, destination_dir)

while True:
    schedule.run_pending()
    time.sleep(60)