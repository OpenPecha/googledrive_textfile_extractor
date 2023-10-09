from bilingual_file_extractor.auth_github import authenticate_github


def create_github_repo(token, repo_name, repo_description=""):
    """
    Create a new GitHub repository using PyGithub.

    Args:
        token (str): Your GitHub personal access token.
        repo_name (str): The name of the repository to be created.
        repo_description (str, optional): A description for the repository (default is an empty string).

    Returns:
        Repository: A PyGithub Repository object representing the newly created repository.
                   Returns None if an error occurs during creation.
    """
    # Authenticate with your GitHub personal access token
    g = authenticate_github(token)

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
        return repo

    except Exception as e:
        print(f"Error creating repository: {str(e)}")
        return None


if __name__ == "__main__":
    # Replace this with your GitHub personal access token
    github_token = "your_personal_github_token"

    # Define the repository name and description
    repository_name = "new-repo1"
    repository_description = "This is a new repository created using PyGithub."

    # Call the function to create the repository
    created_repo = create_github_repo(
        github_token, repository_name, repository_description
    )

    if created_repo:
        print(f"New repository URL: {created_repo.html_url}")
