from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def authorize_google_drive(credentials_file="mycreds.txt"):
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
    drive = GoogleDrive(gauth)  # noqa

    # Now you can use 'drive' to interact with Google Drive
    return drive


# Call the function to authorize Google Drive
drive_instance = authorize_google_drive()

# Now you can use 'drive_instance' to interact with Google Drive
