class FoodTable(dict):
    def addPair(self, flav1, flav2):
        if flav1 in self:
            self[flav1][0].append(flav2)
        else:
            self[flav1] = [[flav2],[]]
        if flav2 in self:
            self[flav2][0].append(flav1)
        else:
            self[flav2] = [[flav1],[]]
            
    def calcWeight(self, flav1, flav2):
        if flav2 == flav1:
            return 0
        if flav2 in self[flav1][0]:
            weight = None
        else:
            sharedFlavs = 0
            for flav in self[flav1][0]:
                if flav in self[flav2][0]:
                    sharedFlavs +=1
            weight = sharedFlavs
        return weight
    
    def getChosenPairs(self, flav):
        if flav in self:
            return self[flav][0]
        else:
            return False
        
    def getPossiblePairs(self, flav):
        if flav in self:
            return self[flav][1]
        else:
            return False
            
    def updateWeights(self):
        #totally O(n^2)...is there a better way?
        for flav1 in self:
            for flav2 in self:
                weight = self.calcWeight(flav1, flav2)
                if weight:
                    self[flav1][1].append((weight, flav2))
                    
def main():
    flavFileName = "pairs.txt"
    flavFile = open(flavFileName)
    flavTable = FoodTable()
    for line in flavFile:
        line = line.strip()
        line = line.split(" - ")
        flavTable.addPair(line[0], line[1])
    flavFile.close()
    flavTable.updateWeights()
    userFlav = raw_input("What flavor would you like to pair?   ")
    if userFlav in flavTable:
        print "Flavors you have said you like with", userFlav, ":"
        for i in flavTable.getChosenPairs(userFlav):
            print i
        print
        #maybe print in order from highest to lowest weights
        print "Flavors you might like with", userFlav, ":"
        for i in flavTable.getPossiblePairs(userFlav):
            print i[1], ",  weight", i[0]
    else:
        print "That flavor is not available. Please try something different or add it somewhere in your list of flavor pairs."
        
if __name__ == "__main__":
    main()
        