import undetected_chromedriver as uc
import time
import pandas as pd
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXPECTED

options = webdriver.ChromeOptions()
options.add_argument('--disable-popup-blocking')
chrome = uc.Chrome(options=options)
wait = WebDriverWait(chrome, 30)           # Content on website loaded dynamically using JavaScript - waits for the elements to be present


def scrape_properties():
    properties_All = wait.until(EXPECTED.presence_of_all_elements_located((By.XPATH, '//div[@class="cardCon"]')))


    for properties in properties_All:
        property_data = {}
        property_data["price"] = properties.find_element(By.XPATH, './/div[@class="listingCardPrice"]').text    # returns all text within the element
        
        icon_elements = properties.find_elements(By.XPATH, './/div[@class="listingCardIconTopCon"]')
        # Iterating trhough the found elements and extract information based on position and content
        # There are two elements in the list, bedrooms being first, and bathrooms being second
        if len(icon_elements) == 2:
            property_data["bedrooms"] = icon_elements[0].text
            property_data["bathrooms"] = icon_elements[1].text
        elif len(icon_elements) == 1:
            property_data["bedrooms"] = 'PARKING'
            property_data["bathrooms"] = 'PARKING'      # Realtor.ca lists parking lots for sale as well and only list the number of bathrooms which is 0 - assigning the bed/bath data as Parking

        if properties.find_elements(By.XPATH, ".//div[@class='listingCardAddress']"):
            property_data["address"] = properties.find_element(By.XPATH, ".//div[@class='listingCardAddress']").text

        all_properties.append(property_data)        # Adding the property data dictionaries into a single list


if __name__ == "__main__":
    all_properties = []
    chrome.get("https://www.realtor.ca/map#ZoomLevel=11&Center=43.708087%2C-79.376385&LatitudeMax=43.91174&LongitudeMax=-78.85076&LatitudeMin=43.50374&LongitudeMin=-79.90201&view=list&Sort=6-D&GeoIds=g30_dpz89rm7&GeoName=Toronto%2C%20ON&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=0&Currency=CAD")
    scrape_properties()
    dataFrame = pd.DataFrame.from_dict(all_properties)       # First page
    

    for i in range(2, 51):                            # Second -> 50th Page
        handles_before = chrome.window_handles
        chrome.execute_script(f"window.open('https://www.realtor.ca/map#ZoomLevel=11&Center=43.708087%2C-79.376385&LatitudeMax=43.88082&LongitudeMax=-79.05332&LatitudeMin=43.53486&LongitudeMin=-79.69945&view=list&CurrentPage={str(i)}&Sort=6-D&GeoIds=g30_dpz89rm7&GeoName=Toronto%2C%20ON&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=0&Currency=CAD','_blank')")
        handles_after = chrome.window_handles
        new_handle = [handle for handle in handles_after if handle not in handles_before][0]
        chrome.switch_to.window(new_handle)
        scrape_properties()
        if len(all_properties) == (12*i):
            print(f"Good: {i}")
        dataFrame = pd.DataFrame.from_dict(all_properties)
        time.sleep(0.25)
        
    
    print(dataFrame)
    dataFrame.to_excel('properties.xlsx')

