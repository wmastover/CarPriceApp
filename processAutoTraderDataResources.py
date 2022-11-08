#this file will run in each make / model folder.
#For each year, it will go through data files, remove duplicates, and output a trend
#line equation,
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def deleteDuplicateLines(filename):

    #open file in read mode
    file = open(filename, "r")

    #initialise array to store unique lines of the file
    lines= []

    #add all unduplicated lines to an array
    counter = 0
    for line in file:
        if line not in lines:
            lines.append(line)
        else:
            counter = counter + 1
    
    print(str(counter) + " Duplicate lines removed")
            
    file.close()

    #overwrite file with the lines array
    file = open(filename, "w")
    for line in lines:
        file.write(line)
    file.close()

def getTrendLineParams(filename):
        
    #intialise file in read mode
    f = open(filename, "r")
    
    # initalise arrays to store mileage and price for all records in the file
    miles = []
    price = []

    #go through each record in the file and add to mile / price arrays
    for line in f:
        lineArray = line.split(",")
        try:
            miles.append(int(lineArray[1]))
            price.append(int(lineArray[2].replace("£","")))
        except:
            print("error with line: " + line)

    f.close()

    #declare function of exponential trend line
    def func(x, a, b, ):
        return (a * np.exp(-b * x))
 
    #curve fit to data, popt is the array storing the optimum values of a and b
    popt, pcov = curve_fit(func, miles, price, p0=[10000, 0.0005])

    print("Parameter a: " + str(popt[0]))  
    print("Parameter b: " + str(popt[1]))
    

    #generate trendline data points
    price2 = []
    for i in miles:
       price2.append(func(i, popt[0], popt[1]))
    
    #show graph with data points and trendline
    plt.plot(miles, price, "ko")
    plt.plot(miles, price2, "ko", color="green") 
    plt.show()

    return(popt[0], popt[1])


