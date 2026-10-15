import os
import shutil
from collections import defaultdict
from pathlib import Path

# Mapping of folder names to their corresponding file extensions
CATEGORY_MAP = {
    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".svg",
        ".webp",
        ".ico",
    ],
    "Documents": [
        ".pdf",
        ".docx",
        ".doc",
        ".txt",
        ".xlsx",
        ".xls",
        ".pptx",
        ".ppt",
        ".csv",
    ],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"],
    "Code": [
        ".py",
        ".js",
        ".html",
        ".css",
        ".cpp",
        ".c",
        ".java",
        ".json",
        ".sql",
    ],
    "Executables": [".exe", ".msi", ".bat", ".sh"],
}


def organize_folder(target_directory):
    """Organizes files in target_directory into subfolders by type and prints a summary."""
    target_path = Path(target_directory).resolve()

    if not target_path.exists() or not target_path.is_dir():
        print(
            f"Error: Directory '{target_directory}' does not exist or is invalid."
        )
        return

    # Track count of moved files per category
    summary = defaultdict(int)
    skipped_count = 0

    print(f"\n📂 Scanning directory: {target_path}\n")

    for item in target_path.iterdir():
        # Ignore subdirectories and system/hidden files
        if item.is_dir() or item.name.startswith("."):
            continue

        ext = item.suffix.lower()

        # Determine the target subfolder name
        destination_category = "Others"
        for category, extensions in CATEGORY_MAP.items():
            if ext in extensions:
                destination_category = category
                break

        # Create subfolder path
        destination_folder = target_path / destination_category
        destination_folder.mkdir(exist_ok=True)

        destination_file_path = destination_folder / item.name

        # Avoid overwriting if a file with the same name already exists in target subfolder
        if destination_file_path.exists():
            print(f"⚠️ Skipped (already exists): {item.name}")
            skipped_count += 1
            continue

        # Move file
        shutil.move(str(item), str(destination_file_path))
        summary[destination_category] += 1

    # Print summary breakdown
    print("=" * 40)
    print("         ORGANIZATION SUMMARY         ")
    print("=" * 40)

    total_moved = sum(summary.values())
    if total_moved == 0:
        print("No files were moved.")
    else:
        for category, count in sorted(summary.items()):
            print(f"  • {category:<12}: {count} file(s)")
        print("-" * 40)
        print(f"  Total Moved : {total_moved} file(s)")

    if skipped_count > 0:
        print(f"  Total Skipped: {skipped_count} file(s)")
    print("=" * 40 + "\n")


if __name__ == "__main__":
    # Specify the target directory path (e.g., Path.home() / "Downloads" or "./my_folder")
    folder_to_organize = input(
        "Enter the directory path to organize: "
    ).strip()
    organize_folder(folder_to_organize)
    