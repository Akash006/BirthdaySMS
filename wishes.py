import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import random
import requests

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("cread.json", scope)
client = gspread.authorize(creds)

# sheet = ss.worksheet("Friends")
# date = sheet.col_values(1)
# print(date)

class wish():

    def __init__(self):
        self.ss = client.open("Calender")
        self.sheets = ["Friends","Family"]
        self.x = datetime.datetime.now()
        self.currectDate = self.x.strftime("%d-%B")
        self.Birthday = []

    def check(self):
        for sht in self.sheets:
            sheet = self.ss.worksheet(sht)
            date = sheet.col_values(1)
            name = sheet.col_values(2)
            phNo = sheet.col_values(3)

            for dates,ph in zip(date,phNo):
                if dates == self.currectDate:
                    self.Birthday.append(ph)

        print(self.Birthday)

    def send(self):
        sh = self.ss.worksheet("B Wishes")
        wis = sh.col_values(1)

        for bday in self.Birthday:
            wish = random.choice(wis)
            wish += "\n\nRegards,\nAkash Saini" 
            url = "https://www.fast2sms.com/dev/bulk"
            payload = "sender_id=FSTSMS&message={0}&language=english&route=p&numbers={1}".format(wish,bday)
            headers = {
            'authorization': "YOUR API TOKEN",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)

if __name__ == "__main__":
    a = wish()
    a.check()
    a.send()


