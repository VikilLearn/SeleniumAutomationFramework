import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import utilities.custom_logger as cl
from time import sleep
from datetime import datetime, date, timedelta
import os


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'id':
            return By.ID
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'tag':
            return By.TAG_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        elif locator_type == 'partial_link':
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.info("Locator type '" + locator_type + "' not correct/supported", end='. ')
            return False


    def getElement(self, locator, locator_type='id'):        # Non default parameter follows default parameters
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.getByType(locator_type)
            element = self.driver.find_element(byType, locator)
            self.log.info('Element found with locator: ' + locator + ' and locatorType: ' + locator_type)
            return element
        except:
            self.log.info('#'* 10 + ' Element not found with locator: ' + locator + ' and locatorType: ' + locator_type)
            return False

    def getElementList(self, locator, locator_type='id'):        # Non default parameter follows default parameters
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.getByType(locator_type)
            element = self.driver.find_elements(byType, locator)
            self.log.info('Element list found with locator: ' + locator + ' and locatorType: ' + locator_type)
            return element
        except:
            self.log.info('#'* 10 + ' Element list not found with locator: ' + locator + ' and locatorType: ' + locator_type)
            return False

    def isElementPresent(self, locator='', locator_type='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locator_type)
            if element:
            # if element is not None:           ## As per tutor/trainer
                self.log.info('Element found with locator: ' + locator + ' and locatorType: ' + locator_type)
                return True
            else:
                self.log.info('Element not found with locator: ' + locator + ' and locatorType: ' + locator_type)
                return  False
        except:
            self.log.info('#'* 10 + ' Element not found with locator: ' + locator + ' and locatorType: ' + locator_type)
            return False


    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False


    def elementsPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if(len(elementList)) > 0:
                self.log.info('Element found with locator: ' + locator + ' and locatorType: ' + locator_type)
                return True
            else:
                self.log.info('Element not found with locator: ' + locator + ' and locatorType: ' + locator_type)
                return  False
        except:
            self.log.info('#'* 10 + ' Element not found with locator: ' + locator + ' and locatorType: ' + locator_type)
            return False

    def close(self):
        return close


    def waitForElement(self, locator, locator_type, timeout=10, poll_frequency=1):
        try:
            self.driver.implicitly_wait(0)
            self.log.info(f'Wait for max :: {timeout} :: seconds for element to be available.')

            byType = self.getByType(locator_type)
            wait = WebDriverWait(self.driver, timeout, poll_frequency,
                                              ignored_exceptions=[NoSuchElementException
                                                                , ElementNotVisibleException
                                                                , ElementNotSelectableException
                                                                , ElementClickInterceptedException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))

            self.log.info(f'Element located on the webpage:\n{element}')

            self.driver.implicitly_wait(3)
            return element

        except:
            self.log.info('#'* 10 + ' Element not found with locator: ' + locator + ' and locatorType: ' + locator_type)
            print_stack()                                   # Prints the trace entries
            return False


    def enterText(self, text, locator='', locator_type='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locator_type)
            element.send_keys(text)
            self.log.info('Sent data on the element with locator: ' + locator + ' and locatorType: ' + locator_type)
            return text
        except:
            self.log.info('#'* 10 + ' Cannot send data on the element with locator: ' + locator + ' and locatorType: ' + locator_type)
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        # Either provide element or a combination of locator and locatorType
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text


    def elementClick(self, locator='', locator_type='id', element=None):
        # Either provide element or a combination of locator and locatorType
        try:
            if locator:
                element = self.getElement(locator, locator_type)
            # element.click()
            self.driver.execute_script("arguments[0].click();", element)

            self.log.info('Click on element with locator: ' + locator + ' and locatorType: ' + locator_type)
        except:
            self.log.info('#'* 10 + ' Cannot click on the element with locator:' + locator + ' and locatorType: ' + locator_type)
            print_stack()

    def screenshot(self, resultMessage):
        fileName = resultMessage + str(datetime.now().strftime('%Y%m%d%H%M%S')) + '.png'
        screenshotDir = '..//screenshots/'
        relativeFileName = screenshotDir + fileName
        currentDir = os.path.dirname(__file__)
        destFile = os.path.join(currentDir, relativeFileName)
        destDir = os.path.join(currentDir, screenshotDir)
        try:
            if not os.path.exists(destDir):
                os.makedirs(destDir)
            self.driver.save_screenshot(destFile)
            self.log.info('Screenshot saved to directory: ' + destDir)
        except Exception as e:
            self.log.error('#'* 10 + ' Exception occured: ' + e)
            print_stack()


    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")


    def switchToFrame(self, id="", name="", xpath="", index=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        elif xpath:
            self.driver.switch_to.frame(self.getElement(locator=xpath, locator_type='xpath'))
        else:
            self.driver.switch_to.frame(index)


    def switchToDefaultContent(self):
        """
        Switch to default content

        Parameters:
            None
        Returns:
            None
        Exception:
            None
        """
        self.driver.switch_to.default_content()


    def SwitchFrameByIndex(self, locator, locatorType="xpath"):

        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """
        result = False
        try:
            iframe_list = self.getElementList("//iframe", locatorType="xpath")
            self.log.info("Length of iframe list: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchToFrame(index=iframe_list[i])
                result = self.isElementPresent(locator, locatorType)
                if result:
                    self.log.info("iframe index is:")
                    self.log.info(str(i))
                    break
                self.switchToDefaultContent()
            return result
        except:
            print("iFrame index not found")
            return result


    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value


    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator=locator, locator_type=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled