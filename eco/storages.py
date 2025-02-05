from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from django.core.files.storage import Storage
import os

class GoogleDriveStorage(Storage):
    def __init__(self, *args, **kwargs):
        self.credentials = Credentials.from_service_account_file(
            'google_credentials/cre.json',
            scopes=["https://www.googleapis.com/auth/drive.file"]
        )
        self.service = build('drive', 'v3', credentials=self.credentials)

    def _save(self, name, content):
        file_metadata = {'name': name}
        media = MediaFileUpload(content.name, mimetype=content.content_type)
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file['id']  # Return the file ID instead of file path

    def url(self, name):
        return f"https://drive.google.com/uc?id={name}"  # Google Drive URL to access the file by ID
