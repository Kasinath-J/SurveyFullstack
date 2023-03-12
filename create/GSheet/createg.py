from apiclient import discovery
from google.oauth2 import service_account
from pathlib import Path
import os


scopes = ['https://www.googleapis.com/auth/spreadsheets']
secret_file = os.path.join(Path(__file__).resolve().parent.parent.parent,r"client_secret.json")
credentials = service_account.Credentials.from_service_account_file(secret_file,scopes=scopes)
service = discovery.build('sheets','v4',credentials=credentials)

def newGSheet(title):
    try:
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        
        spreadsheet = service.spreadsheets().create().execute()
        return spreadsheet.get('spreadsheetId')
    except :
        print(f"An error occurred")
        return None
