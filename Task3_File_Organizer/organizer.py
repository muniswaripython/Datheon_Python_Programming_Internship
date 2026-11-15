import os
import shutil
from pathlib import Path

# Folder containing files to organize
source_folder = Path(__file__).parent / "Test_Files"

# File extension categories
file_types = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".py": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code"
}

def organize_files():
    if not source_folder.exists():
        print("Test_Files folder does not exist!")
        return

    total_moved = 0

    for file in os.scandir(source_folder):
        if file.is_file():
            extension = Path(file.name).suffix.lower()
            category = file_types.get(extension)

            if category:
                destination = source_folder / category
                destination.mkdir(exist_ok=True)

                try:
                    shutil.move(
                        file.path,
                        destination / file.name
                    )
                    print(f"Moved: {file.name} -> {category}")
                    total_moved += 1

                except (FileExistsError, PermissionError, OSError) as error:
                    print(f"Could not move {file.name}: {error}")

            else:
                print(f"Skipped: {file.name}")

    print("\nFile organization completed!")
    print("Total files relocated:", total_moved)


if __name__ == "__main__":
    organize_files()
