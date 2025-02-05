
import os
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from django.core.files.storage import Storage

class GoogleDriveStorage(Storage):
    def __init__(self, *args, **kwargs):
        # Get the credentials JSON string from the environment variable
        google_creds_str = os.getenv('GOOGLE_CREDENTIALS_JSON')

        if google_creds_str is None:
            raise ValueError("Google credentials not found in environment variable.")

        # Convert the JSON string into a dictionary
        google_creds_dict = json.loads(google_creds_str)

        # Load the credentials using the dictionary
        self.credentials = Credentials.from_service_account_info(
            google_creds_dict, scopes=["https://www.googleapis.com/auth/drive.file"]
        )

        # Initialize the Google Drive API service
        self.service = build('drive', 'v3', credentials=self.credentials)

    def _save(self, name, content):
        file_metadata = {'name': name}
        media = MediaFileUpload(content.name, mimetype=content.content_type)
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file['id']  # Return the file ID instead of file path

    def url(self, name):
        return f"https://drive.google.com/uc?id={name}"  # Google Drive URL to access the file by ID
