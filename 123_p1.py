from graphics import *
 
countProgress = 0
countTrailer = 0
countRetriever = 0
countExclude = 0

def main():

#make globle variable editable 
    global countProgress
    global countTrailer
    global countRetriever
    global countExclude

#main loop for multiple outcomes
    mainRepeateController = 'Y'
    while mainRepeateController=='Y':
        marksPass = 0
        marksDefer = 0
        marksFail = 0
    #repeate untill the total is corrected  
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
                
        #taking the result from UD function
        result = predictProgression(marksPass,marksDefer,marksFail)
        
        #temporally print result
        print (result)
        
        #print text file
        #textFile(result,marksPass,marksDefer,marksFail)
        
        #asking for multiple outcome
        mainRepeateController = input("Would you like to enter another set of data? \n please enter 'y' to continue \n 'q' to quite : ").upper()
        
    #print summury graph    
    printGraph()
    
    #temporally print the summery
    print(f"progress: {countProgress}\nRetriever: {countRetriever}\nTrailer: {countTrailer}\nexclude: {countExclude}") 
    
    
def predictProgression(marksPass,marksDefer,marksFail):
    
    #make globle variable editable
    global countProgress
    global countTrailer
    global countRetriever
    global countExclude
    
    #cheking the conditions, define the result and taking counts for summery
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
    #returning the result
    return result

#data validation
def getDataValidate(getDataFor):
#repeate untill mark is recorded in expected range
    loopController= 0
    while(loopController==0):
        #repeate untill mark is recorded under integer
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
    #returning the value for relevent catogory
    return tempMark
    
#printing the graph using graphics.py    
def printGraph():
    histogramWin = GraphWin("Histogram",845,600)
    
#Topic text
    topicText = Text(Point(422,25),"Histogram Results")
    topicText.setSize(22)
    topicText.draw(histogramWin)
    
#Draw Down Line
    downLine = Line(Point(50,501),Point(795,501))
    downLine.setArrow("both")
    downLine.setWidth(2)
    downLine.draw(histogramWin)
#--------------creating bars---------------------------    
    #Progress Bar
    labelProgressBar = Text(Point(175,70),"100")
    labelProgressBar.setSize(15)
    labelProgressBar.draw(histogramWin)
    
    labelProgressBar = Text(Point(175,520),"Progress")
    labelProgressBar.setSize(15)
    labelProgressBar.draw(histogramWin)

    progressBar = Rectangle(Point(100,500),Point(250,80))
    progressBar.setFill("lightgreen")
    progressBar.draw(histogramWin)
    
    #Trailer Bar
    labelProgressBar = Text(Point(340,70),"100")
    labelProgressBar.setSize(15)
    labelProgressBar.draw(histogramWin)
    
    labelProgressBar = Text(Point(340,520),"Trailer")
    labelProgressBar.setSize(15)
    labelProgressBar.draw(histogramWin)

    TrailerBar = Rectangle(Point(265,500),Point(415,80))
    TrailerBar.setFill("lightblue")
    TrailerBar.draw(histogramWin)
    
    
    #Retriever Bar
    labelProgressBar = Text(Point(505,70),"100")
    labelProgressBar.setSize(15)
    labelProgressBar.draw(histogramWin)
    
    labelProgressBar = Text(Point(505,520),"Retriever")
    labelProgressBar.setSize(15)
    labelProgressBar.draw(histogramWin)
    
    retrieverBar = Rectangle(Point(430,500),Point(580,80))
    retrieverBar.setFill("lightyellow")
    retrieverBar.draw(histogramWin)
    
    #Exclude Bar
    labelProgressBar = Text(Point(670,70),"100")
    labelProgressBar.setSize(15)
    labelProgressBar.draw(histogramWin)
    
    labelProgressBar = Text(Point(670,520),"Exclude")
    labelProgressBar.setSize(15)
    labelProgressBar.draw(histogramWin)
    
    excludeBar= Rectangle(Point(595,500),Point(745,80))
    excludeBar.setFill("pink")
    excludeBar.draw(histogramWin)
    
#show total
    labelProgressBar = Text(Point(422,570),"33 Outcomes in total")
    labelProgressBar.setSize(20)
    labelProgressBar.draw(histogramWin)
    
#Show histogram Window
    histogramWin.getMouse()
    histogramWin.close()
            
#run the main function
#if __name__ == "__main__":
#    main()

printGraph()