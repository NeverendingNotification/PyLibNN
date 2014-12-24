class StopWords:
    # remove stop words from data set 
    # method removeStopWords(data):
    #   
    def __init__(self,stopWords=0):
        if(stopWords==0):
            stopWords=['the', 'of', 'a', 'an','at', 'is']
        self.stopWords=stopWords

    def removeStopWord(self,words):
        for sw in self.stopWords:
            while sw in words:
                words.remove(sw)
            
    
    def removeStopWords(self,dataSets):
        data=dataSets.dataSets
        for name in data.keys():
            for sw in self.stopWords:
                data[name].removeWord(sw)
        return dataSets
                
class SWFilter(StopWords):
    def __init__(self,filterWords,filterFile=""):
        if filterFile!="":
            filterWords=open(filterFile).read().split("\n")[:-1]
        self.filterWords=filterWords            
        StopWords.__init__(self)

    def removeStopWord(self,words):
        newWords=[]
        for word in words:
            if word in self.filterWords:
                newWords.append(word)
        return newWords
            

    
    def removeStopWords(self,dataSets):
        data=dataSets.dataSets
        for name in data.keys():
            for sw in self.stopWords:
                data[name].leaveWords(self.filterWords)
        return dataSets
