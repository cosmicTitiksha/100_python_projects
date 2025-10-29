import os

def bulk_rename_files(directory, prefix, extension):
    """Renames all files in a directory with a specified extension."""
    
    # 1. Define Variables
    count = 1
    
    # 2. Get the List of Files
    try:
        file_list = os.listdir(directory)
    except FileNotFoundError:
        print(f"Error: Directory not found at '{directory}'")
        return
    
    print(f"\n--- Starting Bulk Rename in: {directory} ---")

    # 3. Iterate, Filter, and Rename
    for old_name in file_list:
        old_file_path = os.path.join(directory, old_name)

        # Skip directories and files that don't match the extension
        if not os.path.isfile(old_file_path) or not old_name.endswith(extension):
            continue
            
        # Generate the New Name: prefix + sequential number (padded to 3 digits) + extension
        new_name = f"{prefix}{count:03d}{extension}"
        new_file_path = os.path.join(directory, new_name)
        
        # Perform the Rename
        try:
            os.rename(old_file_path, new_file_path)
            print(f"SUCCESS: '{old_name}' -> '{new_name}'")
            count += 1
        except Exception as e:
            print(f"FAILED to rename '{old_name}'. Error: {e}")

    print(f"--- Finished. {count - 1} files were renamed. ---")



# Create a folder called 'test_files' with some .txt files before running !!!
TARGET_DIRECTORY = './test_files' 
NEW_PREFIX = 'test_renamer_'
TARGET_EXTENSION = '.txt' # Only files ending with this will be renamed

# Run the function
bulk_rename_files(TARGET_DIRECTORY, NEW_PREFIX, TARGET_EXTENSION)