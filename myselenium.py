from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
import time

options = Options() # ChromeOptions yerine Options
options.add_argument('allow-elevated-browser')
#options.add_argument('--start-fullscreen') tam ekran ile çalışmasını sağlar
options.add_experimental_option('w3c', True)
options.binary_location = 'C:\\Users\\arslan\\AppData\\Local\\Programs\\Opera\\opera.exe'

webdriver_service=service.Service('F:\\İndirilenler\\operadriver_win64\\operadriver.exe')
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url,options=options)
driver.get('https://www.google.com/')
driver.get('https://web.whatsapp.com/')
time.sleep(10)


driver.quit()