import time
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

