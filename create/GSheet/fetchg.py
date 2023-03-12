from apiclient import discovery
from google.oauth2 import service_account
from pathlib import Path
import os


scopes = ['https://www.googleapis.com/auth/spreadsheets']
secret_file = os.path.join(Path(__file__).resolve().parent.parent.parent,r"client_secret.json")
credentials = service_account.Credentials.from_service_account_file(secret_file,scopes=scopes)
service = discovery.build('sheets','v4',credentials=credentials)


def fetchGSheet(gid):
    range_name = 'Sheet1!A1:B10'
    response= service.spreadsheets().values().get(spreadsheetId=gid, range=range_name).execute()
    return response

    # return response

# print(fetchGSheet("1KINif-eSxxILPJrrxthxOcmmBkeSyBQRvW9vtD1sHT4"))