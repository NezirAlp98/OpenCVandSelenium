from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 

options = Options() # ChromeOptions yerine Options
options.add_argument('allow-elevated-browser')

options.add_experimental_option('w3c', True)
options.binary_location = 'C:\\Users\\arslan\\AppData\\Local\\Programs\\Opera\\opera.exe'

webdriver_service=service.Service('F:\\İndirilenler\\operadriver_win64\\operadriver.exe')
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url,options=options)
driver.get("http://duckduckgo.com")
driver.maximize_window()
arama_kutusu=driver.find_element(By.ID,"search_form_input_homepage")
arama_kutusu.send_keys("selenium")
driver.find_element(By.ID,"search_button_homepage").click()
driver.find_element(By.ID,"r1-1").click()