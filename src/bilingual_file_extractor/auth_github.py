from github import Github


def authenticate_github(token):
    """
    Authenticate to GitHub using a personal access token.

    Args:
        token (str): Personal access token for GitHub.

    Returns:
        Github: A PyGithub instance authenticated with the token.
    """
    g = Github(token)
    return g


# Now you can use github_client to interact with GitHub's API.

if __name__ == "__main__":
    # Replace with your GitHub username and personal access token
    github_username = "gangagyatso4364"
    github_token = "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"

    # Authenticate to GitHub
    # Authenticate to GitHub
    github_client = authenticate_github(github_token)

    # Access a user's repositories
    user = github_client.get_user(github_username)
    repositories = user.get_repos()

    # List the repository names
    for repo in repositories:
        print(repo.name)
