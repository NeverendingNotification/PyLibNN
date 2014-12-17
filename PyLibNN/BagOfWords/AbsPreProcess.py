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
        dataSets.setDictionary(dictionary)
        unfiltered=dictionary.token2id.keys()
        dictionary.filter_extremes(no_below=self.lowerLimit)
        filtered=dictionary.token2id.keys()
        removed=set(unfiltered)-set(filtered)
        for rem in removed:
            dataSets.removeWord(rem)
        return dataSets
