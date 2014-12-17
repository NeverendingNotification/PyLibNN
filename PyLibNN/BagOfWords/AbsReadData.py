import os
from BOWData import DataSets
import codecs
class ReadData:
    #Reading data + removing symbols in the text
    def __init__(self,files,targetDir=0,removeSyms=[u".",u",",u"'",u'"'],exts=u".txt"):
        #If targetDir is set find files in target directory
        if targetDir!=0:
            files=[os.path.join(targetDir,fil) for fil in os.listdir(targetDir) if fil.endswith(exts)]
#        self.files=files
        self.files=files[:50]
        self.removeSyms=removeSyms
    def removeSymbol(self,txt):
        for sym in self.removeSyms:
            txt="".join(txt.split(sym))
        return txt

    def readData(self):
        dataSets=DataSets()
        for filename in self.files:
            lines=codecs.open(filename,"r","utf-8").read().strip().split(u"\n")
            words=[]
            for line in lines:
                line=self.removeSymbol(line)
                words.extend(line.strip().split())
            dataSets.addData(filename,words)
#            outData.append(BOWDataRaw(filename,words))
        return dataSets
        
