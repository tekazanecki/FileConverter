
# File Converter

File Converter is a Python project designed to convert `.webp` files to `.jpg` or `.png` format. It can operate in two modes: via a console command or by using a shortcut that interacts with Windows Explorer to get the selected file path.

## Features

- Convert `.webp` files to `.jpg` or `.png` format.
- Archive converted files.
- Operate via console or shortcut.

## Requirements

- Python 3.x
- [Pillow](https://pillow.readthedocs.io/en/stable/) library
- [pyperclip](https://pyperclip.readthedocs.io/en/latest/) library
- Windows PowerShell
- Basic understanding of PowerShell scripts and batch files

## Installation

1. Clone the repository:
    
    bash
    

- `git clone https://github.com/yourusername/file-converter.git` 
- `cd file-converter`
    
- Install the required Python libraries:
    
    bash
    

1. `pip install Pillow pyperclip`
    

## Usage

### Console Mode

You can convert files using the console mode by specifying the file or folder path.

#### Convert a Single File

bash

`python file_converter.py --file path/to/your/file.webp`

#### Convert All Files in a Folder

bash

`python file_converter.py --folder path/to/your/folder`

### Shortcut Mode

The shortcut mode allows you to use a PowerShell script to copy the selected file path in Windows Explorer to the clipboard, then convert it using the Python script.

#### Create a Shortcut

1. Create a batch file `convert_file_shortcut.bat` with the following content:
    
    batch
    

1. `@echo off python path\to\your\project\file_converter.py shortcut pause`
    
2. Create a shortcut to this batch file on your desktop or any convenient location.
    

#### Use the Shortcut

1. Select a `.webp` file in Windows Explorer.
2. Run the shortcut created in the previous step.
3. The file will be converted and saved in the same directory.

## Directory Structure

- `input/` - Default input directory for `.webp` files.
- `output/` - Default output directory for converted files.
- `arch/` - Directory for archiving original `.webp` files after conversion.

## File Descriptions

### file_converter.py

The main script for converting `.webp` files. It includes functions to:

- Ensure required directories exist.
- Convert a single file or all files in a folder.
- Handle console and shortcut modes.

### get_selected_file_path.ps1

A PowerShell script to retrieve the path of the selected file in Windows Explorer and copy it to the clipboard.

### convert_file_shortcut.bat

A batch file to run the `file_converter.py` script in shortcut mode.

## Example

To convert all `.webp` files in the default input directory, run:

bash

`python file_converter.py`

To convert a specific file via the console:

bash

`python file_converter.py console --file path/to/your/file.webp`

To convert all files in a specific folder:

bash

`python file_converter.py console --folder path/to/your/folder`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.