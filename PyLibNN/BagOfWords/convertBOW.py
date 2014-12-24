import AbsReadData as RD
import AbsStopWords as SW
import codecs
from main import cpuTimer
import os
import shutil
import gensim

def makeStopWords(swfile="stopwords.txt"):
    return codecs.open(swfile,"r","utf-8").read().lower().strip().split(u",")


def convertBOW(fil,readData,stopWords,dic=0):
    try:
        txt=codecs.open(fil,"r","utf-8").read().lower().strip()
    except IOError:
        print "error reading file",fil
#    txt=readData.removeSymbol(txt)
    lines=txt.split(u"\n")
#    return lines
    words=[]

    for line in lines:
        line=readData.removeSymbol(line)
        words.extend([txt for txt in line.strip().split() if not (txt.isdigit() or len(txt)<=1)])

    if dic==0:
        words=stopWords.removeStopWord(words)
    else:
        words=dic.doc2bow(words)
#    stopWords=SW.StopWords(stopWords=makeStopWords())
    
    return words

def saveBOW(fil,bow,outfile,outdir="./"):
    hndl=open(outdir+outfile,"a")
    strs=fil.split("/")
    hndl.write("".join(strs[-2:])+u":"+str(bow)+u"\n")
    hndl.close()


def convertFiles(outdir,outfile="result.txt",filterFile="filter2.txt",**params):
    readData=RD.ReadData([],**params)
    stopWords=SW.SWFilter(0,filterFile=filterFile)    
    filterWords=stopWords.filterWords
    dic=gensim.corpora.Dictionary([filterWords])
    
    files=readData.files        
    timer=cpuTimer()
    timer.start()
    
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    shutil.copyfile(filterFile,outdir+"/"+filterFile)
    n=0    
    showCount=1000
    os.remove(outdir+outfile)
#    print filterWords
    for fil in files:
        bow=convertBOW(fil,readData,stopWords,dic=dic)
        saveBOW(fil,bow,outfile,outdir=outdir)
        n+=1
        if n%showCount==0:
            print "count",n,"time :",timer.show(stop=1),"(s)"
    
def main():
    convertFiles("/mnt/bowdata/filterWavelength/",targetDir="/mnt/rawdata",rec=1)   

if __name__=="__main__":
    main()
