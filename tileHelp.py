class Tile:
    def __init__(self, thisFound, whatsThis, amIHere, description):
        self.thisFound = thisFound
        self.whatsThis = whatsThis
        self.discovered = 0
        self.amIHere = 0
        self.description = description
        
    def __str__(self):
        return self.thisFound
    def getLn1(self):
        return "|" + self.thisFound
    def getLn2(self):
        if self.discovered == 0:
            return "|" + "  >  ?  <  "
        else:
            return "|" + self.whatsThis
    def getLn3(self):
        if self.amIHere == 0:
            return "|" + "    ---    "
        else:
            return "|" + "  >>YOU<<  "
    def getDescription(self):
        return self.description
        
