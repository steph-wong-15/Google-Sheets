#referenced: https://developers.google.com/sheets/api/quickstart/python

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

#referenced: https://developers.google.com/identity/protocols/oauth2/service-account#python
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'

#Allows read and write access
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# credentials set to none initially
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The spreadsheet ID 
# Get spreadsheet ID from google sheets file that you want to interact with
# ID can be found in google spread sheet url after /d/
SAMPLE_SPREADSHEET_ID = '1ch5sZ2MtoNp4lv_kEOCPKyycAiIxSB0ahthe3aEHu4U'

   
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

# Data to be written
info_values = [['First Name', 'Last Name', 'University Subject', 'Date of Birth'], ['Adam', 'Testman', 'Computer Science', 'January 1, 1998']]


## WRITE
#referenced: https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/update
request =sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="info!A1", valueInputOption="USER_ENTERED", body={"values":info_values}).execute()

## READ
# Get request to get info from google sheets
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="info!A1:D1").execute()
values = result.get('values', [])

print(result)

#print('Name, Major:')
    #for row in values:
    # Print columns A and E, which correspond to indices 0 and 4.
    #print('%s, %s' % (row[0], row[4]))
    #except HttpError as err:
    #print(err)

