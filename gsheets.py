import asyncio, random, os, gspread, discord
from oauth2client.service_account import ServiceAccountCredentials as SAC

def open():
    global sheet
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    creds = SAC.from_json_keyfile_name("SwifflingBot.json", scope)
    cliente = gspread.authorize(creds)
    sheet = cliente.open("Switchlings Bot Profile").sheet1

def read():
    return sheet.get_all_records()

def lenrows():
    return sheet.row_count


async def redoplaceinqueue():
    global sheet
    lenny = lenrows()
    lentimes = round((lenny/50)-0.5)
    for x in range(0,lentimes):
        for y in range((50*x),(50*x)+49):
            if y !=0 and y !=1:
                placebat="{}{}".format("A",str(x))
                sheet.update_acell(placebat,str(x))
        await asyncio.sleep(100)
    for y in range(50*(x+1),lenny):
        if y!=0 and y!=1:
            placebat="{}{}".format("A",str(x))
            sheet.update_acell(placebat,str(x))
        


def updatecell(varchar, place: str, variable):
    global sheet
    listie = {"switchcode" : "C", "gender" : "D", "skincolour" : "E", "eyecolour" : "F", "hairstyle": "G", "trousers": "H", "weapon": "I", "level": "J", "sz": "K", "tc": "L", "rm": "M", "cb": "N",
              "hat": "O", "hatmain": "P", "hatsub1": "Q", "hatsub2": "R", "hatsub3" : "S",
              "shirt": "T", "shirtmain": "U", "shirtsub1": "V", "shirtsub2": "W", "shirtsub3": "X",
              "shoes": "Y", "shoesmain": "Z", "shoessub1": "AA", "shoessub2": "AB", "shoessub3": "AC"}

    column = listie[varchar]
    placebat = "{}{}".format(column,place)
    sheet.update_acell(placebat, variable)
    if varchar=="gender":
        column = listie["hairstyle"]
        placebat = "{}{}".format(column,place)
        sheet.update_acell(placebat, "None")

def delrow(index):
    global sheet
    sheet.delete_row(index)

def addrow(values):
    global sheet
    sheet.append_row(values)
    
