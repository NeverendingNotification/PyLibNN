import makeCorpus as mC
import gensim.models as models
import os
modelFile="model.lsi"
resultFile="result.txt"
topicFile="topic.txt"

class makeModel:
    def __init__(self,dire,filterFile="filter.txt",num_topics=5):
        self.targetDir=dire
        self.filterFile=filterFile
        self.num_topics=num_topics

    def bow2Model(self):
        targetDir=self.targetDir
        
        corp=mC.corpusFile(targetDir+resultFile)
        model=models.lsimodel.LsiModel(corp,num_topics=self.num_topics)
        model.save(targetDir+modelFile)

    def reformTopic(self,model):
        topics=model.print_topics()
        dic=open(self.targetDir+self.filterFile,"r").read().strip().split("\n")        
        ret=[]
        for topic in topics:
            txt=""
            for sets in topic.split("+"):
                pair=sets.split("*")
                index=int("".join(pair[1].split('"')))
                txt+=pair[0]+"*"+dic[index]+"+"
            ret.append(txt[:-1]+"\n")
        
        return ret
        
    def bow2Vector(self,output):
        model=models.LsiModel.load(self.targetDir+modelFile)
        #Make topic file
        hndl=open(self.targetDir+topicFile,"w")
        for txt in self.reformTopic(model):
            hndl.write(txt)
        hndl.close()
        #convert bow to vector with model
        corp=mC.corpusFile2(self.targetDir+resultFile)
        if os.path.exists(self.targetDir+output):
            os.remove(self.targetDir+output)
        hndl=open(self.targetDir+output,"a")
        n=0
        txt=""
        for name,val in corp:
            vals=model[val]
            if len(vals)==0:
                out="0"
            else:
                out=str([x[1] for x in vals])
            txt+=name+":"+out+"\n"
            n+=1
            if n%10==0:
                hndl.write(txt)
                txt=""
        else:
            hndl.write(txt)
        hndl.close()

    def clasify(self,ofile,infile):
        model=models.LsiModel.load(self.targetDir+modelFile)
        n_topic=len(model.print_topics())
        corp=mC.corpusFile2(self.targetDir+infile)
        ohndl=open(self.targetDir+ofile,"w")
        counts=[0]*n_topic
        count=0
        for name,val in corp:
            if val!=0:
                abscounts=[abs(cnt) for cnt in val]
                index=abscounts.index(max(abscounts))
                counts[index]+=1
            count+=1
        ohndl.write("Total count ="+str(count)+"\n")
        sumcnt=sum(counts)
        ohndl.write("Total count for Astronomy="+str(sumcnt)+"\n")
        ohndl.write("Number of Each Topics are\n")
        topics=self.reformTopic(model)
        for n,cnt in enumerate(counts):
            ohndl.write("Topic:"+str(n)+"\n")
            ohndl.write("  "+topics[n])
            ohndl.write("  "+str(cnt)+"("+str((100.0*cnt)/sumcnt)+"%)\n")
        ohndl.close()
        

def main(target="/mnt/bowdata/filterWavelength/",filterFile="filter.txt"):
    output="output.txt"
    classfile="class.txt"
    model=makeModel(target,filterFile=filterFile)
    if not os.path.exists(target+modelFile):
        model.bow2Model()
    if not os.path.exists(target+output):
        model.bow2Vector(output)
    model.clasify(classfile,output)
    
    
        
if __name__=="__main__":
    main()


