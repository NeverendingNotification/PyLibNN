import os
from BOWData import DataSets
import codecs
class ReadData:
    #Reading data + removing symbols in the text
    def __init__(self,files,targetDir=0,removeSyms=[u".",u",",u"'",u'"',u'(',u')',u'&',u':',u';',u'[',u']',\
                                                    u'{',u'}'],exts=u".txt",rec=0):
        #If targetDir is set find files in target directory
        if targetDir!=0:
            if rec==0:
                files=[os.path.join(targetDir,fil) for fil in os.listdir(targetDir) if fil.endswith(exts)]
            else:
                dirs=[os.path.join(targetDir,fil) for fil in os.listdir(targetDir) if os.path.isdir(os.path.join(targetDir,fil))]

                files=[]
                for dire in dirs:
                    files.extend([os.path.join(dire,fil) for fil in os.listdir(dire)])
#        self.files=files
        self.files=files[:]
        self.removeSyms=removeSyms
    def removeSymbol(self,txt):
        for sym in self.removeSyms:
            txt="".join(txt.split(sym))
        return txt

    def readData(self):
        dataSets=DataSets()
        for filename in self.files:
            lines=codecs.open(filename,"r","utf-8").read().lower().strip().split(u"\n")
            words=[]
            for line in lines:
                line=self.removeSymbol(line)
                words.extend([txt for txt in line.strip().split() if not txt.isdigit()])
            dataSets.addData(filename,words)
#            outData.append(BOWDataRaw(filename,words))
        return dataSets
        
