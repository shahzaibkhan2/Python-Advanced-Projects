# Import necessary modules
import os
import shutil


# Function to collect cache
def collect_cache(folder_path):
    # Get the list of files and folders in the specified folder
    items_for_cache = os.listdir(folder_path)

    # Iterate over each item
    for item in items_for_cache:
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            # If it's a file, remove it
            os.remove(item_path)
        elif os.path.isdir(item_path):
            # If it's a subfolder, recursively call collect_cache
            collect_cache(item_path)

    # Remove the empty folder after cleaning the cache
    os.rmdir(folder_path)


# Example for usage
cache_folder = "/path/to/cache/folder"
collect_cache(cache_folder)
