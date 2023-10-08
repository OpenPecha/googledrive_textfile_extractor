from bilingual_file_extractor.auth_drive import authorize_google_drive


def list_files_and_folders_in_drive(folder_id):

    drive_instance = authorize_google_drive("mycreds.txt")
    # Create an empty list to store file IDs and names
    file_list = []
    folder_list = []
    # List all files and folders in your Google Drive
    file_list_drive = drive_instance.ListFile(
        {"q": f"'{folder_id}' in parents and trashed=false"}
    ).GetList()

    # Extract file and folder information and append them to the respective lists
    for item in file_list_drive:
        item_id = item["id"]
        item_name = item["title"]
        if item["mimeType"] == "application/vnd.google-apps.folder":
            folder_list.append({"id": item_id, "name": item_name})
        else:
            file_list.append({"id": item_id, "name": item_name})

    return file_list, folder_list


if __name__ == "__main__":
    shared_folder_id = "1H_df94P26sDOxQVdTy65UZxJj4IB0iZz"

    files, folders = list_files_and_folders_in_drive(shared_folder_id)

    # Print the list of file IDs and names
    print("Files:")
    for file_info in files:
        print(f'File ID: {file_info["id"]}, File Name: {file_info["name"]}')

    # Print the list of folder IDs and names
    print("\nFolders:")
    for folder_info in folders:
        print(f'Folder ID: {folder_info["id"]}, Folder Name: {folder_info["name"]}')
