class Filter:
    def __init__(self, boardsize):
        self.size = boardsize

    def apply(self, means):
        print 'length: '+str(len(means))
        globalAvg = self.getGlobalWhiteAverage(means)
        print globalAvg
        for i in range(len(means)):
            if self.isWhite(i):
                continue
            neighbours = self.getNeighbours(i, means)
            localAvg = sum(neighbours)/float(len(neighbours))
            means[i] = means[i]/localAvg * globalAvg

    def getGlobalWhiteAverage(self, means):
        #whites = list(filter(self.isWhite, means))
        enumerated = list(
            filter(lambda (x, _): self.isWhite(x),
                enumerate(means)
            )
        )
        print 'global whites'
        for (index, val) in enumerated:
            print index
        print '---END GLOBAL WHITES---'
        whites = list(map(lambda (i, _): i, enumerated))
        return sum(whites) / float(len(whites))

    def isWhite(self, index):
        row = index / self.size
        col = index % self.size

        return row % 2 != col % 2

    def getRow(self, i):
        return i / self.size

    def getCol(self, i):
        return i % self.size

    def getNeighbours(self, index, means):
        row = self.getRow(index)
        col = self.getCol(index)
        return list(filter(lambda x: x != -1, [
            self.getMeanAt(row-1, col, means),
            self.getMeanAt(row+1, col, means),
            self.getMeanAt(row, col-1, means),
            self.getMeanAt(row, col+1, means)
        ]))

    def getMeanAt(self, row, col, means):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return -1
        index = row * self.size + col
        print index
        return means[index]
