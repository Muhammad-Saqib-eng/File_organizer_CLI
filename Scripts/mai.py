import os
import shutil


FILE_TYPES= {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".csv": "Documents",
    ".xlsx": "Documents",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".mp4": "Videos",
    ".mov": "Videos",        
    ".zip": "Archives",
    ".rar": "Archives",
    ".tar": "Archives",
    ".py": "Scripts",
    ".js": "Scripts",
    ".html": "Scripts",

}



def organize_files(folder_path):
    folders= os.listdir(folder_path)   
    counter=0
    for folder in folders:
        name,ext= os.path.splitext(folder)
        if ext in FILE_TYPES:
            folder_name= FILE_TYPES[ext]
            folder_dest= os.path.join(folder_path,folder_name)
            if not os.path.exists(folder_dest):
                os.makedirs(folder_dest)
            shutil.move(os.path.join(folder_path,folder), os.path.join(folder_dest,folder))
            counter+=1
    if counter==0:
        print("No files to organize in the specified folder.")
    else:   
        print(f"Organized {counter} files in the folder: {folder_path}")
    

folder_path=input("Enter the folder path to organize: ")
if os.path.exists(folder_path):
    organize_files(folder_path)
else:
    print("The specified folder path does not exist.")
            