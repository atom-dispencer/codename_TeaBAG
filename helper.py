class Tile:
    def __init__(self, thisFound, whatsThis, yoAreHere):
        self.thisFound = thisFound
        self.whatsThis = whatsThis
        self.yoAreHere = yoAreHere
    def __str__(self):
        return self.thisFound
