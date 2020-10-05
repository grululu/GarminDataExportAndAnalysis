import pickle
import os.path
from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.currentonly']
API_ID = "MPXBjd9Jo6JaTAgnJv0OTTgDjbPpXjcUl"
FUNCTION = "importCSVFromGoogleDrive"

def get_scripts_service():
    """Calls the Apps Script API.
    """
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
            creds.refresh(Request())
        else:
            # Credentials path from the credentials .json file
            # from step 3 from Google Cloud Platform section
            flow = InstalledAppFlow.from_client_secrets_file(
                '.credentials/client_id.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('script', 'v1', credentials=creds)


service = get_scripts_service()
# API ID from step 3 in Google Sheets/Script section

# Instead macro_test select your macro function name
# from step 5 in Sheets/Script section
request = {"function": FUNCTION}

try:
    response = service.scripts().run(body=request, scriptId=API_ID).execute()
    print(response)
except errors.HttpError as error:
    # The API encountered a problem.
    print(error.content)
