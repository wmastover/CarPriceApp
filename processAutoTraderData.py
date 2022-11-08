import os
from processAutoTraderDataResources import deleteDuplicateLines
from processAutoTraderDataResources import getTrendLineParams



def processCarData(folderName):
    #get directory location
    directory = os.getcwd()
    folderDirectory = (directory + "/" + folderName)

    #for each text file in the folder, delete duped lines and get trend line params
    for file in os.listdir(folderDirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            print(filename)
            fileLocation = folderDirectory + "/" + filename

            deleteDuplicateLines(fileLocation)
            getTrendLineParams(fileLocation)


        
processCarData("Ford Fiesta")