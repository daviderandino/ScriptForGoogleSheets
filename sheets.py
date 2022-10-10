# https://www.makeuseof.com/tag/read-write-google-sheets-python/

import re
import time
from traceback import print_tb
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

cell = sheet.acell('B16').value 

position = "B16"
i = 16 #row
j = 2 #column

while(cell!=None):
    cell = sheet.acell(position).value 
    print("Cell not yet empty!!!\n")
    time.sleep(5)

sheet.update_acell(position,text)
print("Cell updated succesfully")
