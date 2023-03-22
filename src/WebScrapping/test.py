from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Firefox()
driver.get("https://www.empleate.gob.es/empleo/#/trabajo?search=software&pag=0")
# Espera a que se cargue la página
time.sleep(5)
#links = driver.find_elements(By.XPATH,"//*[contains(@title,'Titulo de la oferta')]") # Selecciona los enlaces de las ofertas por su clase
main_window = driver.current_window_handle # Guarda la pestaña principal

for i in range(0,9):
    link = driver.find_elements(By.XPATH,"//*[contains(@title,'Titulo de la oferta')]")[i] # Selecciona los enlaces de las ofertas por su clase
    driver.execute_script("arguments[0].scrollIntoView(true);", link)
    #si se usa link.click se buguea
    #driver.execute_script("arguments[0].click();", link)
    driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('click', {ctrlShift: true}));", link)
    time.sleep(3)
    download_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btnDescargarPdf")))
    download_button.click()
    driver.switch_to.window(main_window)
    time.sleep(1)
    #Cambiamos a la anterior ventana
#driver.switch_to.window(main_window) # Vuelve a la pestaña principal