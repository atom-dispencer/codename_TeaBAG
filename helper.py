class Tile:
    def __init__(self, thisFound, whatsThis, yoAreHere):
        self.thisFound = thisFound
        self.whatsThis = whatsThis
        self.yoAreHere = yoAreHere
        self.discovered = 0
        self.amIHere = 0

#    def __init__(self, thisFound):
 #       self.thisFound = thisFound
  #      self.whatsThis = " >     < "
   #     self.yoAreHere = "  ---  "
        
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
            return "|" + "           "
        else:
            return "|" + self.yoAreHere
