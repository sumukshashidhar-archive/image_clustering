from os import listdir


def get_jpg_files(filepath):
    """
    Get a list of files with the .jpg extension in the specified directory.

    Parameters:
    filepath (str): The path to the directory to search for .jpg files.

    Returns:
    list: A list of filenames with the .jpg extension in the specified directory.
    """
    # Initialize an empty list to store the .jpg filenames.
    jpg_files = []

    # Use os.listdir() to get a list of filenames in the specified directory.
    filenames = listdir(filepath)

    # Loop through the filenames and check if the file has a .jpg extension.
    for filename in filenames:
        if filename.endswith('.jpg'):
            # If the file has a .jpg extension, append it to the jpg_files list.
            jpg_files.append(filename)

    # Return the list of .jpg filenames.
    return sorted(jpg_files)
