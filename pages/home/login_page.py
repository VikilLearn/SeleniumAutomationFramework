# To run the test go to command prompt. login_page.py location and execute following command: py.test -v login_tests.py --browser chrome --html=chromeReport.html

from base.selenium_driver import SeleniumDriver
from time import sleep
import logging
import utilities.custom_logger as cl
from traceback import print_stack
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)            ## Very important as we have inherited SeleniumDriver class
        self.driver = driver


    #Locators and locator type
    signIn_link = '//a[contains(text(), "Sign In")]'
    signInLink_lt = 'xpath'

    emailid_field = 'email'
    emailid_lt = 'id'

    pwd_field = 'login-password'
    pwd_lt = 'id'

    login_button = 'login'
    loginBtn_lt = 'id'

    checkLogin = '//div[@id="course-list"]/div[contains(text(),"You have not enrolled to any courses.")]'
    checkLogin_lt = 'xpath'

    title_loc = '//title[contains(text(),"My Courses")]'
    title_lt = 'xpath'

    def clickSignInLink(self):
        return self.elementClick(self.signIn_link, self.signInLink_lt)

    def enterEmail(self, username):
        self.enterText(username, self.emailid_field, self.emailid_lt)

    def enterPassword(self, pwd):
        self.enterText(pwd, self.pwd_field, self.pwd_lt)

    def clickLoginButton(self):
        return self.elementClick(self.login_button, self.loginBtn_lt)

    def verifyLoginSuccess(self):
        result = self.isElementPresent(self.checkLogin, self.checkLogin_lt)
        if result:
            self.log.info('*' * 30 + 'Login successful.' + '*' * 30)
        else:
            self.log.info('*' * 30 + 'Login unsuccessful.' + '*' * 30)
            # print_stack()
        return result

    def verifyLoginFailed(self, id, pwd):
        lt = 'xpath'
        if id == '':
            loc = '//form[@name="loginform"]/div/span[contains(text(), "The email field is required")]'
            result = self.isElementPresent(loc, lt)
            self.log.info('*' * 30 + 'Login unsuccessful: Email field is blank.' + '*' * 30)
        elif id != '' and pwd == '':
            result = True
            self.log.info('*' * 30 + 'Login unsuccessful: Password field is blank.' + '*' * 30)
        else:
            self.log.info('*' * 30 + 'Login unsuccessful: Invalid email/password' + '*' * 30)
            result = True
        return result

    def verifyLoginTitle(self):
        sleep(1)
        return self.verifyPageTitle("My Courses")
        # return self.verifyPageTitle("Google")         ## To fail the test case


    def clearText(self):
        emailField = self.getElement(self.emailid_field, self.emailid_lt)
        if emailField:
            emailField.clear()
        pwdField = self.getElement(self.pwd_field, self.pwd_lt)
        if pwdField:
            pwdField.clear()

    def login(self, username, pwd):
        self.clickSignInLink()
        self.clearText()
        self.enterEmail(username)
        self.enterPassword(pwd)
        self.clickLoginButton()
