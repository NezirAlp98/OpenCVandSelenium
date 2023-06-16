from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
dropdown=driver.find_element(By.ID,"odeme-tipi")
odeme=Select(dropdown)
odeme_tipleri=odeme.options #web element listesi her bir option tag

for tip in odeme_tipleri:
    print(tip.text)
time.sleep(2)
odeme.select_by_visible_text("Kredi Kartı")
time.sleep(2)
odeme.select_by_index(3)
time.sleep(2)


