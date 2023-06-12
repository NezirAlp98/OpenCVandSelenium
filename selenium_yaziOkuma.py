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
driver.maximize_window()
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
seckinMaddeAlani=driver.find_element(By.ID,"mp-tfa")
seckinMaddeYazisi=seckinMaddeAlani.text
seckinMaddeYazisi=seckinMaddeYazisi.split(",")[0]
print(f"Seçkin madde: {seckinMaddeYazisi}")

kaliteliMadde=driver.find_element(By.ID,"mp-tfp").text
kaliteliMadde=kaliteliMadde.split(",")[0]
print(f"Kaliteli madde: {kaliteliMadde}")
