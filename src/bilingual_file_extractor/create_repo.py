from bilingual_file_extractor.auth_github import authenticate_github


def create_github_repo(username, token, repo_name, repo_description=""):
    # Authenticate with your GitHub credentials
    g = authenticate_github(username, token)

    try:
        # Create a new repository
        user = g.get_user()
        repo = user.create_repo(
            repo_name,
            description=repo_description,
            private=False,  # Set to True for a private repository
            auto_init=True,  # Initialize with a README file (optional)
        )
        print(f"Repository {repo.full_name} created successfully.")
    except Exception as e:
        print(f"Error creating repository: {str(e)}")


if __name__ == "__main__":

    # Replace these with your GitHub username and personal access token
    github_username = "gangagyatso4364"
    github_token = "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"

    # Define the repository name and description
    repository_name = "new-repo1"
    repository_description = "This is a new repository created using PyGithub."

    # Call the function to create the repository
    create_github_repo(
        github_username, github_token, repository_name, repository_description
    )
