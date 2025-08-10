import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ultis.ultis import *

FILE_NAME = "voice-to-text"
SHEET_NAME = "Voice1"
ANDROID_DETECT_OUTPUT_COL = "C"
IOS_DETECT_OUTPUT_COL = "D"
API_RESULT_COL = "E"
ultis = Ultis()

class GGSheet():
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.spreadsheet = self.client.open(FILE_NAME)
        self.worksheet = self.spreadsheet.worksheet(SHEET_NAME)

    def find_row(self, id):
        self.cell = self.worksheet.find(id)
        return self.cell.row
    
    def get_column(self, os):
        self.col = ""
        if os == "android":
            self.col = ANDROID_DETECT_OUTPUT_COL
        elif os == "ios":
            self.col = IOS_DETECT_OUTPUT_COL
        else:
            self.col = API_RESULT_COL
        return self.col
    
    def write_text(self, text, row, col):
        self.worksheet.update(f"{col}{row}", [[text]])
