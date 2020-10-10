from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.appdata','https://www.googleapis.com/auth/drive']
FOLDER_ID="1u-CnTlzDCZ7abSDz-JaPfcCOreGlvwdv"
FILE_ID="1_EizWf92dxMpXNUd9rkn_m3tXNbmDFgr"


def updateFile(service):
    file = service.files().get(fileId=FILE_ID).execute()
    media = MediaFileUpload('/MyApp/Activities.csv')
    
    # Send the request to the API.
    updated_file = service.files().update(
        fileId=FILE_ID,
        media_body=media).execute()

def main():
    creds = None
    tokenPath=os.environ.get('TOKEN_PATH')
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(tokenPath):
        with open(tokenPath, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("creds.refresh(Request())")
            creds.refresh(Request())
        else:
            print("flow")
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            print("creds")
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    updateFile(service)


if __name__ == '__main__':
    main()
