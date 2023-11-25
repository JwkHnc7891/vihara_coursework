from graphics import *
 
countProgress = 0
countTrailer = 0
countRetriever = 0
countExclude = 0

def main():

    global countProgress
    global countTrailer
    global countRetriever
    global countExclude

    mainRepeateController = 'Y'
    while mainRepeateController=='Y':
        marksPass = 0
        marksDefer = 0
        marksFail = 0
        
        loopControllerTotalCheck = True
        while loopControllerTotalCheck:
            getDataFor = "Pass"
            marksPass = getDataValidate(getDataFor)
            getDataFor = "Defer"
            marksDefer = getDataValidate(getDataFor)
            getDataFor = "fail"
            marksFail = getDataValidate(getDataFor)
            
            markTotal = marksPass+marksDefer+marksFail
            if markTotal!=120:
                print("Total error!")
                loopControllerTotalCheck = True
            else:
                loopControllerTotalCheck = False
        
        result = predictProgression(marksPass,marksDefer,marksFail)
        print (result)
        
        textFile(result,marksPass,marksDefer,marksFail)
        
        mainRepeateController = input("Would you like to enter another set of data? \n please enter 'y' to continue \n 'q' to quite : ").upper()
        
    #printGraph()
    #print ("progress: " +str(countProgress)+ "\nRetriever: "+str(countRetriever)+ "\nTrailer: "+str(countTrailer)+"\nexclude: "+str(countExclude))
    print(f"progress: {countProgress}\nRetriever: {countRetriever}\nTrailer: {countTrailer}\nexclude: {countExclude}") 
    
def textFile(result,marksPass,marksDefer,marksFail):
    txtFile = open("resultLog.txt","a")
    txtFile.write(f"\n{result}, {marksPass}, {marksDefer}, {marksFail}")
    txtFile.close()
            
def predictProgression(marksPass,marksDefer,marksFail):

    global countProgress
    global countTrailer
    global countRetriever
    global countExclude

    if marksFail>=80: 
        result= "Exclude"
        countExclude = countExclude+1
    elif marksPass == 120: 
        result = "Progress"
        countProgress = countProgress + 1
    elif marksPass == 100: 
        result = "Pregress - Module trailer"
        countTrailer = countTrailer = 1
    elif marksPass == 80 or marksPass == 60 or marksPass == 40 or marksPass == 20 : 
        result = "Do not progress - Module retriever"
        countRetriever = countRetriever + 1
    
    return result

def getDataValidate(getDataFor):
    loopController= 0
    while(loopController==0):
        while (loopController==0):
            try:
                tempMark = int(input('Enter marks for '+ getDataFor+ ': '))
                loopController= 1
            except:
                print ("Please enter an integer value!")
                loopController= 0
        loopController=0    
        if tempMark==0 or tempMark==20 or tempMark==40 or tempMark==60 or tempMark==80 or tempMark==100 or tempMark==120:
            loopController= 1
        else:
            print ("Please enter marks under valid value set!")
            loopController=0
    return tempMark

if __name__ == "__main__":
    main()