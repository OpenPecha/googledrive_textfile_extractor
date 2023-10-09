from bilingual_file_extractor.auth_drive import authorize_google_drive


def list_files_in_drive(folder_id):
    """_summary_

    Args:
        folder_id (_type_): _description_

    Returns:
        _type_: _description_
    """

    drive_instance = authorize_google_drive("mycreds.txt")

    # List all files and folders in your Google Drive
    file_list_drive = drive_instance.ListFile(
        {"q": f"'{folder_id}' in parents and trashed=false"}
    ).GetList()

    return file_list_drive


if __name__ == "__main__":
    shared_folder_id = "1H_df94P26sDOxQVdTy65UZxJj4IB0iZz"

    files = list_files_in_drive(shared_folder_id)

    file_list = []
    for item in files:
        item_id = item["id"]
        item_name = item["title"]
        file_list.append({"id": item_id, "name": item_name})

    # Print the list of file IDs and names
    print("Files:")
    for file_info in file_list:
        print(f'File ID: {file_info["id"]}, File Name: {file_info["name"]}')
