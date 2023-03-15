from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#PATH = r'C:\Users\03961465\PycharmProjects\webScraping\Prueba'
driver = webdriver.Firefox()

driver.get('https://www.empleate.gob.es/empleo/#/')
time.sleep(4)

text_area = driver.find_element(By.ID,"searchbar")
search_button = driver.find_element(By.CLASS_NAME, "btn-search")

text_area.send_keys("Software")
search_button.click()

time.sleep(5)

job_apply = driver.find_element(By.XPATH, '/html/body/section[2]/section/div[4]/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div[1]/p[2]/a')

job_apply.click()

time.sleep(5)
download_button = driver.find_element(By.CLASS_NAME, "btnDescargarPdf")
download_button.click()

print("Acabado:")
time.sleep(10)
driver.quit()
