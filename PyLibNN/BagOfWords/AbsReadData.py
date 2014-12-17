import os
from BOWData import DataSets
class ReadData:
    #Reading data + removing symbols in the text
    def __init__(self,files,targetDir=0,removeSyms=[".",",","'",'"'],exts=".txt"):
        #If targetDir is set find files in target directory
        if targetDir!=0:
            files=[os.path.join(targetDir,fil) for fil in os.listdir(targetDir) if fil.endswith(exts)]
        self.files=files        
        self.removeSyms=removeSyms
    def removeSymbol(self,txt):
        for sym in self.removeSyms:
            txt="".join(txt.split(sym))
        return txt

    def readData(self):
        dataSets=DataSets()
        for filename in self.files:
            lines=open(filename).read().strip().split("\n")
            words=[]
            for line in lines:
                line=self.removeSymbol(line)
                words.extend(line.strip().split())
            dataSets.addData(filename,words)
#            outData.append(BOWDataRaw(filename,words))
        return dataSets
        
