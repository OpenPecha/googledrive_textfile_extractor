from bilingual_file_extractor.auth_drive import authorize_google_drive


def list_files_in_drive(folder_id):
    """
    List all files and folders within a specified folder in Google Drive.

    Args:
        folder_id (str): The ID of the folder to list files from.

    Returns:
        list: A list of dictionaries, where each dictionary contains information about a file or folder.
              Each dictionary has the keys 'id' for the item's ID and 'name' for the item's name.
    """
    # Authenticate to Google Drive using credentials from 'mycreds.txt'
    drive_instance = authorize_google_drive("mycreds.txt")

    # List all files and folders in the specified folder in Google Drive
    file_list_drive = drive_instance.ListFile(
        {"q": f"'{folder_id}' in parents and trashed=false"}
    ).GetList()

    return file_list_drive


if __name__ == "__main__":
    # Replace 'shared_folder_id' with the ID of the folder you want to list files from
    shared_folder_id = "1H_df94P26sDOxQVdTy65UZxJj4IB0iZz"

    # Call the 'list_files_in_drive' function to retrieve a list of files and folders
    files = list_files_in_drive(shared_folder_id)

    # Print the list of file IDs and names
    print("Files:")
    for file_info in files:
        print(f'File ID: {file_info["id"]}, File Name: {file_info["name"]}')
