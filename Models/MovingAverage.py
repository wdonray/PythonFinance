class MovingAverage:
    def __init__(self, days):
        # Moving average days
        self.days = days

    # Title of column for moving average
    def getMAColumn(self):
        return "Sma_" + str(self.days)

    def getMABeatsClosePercetage(self, df):
        # Creates column with the name from getMAColumn
        # That column is the rolling ma with a window size of our ma
        # Created from the 4th column in df which is adjusted close
        df[self.getMAColumn()] = df.iloc[:, 4].rolling(window=self.days).mean()

        # Cut out the first 50 days since they do not have a ma
        df = df.iloc[self.days:]

        # Track how often the close is greater than the ma
        higher = 0
        lower = 0
        for i in df.index:
            if(df["Adj Close"][i] > df[self.getMAColumn()][i]):
                higher += 1
            else:
                lower += 1

        percentage = round(higher / (higher + lower) * 100)

        return (str(percentage) + "%")
