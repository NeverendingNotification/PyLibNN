import gensim

class Texts2Vectors:
    def __init__(self):
        pass
    def texts2Vectors(self,dataSets,LSI=0,nTopics=2):
        dic=dataSets.getDictionary()
        data=dataSets.dataSets
        
        for name in data.keys():
            vector=dic.doc2bow(data[name].getWords())
            data[name].setVector(vector)

        if LSI==1:
            lsiModel=gensim.models.LsiModel(dataSets.getVectors(),num_topics=nTopics)
            dataSets.setLSIModel(lsiModel)
            for name in data.keys():
                vector=lsiModel[data[name].getVector()]            
                data[name].setVector(vector)
            
            
        return dataSets
