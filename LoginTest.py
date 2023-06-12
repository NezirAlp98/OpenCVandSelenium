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
def login(userName,password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID,"username").send_keys(userName)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,"button.radius").click()
    time.sleep(2)
    text_warning=driver.find_element(By.ID,"flash").text
    return text_warning
    

mesaj=login("asdf","SuperSecretPassword!")
assert "Your username is invalid!"in mesaj


mesaj=login("tomsmith","123sdasdf!")
assert "Your password is invalid!" in mesaj

mesaj=login("tomsmith","SuperSecretPassword!")
assert "You logged into a secure area!" in mesaj

link=driver.current_url
assert "secure" in link

driver.find_element(By.CSS_SELECTOR,"a.button").click()
time.sleep(1)
