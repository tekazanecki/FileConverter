import os
import argparse
from PIL import Image

# Argument parser
parser = argparse.ArgumentParser(description='Convert files to JPG or PNG')
parser.add_argument('format', type=str, nargs='?', default='png', help='Target format: jpg or png')
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

def convert_files():
    """
    Convert .webp files to the specified format and move the original files to the archive directory.
    """
    ensure_directories_exist()
    # Iterate through all files in the input folder
    for filename in os.listdir(input_dir):
        if filename.endswith(".webp"):
            # Open the file
            img = Image.open(input_dir + filename)
            print(f"File {filename} has been loaded")

            # Convert image to RGB
            img = img.convert('RGB')

            # Change file format
            root, ext = os.path.splitext(filename)
            img.save(output_dir + root + '.' + args.format)
            print(f"File {filename} has been converted")

            # Move the old file to the archive
            os.rename(input_dir + filename, archive_dir + filename)
            print(f"File {filename} has been moved to the archive")
            print("-------------------------------------------------------------------")


if __name__ == '__main__':
    convert_files()