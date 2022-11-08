from distutils.log import error
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService # Similar thing for firefox also!
#from subprocess import CREATE_NO_WINDOW # This flag will only be available in windows

# Define your own service object with the `CREATE_NO_WINDOW ` flag
# If chromedriver.exe is not in PATH, then use:
# ChromeService('/path/to/chromedriver')
chromedriver = ChromeDriverManager().install()
#chrome_service = ChromeService(chromedriver)
#chrome_service.creationflags = CREATE_NO_WINDOW


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

#options.add_argument('--headless')


def sendError(errorMessage):
    print(errorMessage)



def getMakeList():
    f = open("makeList.txt", "r")

    for x in f:
        getModelList(x.replace("\n", ""))



def getModelList(make):
    driver = webdriver.Chrome(chromedriver, chrome_options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.set_window_size(1000, 3000)
    #create driver

    #try get linkedin login page
    try:
        driver.get("https://www.autotrader.co.uk/car-search?sort=relevance&postcode=tq122pu" + "&make=" + make )
        time.sleep(10)
        
    except:
        sendError("unable to load page")

    flyouts = driver.find_elements(By.CLASS_NAME, "js-flyout")

    for x in flyouts:
        
        if x.get_attribute("data-temp") == "model-flyout":
            print(" ")
            print("make:" + make)

            f = open(make + ".txt", "w")
            flyout__options = x.find_element(By.CLASS_NAME, "sf-flyout__options")
            
            try:
                y = flyout__options.find_elements(By.CLASS_NAME,("value-button"))
                
                for i in y:
                    f.write(i.get_attribute("data-selected-value") + "\n")
                    

            except:
                print("error")

getMakeList()