import asyncio, random, os, gspread, discord
from oauth2client.service_account import ServiceAccountCredentials as SAC

class SwitchlingsBotProfile():
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
    
class ListOfRanks():
    def open():
        global sheet1
        scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
        creds = SAC.from_json_keyfile_name("SwifflingBot.json", scope)
        clienteee = gspread.authorize(creds)
        sheet1 = clienteee.open("List of Ranks").sheet1

    def read():
        x = sheet1.get_all_values()[0]
        y=0
        while True:
            try:
                if x[y]=="":
                    x.remove(x[y])
                else:
                    y=y+1
            except IndexError:
                break
        return x

    def updaterow(values):
        sheet1.insert_row(values,index=1)
    

            
                