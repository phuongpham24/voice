import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ultis.ultis import *

FILE_NAME = "voice-to-text"
SHEET_NAME = "newVoice"
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
    
    def write_text(self, text, row, col):
        self.worksheet.update(range_name=f"{col}{row}", values=[[text]])
