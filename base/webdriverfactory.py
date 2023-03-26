from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser


    def getWebDriverInstance(self):
        url = 'https://courses.letskodeit.com/'
        if self.browser == 'edge':
            print("Running tests on Edge")
            drvr_path = 'C:\\Users\\vikil.biyala\\PycharmProjects\\drivers\\msedgedriver.exe'
            srvc = Service(executable_path=drvr_path)
            driver = webdriver.Edge(service=srvc)

        elif self.browser == 'chrome':
            print("Running tests on chrome")
            drvr_path = 'C:\\Users\\vikil.biyala\\PycharmProjects\\drivers\\chromedriver.exe'
            srvc = Service(executable_path=drvr_path)

            # options = webdriver.ChromeOptions()
            # options.add_experimental_option('excludeSwitches', ['enable-logging'])
            # driver = webdriver.Chrome(options=options, service=srvc)
            driver = webdriver.Chrome(service=srvc)
        else:
            print('Selected incorrect browser.')

        driver.get(url)
        driver.implicitly_wait(5)
        driver.maximize_window()
        return driver

