from numpy import product
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

#go through an autotrader search and get the   
def getCars(make, model, year):
        fileName = (model + " " + year + ".txt")

        print("(. Y .)")

        f = open(fileName, "a")
        chromedriver = ChromeDriverManager().install()
        driver = webdriver.Chrome(chromedriver )

        driver.get("https://www.autotrader.co.uk/car-search?sort=relevance&postcode=tq122pu" + "&make=" + make + "&model=" + model + "&exclude-writeoff-categories=on" + "&year-from=" + year + "&year-to=" + year )
        time.sleep(5)

        iframe = driver.find_element(By.ID, "sp_message_iframe_687971")

        driver.switch_to.frame(iframe)
        Buttons = driver.find_elements(By.TAG_NAME, "button")

        for x in Buttons:
            if x.get_attribute("title") == "Accept All":
                x.click()
                
        time.sleep(5)
        
        done = False
        while done == False:
            time.sleep(5)
            productCards = driver.find_elements(By.CLASS_NAME, "search-page__result")


            for x in productCards:

                link = x.find_element(By.CLASS_NAME, "listing-fpa-link").get_attribute("href")
                
                imageLink = x.find_element(By.CLASS_NAME, "product-card-image__main-image").get_attribute("src")
                
                productCardInfo = x.find_element(By.CLASS_NAME, "product-card-content__car-info")
                priceWrapper = productCardInfo.find_element(By.CLASS_NAME,"product-card-pricing__price")

                try:
                    if priceWrapper.find_element(By.CLASS_NAME, "product-card-pricing__small-copy") != None: 
                        print("lease")
                except:
                    price = priceWrapper.find_element(By.TAG_NAME,"span").text
                    keySpecs = x.find_element(By.CLASS_NAME, "listing-key-specs")
                    keySpecisList = keySpecs.find_elements(By.TAG_NAME, "li")

                    line = keySpecisList[0].text[:4] +  ", " +  keySpecisList[2].text.replace(" miles", "").replace(",","") + ", " + price.replace(",", "") + ", " + link + ", " + imageLink 
                    f.write(line + "\n")
            
            try:
                driver.find_element(By.CLASS_NAME, "pagination--right__active").click()
            except:
                done= True
                f.close()
                driver.close()

    
#getCars("Ford","Fiesta", "2012")