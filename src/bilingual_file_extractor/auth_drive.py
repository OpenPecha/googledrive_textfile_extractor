from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def authorize_google_drive(credentials_file):
    """
    Authorize access to Google Drive using OAuth2 credentials.

    Args:
        credentials_file (str): The path to the JSON file containing OAuth2 credentials.

    Returns:
        GoogleDrive: A GoogleDrive instance authenticated with the provided credentials.
    """
    # Initialize GoogleAuth and create a local web server to open the browser for authentication
    gauth = GoogleAuth()

    # Try to load saved client credentials if they exist
    gauth.LoadCredentialsFile(credentials_file)

    if gauth.credentials is None:
        # Authenticate if no credentials found
        gauth.LocalWebserverAuth()

        # Save the current credentials to a file for future use
        gauth.SaveCredentialsFile(credentials_file)
    elif gauth.access_token_expired:
        # Refresh credentials if they have expired
        gauth.Refresh()
    else:
        # Initialize GoogleDrive with the existing credentials
        gauth.Authorize()

    # Create a GoogleDrive instance using the authenticated GoogleAuth instance
    drive = GoogleDrive(gauth)

    return drive


if __name__ == "__main__":
    # Authorize access to Google Drive and get a GoogleDrive instance
    drive_instance = authorize_google_drive("mycreds.txt")

    # Now you can use 'drive_instance' to interact with Google Drive
