# You need rarfile and zipfile module to perform this action
# Import modules
import os
import rarfile
import zipfile

# Function for extracting files
def extract_rar(file_path, extract_dir):
    with rarfile.RarFile(file_path, 'r') as rar:
        rar.extractall(extract_dir)
        print(f'Successfully extracted {file_path} to {extract_dir}')

# Function for creating zip
def create_zip(source_dir, zip_file):
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_dir))
        print(f'Successfully created {zip_file}')

# Examples for usage

# Extracting RAR file
rar_file_path = 'path/to/sample_file.rar'
extract_directory = 'path/to/extracted/files'
extract_rar(rar_file_path, extract_directory)

# Creating a zip file
source_directory = 'path/to/files'
zip_file_path = 'path/to/sample_archive.zip'
create_zip(source_directory, zip_file_path)
