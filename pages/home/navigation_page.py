# To run the test go to command prompt. login_page.py location and execute following command: py.test -v login_tests.py --browser chrome --html=chromeReport.html

from base.selenium_driver import SeleniumDriver
from time import sleep
import logging
import utilities.custom_logger as cl
from traceback import print_stack
from base.basepage import BasePage


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)            ## Very important as we have inherited SeleniumDriver class
        self.driver = driver


    #Locators and locator type
    home_nav = 'HOME'
    all_courses_nav = 'ALL COURSES'
    my_courses_nav = 'MY COURSES'
    practice_nav = 'PRACTICE'
    user_settings_nav = 'My Account'
    support_nav = 'SUPPORT'

    def naviageToHome(self):
        self.elementClick(locator=self.home_nav, locator_type='link')

    def naviageToAllCourses(self):
        self.elementClick(locator=self.all_courses_nav, locator_type='link')

    def naviageToMyCourses(self):
        self.elementClick(locator=self.my_courses_nav, locator_type='link')

    def naviageToPractice(self):
        self.elementClick(locator=self.practice_nav, locator_type='link')

    def naviageToUserSettings(self):
        self.elementClick(locator=self.user_settings_nav, locator_type='link')

    def naviageToSupport(self):
        self.elementClick(locator=self.support_nav, locator_type='link')

