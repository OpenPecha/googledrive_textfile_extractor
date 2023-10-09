import os

from bilingual_file_extractor.create_repo import create_github_repo


def upload_file_in_new_repo(username, token, local_folder):
    """
    Creates a new GitHub repository for each file in a local folder and uploads the file to the repository.

    :param github_token: GitHub personal access token
    :param local_folder: Local folder containing the files to upload
    """

    # Iterate through files in the local folder
    for filename in os.listdir(local_folder):
        if os.path.isfile(os.path.join(local_folder, filename)):
            # Create a new repository with the same name as the file
            repo_name = filename.split(".")[0]  # Remove file extension
            # create new git repo
            repo = create_github_repo(username, token, repo_name, repo_description="")

            # Upload the file to the repository

            with open(os.path.join(local_folder, filename), encoding="utf-8") as file:
                content = file.read()
            repo.create_file(
                filename,
                f"Add {filename}",
                content,
            )


if __name__ == "__main__":
    github_username = "gangagyatso4364"
    github_token = "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"
    local_folder = "/home/gangagyatso/Downloads/Test"

    upload_file_in_new_repo(github_username, github_token, local_folder)
