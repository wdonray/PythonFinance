class EMAManager:
    def __init__(self, shortestValue, Emas):
        self.shortestValue = shortestValue
        self.Emas = Emas

    def getShortCollection(self):
        return [x for x in self.Emas if x <= self.shortestValue]

    def getLongCollection(self):
        return [x for x in self.Emas if x > self.shortestValue]

    def getDisplay(self, ema):
        return "Ema_" + str(ema)
