from bilingual_file_extractor.auth_drive import authorize_google_drive


def list_files_in_drive(folder_id):
    """
    List all files and folders within a specified folder in Google Drive.

    Args:
        folder_id (str): The ID of the folder to list files from.

    Returns:
        list: list of files and folders in google drive folder.
    """
    # Authenticate to Google Drive using credentials from 'mycreds.txt'
    drive_instance = authorize_google_drive("mycreds.txt")

    # List all files and folders in the specified folder in Google Drive
    file_list_drive = drive_instance.ListFile(
        {"q": f"'{folder_id}' in parents and trashed=false"}
    ).GetList()

    return file_list_drive


if __name__ == "__main__":
    # Replace with the IDs of the folders you want to list files from
    shared_folder_ids = [
        "1kWP0kSnRhLHmzNW2MQm20XBMqMR3ZFX5",
        "1ljgik1RcIvd5-_HLIaBnLtxd5Icu7q4H",
        "17C-LiZMv7wAgn3f6WALbRecYuy0FSRTX",
        "1H_df94P26sDOxQVdTy65UZxJj4IB0iZz",
    ]
    names = []
    for folder_id in shared_folder_ids:
        # Retrieve a list of files and folders
        file_infos = list_files_in_drive(folder_id)
        for file_info in file_infos:
            # Extract the name without extension and add to the names list
            file_name_without_extension = file_info["title"].split(".")[0]
            names.append(file_name_without_extension)

    # Sort the list of names
    names.sort()

    # Write the sorted list of names to the file
    output_filename = "repo_list.txt"
    with open(output_filename, "w") as file:
        for name in names:
            file.write(f"{name}\n")

    print(f"File names have been written to {output_filename}")
