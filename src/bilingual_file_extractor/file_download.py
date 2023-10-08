import os

from bilingual_file_extractor.auth_drive import authorize_google_drive
from bilingual_file_extractor.drive_file_list import list_files_in_drive


def download_folder(folder_id, saving_to_path):

    drive_instance = authorize_google_drive("mycreds.txt")

    folder = drive_instance.CreateFile({"id": folder_id})

    # Create a local folder with the same name as the remote folder
    local_folder_path = os.path.join(saving_to_path, folder["title"])
    os.makedirs(local_folder_path, exist_ok=True)

    # List all files inside the current folder
    file_list = list_files_in_drive(folder_id)
    for item in file_list:
        # Download files
        item.GetContentFile(os.path.join(local_folder_path, item["title"]))


if __name__ == "__main__":
    shared_folder_id = "12bYoD-HGzpkRdAffKRXIDPUxRlgzlXv_"
    save_to_path = "/home/gangagyatso/Downloads"
    download_folder(shared_folder_id, save_to_path)
