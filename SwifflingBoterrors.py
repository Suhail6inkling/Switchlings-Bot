class WillCrashBot(Exception):
    def __init__(self):
        super().__init__()
        self.message = "This will probably overload the bot and thus will not function"

class PersonNotFound(Exception):
    def __init__(self):
        self.message = "This person is not in the database and cannot be found."

class IncorrectDataSubmitted(Exception):
    def __init__(self):
        self.message = "This item cannot be found. It either doesn't exist, is spelt incorrectly or is in the wrong format. Remember that most items are case-sensitive. If this exists and is new, please contact Suhail6inkling"
        
class RegionMissing(Exception):
    def __init__(self):
        self.message = "A region was not chosen or an incorrect region was chosen. Please choose from NA (North America & Oceania), EU (Europe) or JP (Japan)"

class SwitchlingMissing(Exception):
    def __init__(self):
        self.message = "A Switchling was not chosen or was incorrect. Please choose from Seven19inkling, Smol4inkling, Suhail6inkling, Arca9inkling or Minty12inkling"

class RankError(Exception):
        message = "This rank doesn't exist"