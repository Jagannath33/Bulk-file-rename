import os

def rename_files(directory, ending, newname):
    files = os.listdir(directory)
    counter = 0
    for file in files:
        if file.endswith(ending):
            filetype = file.split('.')[-1]  # Extract the file extension
            new_filename = f"{newname}{counter}.{filetype}"  # Build the new filename
            os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))  # Rename file
            print(f"Renaming {file} to {new_filename}")
            counter += 1

rename_files("C:\\Users\\Asus\\Desktop\\file manipulation", ".txt", "mynewname")







































