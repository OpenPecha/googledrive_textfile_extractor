import os

from bilingual_file_extractor.create_repo import create_github_repo


def upload_file_in_new_repo(token, local_folder):
    """
    Creates a new GitHub repository for each file in a local folder and uploads the file to the repository.

    Args:
        token (str): Your GitHub personal access token.
        local_folder (str): The local folder containing the files to upload.

    Returns:
        None
    """
    # Iterate through files in the local folder
    for filename in os.listdir(local_folder):
        if os.path.isfile(os.path.join(local_folder, filename)):
            # Create a new repository with the same name as the file (without extension)
            repo_name = os.path.splitext(filename)[0]
            repo = create_github_repo(token, repo_name, repo_description="")

            # Upload the file to the repository
            with open(os.path.join(local_folder, filename), encoding="utf-8") as file:
                content = file.read()

            try:
                repo.create_file(
                    filename,
                    f"Add {filename}",
                    content,
                )
                print(f"File '{filename}' uploaded to '{repo.full_name}' repository.")
            except Exception as e:
                print(
                    f"Error uploading file '{filename}' to '{repo.full_name}' repository: {str(e)}"
                )


if __name__ == "__main__":
    # Replace these with your personal access token, and local folder path
    github_token = "perosnal_github_token"
    local_folder = "path/to/your/local_folder"

    # Call the function to create repositories and upload files
    upload_file_in_new_repo(github_token, local_folder)
