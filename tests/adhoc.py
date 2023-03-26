import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

url = 'https://www.letskodeit.com/'
drvr_path = 'C:\\Users\\vikil.biyala\\PycharmProjects\\drivers\\chromedriver.exe'
srvc = Service(executable_path=drvr_path)
driver = webdriver.Chrome(service=srvc)
driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()

print('Page is up and running!')
element = driver.find_element(by=By.LINK_TEXT, value='ALL COURSES')
# element.click()
driver.execute_script("arguments[0].click();", element)

time.sleep(1)
driver.quit()