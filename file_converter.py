import os
import argparse
from PIL import Image
import subprocess
import pyperclip
from pathlib import Path

# Argument parser
parser = argparse.ArgumentParser(description='Convert files to JPG or PNG')
parser.add_argument('format', type=str, nargs='?', default='png', help='Target format: jpg or png')
parser.add_argument('mode', type=str, choices=['shortcut', 'console'], default='console',
                    help='Mode of operation: shortcut or console')
parser.add_argument('--file', type=str, help='Path to a specific file to be converted (used in console mode)')
parser.add_argument('--folder', type=str, help='Path to a folder containing files to be converted')
args = parser.parse_args()

input_dir = 'input/'
output_dir = 'output/'
archive_dir = 'arch/'

def ensure_directories_exist():
    """
    Ensure that the required directories exist. If not, create them.
    """
    for directory in [input_dir, output_dir, archive_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory {directory} has been created")
        else:
            print(f"Directory {directory} already exists")


def convert_file(filepath, target_dir=None, archive=True):
    """
    Convert a single .webp file to the specified format. If target_dir is provided, save the converted file there,
    otherwise save it in the same directory as the original file.

    Args:
        filepath (str): Path to the file to be converted.
        target_dir (str, optional): Directory where the converted file should be saved.
        archive (bool, optional): Whether to save the converted file to an archive.
    """
    if filepath.endswith(".webp"):
        # Open the file
        img = Image.open(filepath)
        print(f"File {filepath} has been loaded")

        # Convert image to RGB
        img = img.convert('RGB')

        # Change file format
        root, ext = os.path.splitext(filepath)
        if target_dir:
            output_filepath = os.path.join(target_dir, os.path.basename(root) + '.' + args.format)
        else:
            output_filepath = root + '.' + args.format
        img.save(output_filepath)
        print(f"File {filepath} has been converted to {output_filepath}")

        if archive:
            archive_filepath = os.path.join(archive_dir, os.path.basename(filepath))
            if not os.path.exists(archive_dir):
                os.makedirs(archive_dir)
            os.rename(filepath, archive_filepath)
            print(f"File {filepath} has been moved to the archive at {archive_filepath}")
        print("-------------------------------------------------------------------")


def convert_files_in_folder(folder):
    """
    Convert all .webp files in the specified folder.

    Args:
        folder (str): Path to the folder containing files to be converted.
    """
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath) and filepath.endswith(".webp"):
            convert_file(filepath, target_dir=output_dir)


if __name__ == '__main__':
    ensure_directories_exist()

    if args.mode == 'shortcut':
        # Run PowerShell script to get selected file path and store it in the clipboard
        subprocess.run(["powershell", "-File", "get_selected_file_path.ps1"])

        # Read the clipboard to get the file path
        selected_file = pyperclip.paste()
        print(f"File from clipboard: {selected_file}")
        file_path = Path(selected_file)
        folder_path = file_path.parent

        if selected_file:
            convert_file(selected_file, target_dir=folder_path, archive=False)
        else:
            print("No file path found in clipboard.")
    elif args.mode == 'console':
        if args.file:
            convert_file(args.file)
        elif args.folder:
            convert_files_in_folder(args.folder)
        else:
            convert_files_in_folder(input_dir)

    input("Press Enter to exit...")
