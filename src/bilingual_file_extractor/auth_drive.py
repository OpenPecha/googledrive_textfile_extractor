from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def authorize_google_drive(credentials_file):
    """_summary_

    Args:
        credentials_file (_type_): _description_

    Returns:
        _type_: _description_
    """ """

    """
    # Initialize GoogleAuth and create a local web server and open the browser
    gauth = GoogleAuth()

    # Try to load saved client credentials
    gauth.LoadCredentialsFile(credentials_file)

    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()

        # Save the current credentials to a file
        gauth.SaveCredentialsFile(credentials_file)
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize GoogleDrive with the credentials
        gauth.Authorize()

    # Create GoogleDrive instance with authenticated GoogleAuth instance
    drive = GoogleDrive(gauth)

    # Now you can use 'drive' to interact with Google Drive
    return drive


if __name__ == "__main__":

    drive_instance = authorize_google_drive("mycreds.txt")

    # Now you can use 'drive_instance' to interact with Google Drive
