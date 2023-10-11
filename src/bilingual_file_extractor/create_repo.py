from bilingual_file_extractor.auth_github import authenticate_github


def github_repo_exists(org, repo_name):
    try:
        org.get_repo(repo_name)
        return True
    except Exception as e:
        print(f"Error creating repository: {str(e)}")
        return False


def create_github_repo(github_token, org_name, repo_name, org, g):
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

    try:
        # Create a new repository
        repo = org.create_repo(
            repo_name,
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
    org_name = "your_github_organization"
    github_token = "your_personal_github_token"

    # Define the repository name and description
    repo_name = "new-repo1"
    g = authenticate_github(github_token)
    org = g.get_organization(org_name)

    # Call the function to create the repository
    created_repo = create_github_repo(github_token, org_name, repo_name, org, g)

    if created_repo:
        print(f"New repository name: {created_repo.full_name}")
