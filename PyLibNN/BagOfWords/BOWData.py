class BOWData:    
    def __init__(self):
        pass
    def show():
        pass


class BOWDataRaw(BOWData):
    def __init__(self,name,words):
        self.name=name.split("/")[-1]
        self.words=words
        self.vector=0
    def show(self,vector=0):
        if self.vector==0 or vector==0:
            print self.name,":",self.words
        else:
            print self.name,":",self.vector
    def removeWord(self,word):
        while word in self.words:
            self.words.remove(word)

    def leaveWords(self,words):
        newWords=[]
        for word in self.words:
            if word in words:
                newWords.append(word)
        self.words=newWords

    def getWords(self):
        return self.words

    def setVector(self,vector):
        self.vector=vector

    def getVector(self):
        return self.vector

class DataSets:
    def __init__(self):
        self.dataSets={}
        self.dictionary=None
        self.LSIModel=None

    def addData(self,name,data):
        self.dataSets[name]=BOWDataRaw(name,data)
    
        
    def setDictionary(self,dic):
        self.dictionary=dic
        
    def getDictionary(self):
        return self.dictionary

    def getValues(self):
        values=[self.dataSets[name].getWords() for name in self.dataSets.keys()]
        return values

    def getVectors(self):
        vectors=[self.dataSets[name].getVector() for name in self.dataSets.keys()]
        return vectors
        
        
    def removeWord(self,word):
        for name in self.dataSets.keys():
            self.dataSets[name].removeWord(word)
    def setLSIModel(self,LSIModel):
        self.LSIModel=LSIModel

    def getStrLSIWeight(self):
        topics=self.LSIModel.print_topics()
        keys=self.dictionary.token2id.keys()
        vals=self.dictionary.values()
        """
        print "Keywords :",len(keys)
        for i,key in enumerate(keys):
            print(i,key)
        print " are reduced to ",len(topics)," topics by LSI"
        """
        retStr=[]
        for n,topic in enumerate(topics):
            strs=topic.split("+")
            ret=""
            for st in strs:
                txt="".join(st.split('"')).strip().split("*")
                ret+=vals[int(txt[1])]+":"+txt[0]+","
            retStr.append(ret.encode('utf-8'))
        return retStr
    
    def printLSIWeight(self):
        for n,ret in enumerate(self.getStrLSIWeight()):
            print n,ret
        """
        topics=self.LSIModel.print_topics()
        keys=self.dictionary.token2id.keys()
        vals=self.dictionary.values()
        print "Keywords :",len(keys)
        for i,key in enumerate(keys):
            print(i,key)
        print " are reduced to ",len(topics)," topics by LSI"
#        self.LSIModel.print_topics()
        for n,topic in enumerate(topics):
            strs=topic.split("+")
            ret=""
            for st in strs:
                txt="".join(st.split('"')).strip().split("*")
                ret+=vals[int(txt[1])]+":"+txt[0]+","
            print u"Topic:",n,ret.encode('utf-8')

            weights=[st.strip().split("*") for st in strs]
            weights.sort(key=lambda x:x[1])
            print "Topic:",n,topic
        """
#            print "Topic :",n,[w[0] for w in weights]


    def show(self,vector=0):
        if vector==1:            
            if self.LSIModel:
                self.printLSIWeight()
            else:
                print self.dictionary.token2id.keys() 
        for name in self.dataSets.keys():
            self.dataSets[name].show(vector=vector)
    
    def outputfile(self,outfile):
        hndl=open(outfile,"w")
        hndl.write("KEYS\n")
        keys=self.dictionary.token2id.keys()

        for i,key in enumerate(keys):
            hndl.write(str(i)+","+key+"\n")            

        hndl.write("Topics \n")
        retStrs=self.getStrLSIWeight()
        for ret in retStrs:
            hndl.write(ret+u"\n")
        hndl.write("Names\n")
        for name in self.dataSets.keys():
            hndl.write(name+":"+str(self.dataSets[name].getVector())+"\n")
        hndl.close()
        
