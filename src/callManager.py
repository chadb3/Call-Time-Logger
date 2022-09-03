from src.Call import Call
from datetime import datetime

class callManager:
    # constructor
    def __init__(this):
        this.initTime=datetime.now()
        this.timeFirstCall=0
        this.callList = []
        this.callCount = 0
    # add a new call to the list
    def newCall(this):
        if(this.callCount>0):
            #debug
            #print("HIT")
            if(not this.callList[this.callCount-1].callEnded):
                this.callList[this.callCount-1].setEndTime()
        this.callCount+=1
        this.callList.append(Call(this.callCount))
        if(len(this.callList)==1 and this.timeFirstCall==0):
            this.timeFirstCall=datetime.now()
    # prints the list of calls
    def printCalls(this):
        for call in this.callList:
            print(call)
    #"Ends" current call - sets the end time for the call. 
    def endCurrentCall(this):
        if(len(this.callList)>0):
            #print("DEBUG: CALLED!")
            this.callList[len(this.callList)-1].setEndTime()
        else:
            print("No Calls to End")
    # shows the duration of the current call
    def askDuration(this):
        #print("asking current delta/Duration")
        lenList=len(this.callList)
        if(lenList>0):
            this.callList[lenList-1].currentDelta()
    # gets the time to the first call from initilization 
    def getTimeToFirstCall(this):
        print("Time to first call")
        if(len(this.callList)==1):
            #print("LEN=1")
            print("Time to First: {}".format(str(this.timeFirstCall-this.initTime)[0:7]))
    # function to remove a call from the list
    def removeCall(this, callNumber):
        print("Attempting to remove call: {}".format(callNumber))
        numCalls=len(this.callList)
        if(numCalls>0):
            this.callList.remove(this.callList[callNumber-1])
            this.callCount-=1
            for i in range(0,len(this.callList)):
                print(i)
                this.callList[i].setCallNumber(i+1)
                print(this.callList[i])
        else:
            print("NO CALLS TO REMOVE")
    # adjust endtime of call.
    # WIP.
    # example use case: forget to "end" the call, but know when it was ended.
    def adjustTimeOfCall(this,callNumber,timeIN):
        print("WIP")
        print("Adjusting time of Call: {}".format(callNumber))
    # prints the list of the calls with the end times rather than the durations
    def printCallsAlternate(this):
        for call in this.callList:
            call.print_alternate()
    # prints the call count.
    def printCallCount(this):
        print(len(this.callList))
    # WIP command set.
    # trying to figure out a way to create commands programmatically
    def commandBuilder(this):
        print("Building Commands for phoneNumberManager")
    # assumed to be int.
    # not for users
    def commandAPItest(this, index):
        index=int(index)
        #print(index)
        commands=[this.newCall,this.endCurrentCall,this.printCalls]
        #commands2={1:this.newCall(),2:this.endCurrentCall(),3:this.printCalls()}
        commands[index]()
        #print("sdf")
        #commands2[index]
        #this.printCallCount()