from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from msedge.selenium_tools import Edge, EdgeOptions
import time
import random 
import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
def get_configured_driver():
    '''Returns a configured driver for the browser that the user has set as default.'''
    
    download_dir = os.path.join(current_directory,"pdf_Files")
    firefox_options = webdriver.FirefoxOptions()
    prefs = {
    "browser.download.folderList": 2,
    "browser.download.dir": download_dir,
    "browser.helperApps.neverAsk.saveToDisk": "application/pdf"
    }
    for option, value in prefs.items():
        firefox_options.set_preference(option, value)
    if os.path.isdir('/proc/self/'):
        print("Running on Docker")
        driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub",
        options=firefox_options)
    else:
        print("Running on local")
        driver = webdriver.Firefox(options=firefox_options)
    return driver

def browser_empleate(driver):
    '''Opens the browser and navigates to the Empleate website to extract ppdf of the jobs offers.'''
    with open(os.path.join(current_directory,'../secrets.json')) as f:
        data = json.load(f)
    driver.get("https://www.empleate.gob.es/empleo/#/trabajo?search=programador&pag=" + str(data['EmpleatePage']))
    time.sleep(5)

    main_window = driver.current_window_handle # Guarda la pestaña principal
    while 1:
        for i in range(0,10):
            link = driver.find_elements(By.XPATH,"//*[contains(@title,'Titulo de la oferta')]")[i] # Selecciona los enlaces de las ofertas por su clase
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            #si se usa link.click se buguea, sin script
            driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('click', {ctrlShift: true}));", link)
            
            time.sleep(random.uniform(3.0,5.0))
            download_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btnDescargarPdf")))
            download_button.click()
            driver.switch_to.window(main_window)
            time.sleep(random.uniform(1.0,2.0))
        
        driver.get("https://www.empleate.gob.es/empleo/#/trabajo?search=programador&pag="+ str(data['EmpleatePage']))
        time.sleep(random.uniform(2.0, 4.0))
        btn_siguiente = driver.find_element(By.XPATH,"//*[contains(@title,'Siguiente')]")
        btn_siguiente.click()
        data['EmpleatePage'] += 1
        with open(os.path.join(current_directory, '../secrets.json'), 'w') as f:
            json.dump(data, f)
            print("Avanzando a la página: " + str(data['EmpleatePage']))
        time.sleep(random.uniform(2.0, 5.0))

if __name__ == "__main__":
    driver = get_configured_driver()
    print("Driver Started")
    browser_empleate(driver)