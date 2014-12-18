#main program for bag of words analysis
from AbsReadData import ReadData as ReadData
#from AbsStopWords import StopWords as StopWords
from AbsStopWords import SWFilter as StopWords
from AbsPreProcess import PreProcess as PreProcess
from AbsTexts2Vectors import Texts2Vectors as Texts2Vectors
import time

def makeDefaultSetting():
    Rd=ReadData([],targetDir="/mnt/arXiv_pdf_1305_007")
    Sw=StopWords(None,filterFile="filter.txt")
#    Sw=StopWords(["euv","x-ray","ir","observation","theory","physics","algorithm","sun","galaxy"])
    Pp=PreProcess(lowerLimit=2)
    Tv=Texts2Vectors()
    return Rd,Sw,Pp,Tv

class cpuTimer:
    def __init__(self):
        self.sTime=-1.0
        self.eTime=-1.0
    def start(self):
        self.sTime=time.time()
    def stop(self):
        self.eTime=time.time()
    def show(self,stop=0):
        if stop!=0:self.stop()
        dt=self.eTime-self.sTime
        self.sTime=self.eTime
        return dt

def main():
    Rd,Sw,Pp,Tv=makeDefaultSetting()
    #read bag of words data 
    timer=cpuTimer()
    timer.start()
    print "Reading data now"
    data=Rd.readData()
    print "Read data : ,",len(data.dataSets.keys())
    print "time :",timer.show(stop=1)
    print "Removing Stop Words"
    #remove Stopwords from data
    data=Sw.removeStopWords(data)
    print "Removing Stop Words finish"
    print "time :",timer.show(stop=1)
    #preprocessing
    print "Preprocess"
    data=Pp.preprocess(data)
    print "Preprocess finish"
    print "time :",timer.show(stop=1)
#    data.show()
    #convert texts to vectors (option LSI)
    print "LSI"
    data=Tv.texts2Vectors(data,LSI=1,nTopics=5)
    print "time :",timer.show(stop=1)
    data.show(vector=1)

if __name__=="__main__":
    main()
