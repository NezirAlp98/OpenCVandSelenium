from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options() # ChromeOptions yerine Options
options.add_argument('allow-elevated-browser')


options.add_experimental_option('w3c', True)
options.binary_location = 'C:\\Users\\arslan\\AppData\\Local\\Programs\\Opera\\opera.exe'

webdriver_service=service.Service('F:\\İndirilenler\\operadriver_win64\\operadriver.exe')
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url,options=options)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app")
orta_boy=driver.find_element(By.CSS_SELECTOR,"input[value='Orta']")
zeytin=driver.find_element(By.CSS_SELECTOR,"input[value='zeytin']")
mantar=driver.find_element(By.CSS_SELECTOR,"input[value='mantar']")
print(orta_boy.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())
orta_boy.click()
zeytin.click()
mantar.click()
print(orta_boy.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())
time.sleep(2)