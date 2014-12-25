
class corpusFile:
    def __init__(self,filename):
        self.filename=filename

    def __iter__(self):
        for line in open(self.filename):
            yield eval(line.split(":")[-1])

class corpusFile2:
    def __init__(self,filename):
        self.filename=filename

    def __iter__(self):
        for line in open(self.filename):
            strs=line.split(":")
            yield strs[0],eval(strs[1])
    
