#main program for bag of words analysis
from AbsReadData import ReadData as ReadData
from AbsStopWords import StopWords as StopWords
from AbsPreProcess import PreProcess as PreProcess
from AbsTexts2Vectors import Texts2Vectors as Texts2Vectors

def makeDefaultSetting():
    Rd=ReadData([],targetDir="/home/nakamura/git/python/NLP-Tutorial/corpus")
    Sw=StopWords()
    Pp=PreProcess(lowerLimit=2)
    Tv=Texts2Vectors()
    return Rd,Sw,Pp,Tv

def main():
    Rd,Sw,Pp,Tv=makeDefaultSetting()
    #read bag of words data 
    data=Rd.readData()
    #remove Stopwords from data
    data=Sw.removeStopWords(data)
    #preprocessing
    data=Pp.preprocess(data)
    data.show()
    #convert texts to vectors (option LSI)
    data=Tv.texts2Vectors(data,LSI=1,nTopics=3)
    data.show(vector=1)

if __name__=="__main__":
    main()
