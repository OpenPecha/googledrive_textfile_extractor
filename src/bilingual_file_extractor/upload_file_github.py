import os

from bilingual_file_extractor.auth_github import authenticate_github
from bilingual_file_extractor.create_repo import create_github_repo, github_repo_exists


def upload_file_in_new_repo(token, org_name, local_folder):

    """
    Creates a new GitHub repository for each file in a local folder and uploads the file to the repository.

    Args:
        token (str): Your GitHub personal access token.
        local_folder (str): The local folder containing the files to upload.

    Returns:
        None
    """
    cnt = 0
    # Iterate through files in the local folder
    for filename in os.listdir(local_folder):
        if os.path.isfile(os.path.join(local_folder, filename)):
            # Create a new repository with the same name as the file (without extension)
            repo_name = os.path.splitext(filename)[0]

            # Upload the file to the repository
            with open(os.path.join(local_folder, filename), encoding="utf-8") as file:
                content = file.read()
            # authenticate github with personal token
            g = authenticate_github(token)
            org = g.get_organization(org_name)

            try:
                cnt = cnt + 1
                if github_repo_exists(org, repo_name):
                    print(
                        f"Repository '{repo_name}' already exists. Skipping upload.",
                        cnt,
                    )
                else:
                    repo = create_github_repo(token, org_name, repo_name, org, g)
                    repo.create_file(
                        filename,
                        f"Add {filename}",
                        content,
                    )
                    print(
                        f"File '{filename}' uploaded to '{repo.full_name}' repository.",
                        cnt,
                    )
            except Exception as e:
                print(
                    f"Error uploading file '{filename}' to '{repo.full_name}' repository: {str(e)}"
                )


if __name__ == "__main__":
    # Replace these with your personal access token, and local folder path
    org_name = "organiztion_name"
    github_token = "your_personel_github_token"
    local_folder = "you_path_to_local_folder"

    # Call the function to create repositories and upload files
    upload_file_in_new_repo(github_token, org_name, local_folder)
