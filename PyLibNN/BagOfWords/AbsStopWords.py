class StopWords:
    # remove stop words from data set 
    # method removeStopWords(data):
    #   
    def __init__(self,stopWords=0):
        if(stopWords==0):
            stopWords=['the', 'of', 'a', 'an','at', 'is']
        self.stopWords=stopWords
    
    def removeStopWords(self,dataSets):
        data=dataSets.dataSets
        for name in data.keys():
            for sw in self.stopWords:
                data[name].removeWord(sw)
        return dataSets
                
