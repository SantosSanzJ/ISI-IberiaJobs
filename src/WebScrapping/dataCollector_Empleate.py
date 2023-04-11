from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from msedge.selenium_tools import Edge, EdgeOptions
from winreg import *
import time
import random 
import json
import os

# Load the JSON document from the file
with open('../secrets.json') as f:
    data = json.load(f)
dirname = os.path.abspath(os.getcwd())

download_dir = os.path.join(dirname,"pdf_Files")

with OpenKey(HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice") as key:
    browser = QueryValueEx(key, 'Progid')[0]

if 'FirefoxURL' in browser:
    firefox_options = webdriver.FirefoxOptions()
    prefs = {
    "browser.download.folderList": 2,
    "browser.download.dir": download_dir,
    "browser.helperApps.neverAsk.saveToDisk": "application/pdf"
    }
    for option, value in prefs.items():
        firefox_options.set_preference(option, value)
    driver = webdriver.Firefox(options=firefox_options)

else:
    options = EdgeOptions()
    options.use_chromium = True
    options.add_experimental_option("prefs", {"download.default_directory": download_dir})
    driver = Edge(options=options)

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
    with open('../secrets.json', 'w') as f:
        json.dump(data, f)
        print("Avanzando a la página: " + str(data['EmpleatePage']))
    time.sleep(random.uniform(2.0, 5.0))