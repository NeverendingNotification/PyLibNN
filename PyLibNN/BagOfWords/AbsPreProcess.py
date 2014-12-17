import gensim
class PreProcess:
    #ProProcess
    # remove very rare words (smaller than lowCount)
    # and very common words from data
    def __init__(self,lowerLimit=2):
        self.lowerLimit=lowerLimit
        
    def preprocess(self,dataSets):
        values=dataSets.getValues()
        dictionary=gensim.corpora.Dictionary(values)
        print "Make Dict"
        dataSets.setDictionary(dictionary)
        unfiltered=dictionary.token2id.keys()
        dictionary.filter_extremes(no_below=self.lowerLimit)
        filtered=dictionary.token2id.keys()
        removed=set(unfiltered)-set(filtered)
        print "Start remove words",len(removed)
        
        for i,rem in enumerate(removed):
 #           if i%50==0:print i
            dataSets.removeWord(rem)
        return dataSets
