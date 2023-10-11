import os

from bilingual_file_extractor.auth_drive import authorize_google_drive
from bilingual_file_extractor.drive_file_list import list_files_in_drive


def download_folder(folder_id, saving_to_path):
    """
    Download all files from a specified Google Drive folder to a local directory.

    Args:
        folder_id (str): The ID of the Google Drive folder to download files from.
        saving_to_path (str): The local directory where the files should be saved.

    Returns:
        None
    """
    # Authenticate to Google Drive using credentials from 'mycreds.txt'
    drive_instance = authorize_google_drive("mycreds.txt")

    # Get information about the Google Drive folder
    folder = drive_instance.CreateFile({"id": folder_id})

    # Create a local folder with the same name as the remote folder
    local_folder_path = os.path.join(saving_to_path, folder["title"])
    os.makedirs(local_folder_path, exist_ok=True)

    # List all files inside the current folder
    file_list = list_files_in_drive(folder_id)

    # Download each file to the local folder
    for item in file_list:

        if item["mimeType"] == "application/vnd.google-apps.folder":
            # If it's a folder, recursively download its contents
            download_folder(item["id"], saving_to_path)

        else:
            item.GetContentFile(os.path.join(local_folder_path, item["title"]))


if __name__ == "__main__":
    # Replace 'shared_folder_id' with the ID of the Google Drive folder you want to download from
    shared_folder_id = "you_share_folder_if"

    # Replace 'save_to_path' with the local directory where you want to save the downloaded files
    save_to_path = "path_to_your_local_folder"

    # Call the 'download_folder' function to download files from the Google Drive folder
    download_folder(shared_folder_id, save_to_path)
