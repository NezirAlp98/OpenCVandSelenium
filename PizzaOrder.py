from selenium.webdriver.support.select import Select
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

def order():
    driver.find_element(By.ID,"siparis").click()

def readMessage():
    return driver.find_element(By.ID,"mesaj").text

order()
message=readMessage()
assert message=="Müşteri ismi girmediniz"
time.sleep(2)

name="Tom Cruise"
driver.find_element(By.ID,"musteri-adi").send_keys(name)
order()
message=readMessage()
assert message=="Pizza boyu seçmediniz"
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"input[value='Küçük']").click()
order()
message=readMessage()
assert message=="Ödeme tipi seçmediniz"
time.sleep(2)

dropdown=driver.find_element(By.ID,"odeme-tipi")
odeme=Select(dropdown)
odeme.select_by_index(2)
order()
message=readMessage()
assert message=="Siparişiniz alındı"
time.sleep(2)

