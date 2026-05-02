# File Organizer CLI

A command-line tool built with Python that automatically sorts all the files in a folder into organized subfolders based on their file type. Instead of manually moving files one by one, you just run the script, give it a folder path, and it handles everything.

## What It Does

You give it a folder path. It goes through every file in that folder, checks the file extension, and moves each file into a matching subfolder like Images, Documents, Videos, Audio, Scripts, or Archives. If the subfolder does not exist yet, it creates it automatically.

## How It Works (Step by Step)

1. The program asks you to enter a folder path.
2. It checks if that path exists using `os.path.exists`. If it does not, it prints an error and stops.
3. If the path is valid, it calls `organize_files()` and passes the folder path to it.
4. Inside the function, `os.listdir()` lists every file and folder inside that path.
5. A `for` loop goes through each item. For every item, `os.path.splitext()` splits the name and the extension.
6. The script skips itself during the loop using `os.path.basename(__file__)` so it does not accidentally move its own `.py` file.
7. It checks if the extension exists as a key in the `FILE_TYPES` dictionary. That dictionary maps extensions to folder names, for example `.jpg` maps to `Images` and `.mp3` maps to `Audio`.
8. If the extension is recognized, it builds the destination path using `os.path.join()`.
9. If that destination subfolder does not exist yet, `os.makedirs()` creates it.
10. `shutil.move()` then moves the file from its current location into the correct subfolder. This is essentially a cut and paste operation.
11. A counter tracks how many files were moved. At the end it prints how many files were organized, or a message saying there was nothing to organize.

## Supported File Types

| Extension | Goes Into |
|-----------|-----------|
| .jpg, .png, .gif | Images |
| .txt, .pdf, .docx, .csv, .xlsx | Documents |
| .mp3, .wav | Audio |
| .mp4, .mov | Videos |
| .zip, .rar, .tar | Archives |
| .py, .js, .html | Scripts |

## Project Structure

```
File_organizer_CLI/
└── file_organizer.py
```

## Requirements

- Python 3.x
- No external libraries needed. Only `os` and `shutil` which are part of Python's standard library.

## How to Run

```
python file_organizer.py
```

Then enter the folder path when prompted.

**Example session:**

```
Enter the folder path to organize: C:\Users\Saqib\Downloads

Organized 14 files in the folder: C:\Users\Saqib\Downloads
```

After running, your Downloads folder would look like this:

```
Downloads/
├── Images/
│   ├── screenshot.png
│   └── photo.jpg
├── Documents/
│   ├── notes.txt
│   └── report.pdf
├── Videos/
│   └── lecture.mp4
└── Scripts/
    └── script.py
```

## Built With

- `os` — for checking paths, listing files, and creating folders
- `shutil` — for moving files from one location to another

## Author

Muhammad Saqib — BS Software Engineering, Air University Islamabad  
GitHub: [Muhammad-Saqib-eng](https://github.com/Muhammad-Saqib-eng)
