# https://www.makeuseof.com/tag/read-write-google-sheets-python/

import re
import time
from traceback import print_tb
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)
sheet_name = "Test" 
sheet = client.open(sheet_name).sheet1

def check_empty_sheet():
    all_cells = sheet.range('B12:E27')
    for cell in all_cells:
        if(cell.value!=''):
            return False
    return True

text = "Text"
position = "B16"

cell = sheet.acell(position).value 

i = 16 #row
j = 2 #column

while(cell!=None):
    cell = sheet.acell(position).value 
    e = datetime.datetime.now()
    print("Cell not yet empty! %s:%s:%s"% (e.hour, e.minute, e.second))
    time.sleep(5)

sheet.update_acell(position,text)
print("Cell updated succesfully")
