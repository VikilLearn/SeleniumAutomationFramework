from time import sleep
import unittest
from pages.home.login_page import LoginPage
import logging
from traceback import print_stack
import utilities.custom_logger as cl
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    validLoginId = 'atestlogin2@email.com'
    validPwd = 'Ltest123'
    blankLoginId = ''
    blankPwd = ''
    invalidLoginId = 'invalid_id'
    invalidPwd = 'invalid_pwd'

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


## Different test cases
    @pytest.mark.run(order=1)
    def test_LoginWithNoUsername(self):
        self.lp.login(self.blankLoginId, self.validPwd)
        result = self.lp.verifyLoginFailed(self.blankLoginId, self.validPwd)
        self.ts.mark(result,'LoginFailed')
        # assert result == True


    @pytest.mark.run(order=2)
    def test_LoginWithNoPassword(self):
        self.lp.login(self.validLoginId, self.blankPwd)
        result = self.lp.verifyLoginFailed(self.validLoginId, self.blankPwd)
        self.ts.mark(result,'LoginFailed')
        # assert result == True


    @pytest.mark.run(order=3)
    def test_LoginWithNoUsernamePassword(self):
        self.lp.login(self.blankLoginId, self.blankPwd)
        result = self.lp.verifyLoginFailed(self.blankLoginId, self.blankPwd)
        self.ts.mark(result,'LoginFailed')
        # assert result == True


    @pytest.mark.run(order=4)
    def test_LoginWithInValidUsernamePassword(self):
        self.lp.login(self.invalidLoginId, self.invalidPwd)
        result = self.lp.verifyLoginFailed(self.invalidLoginId, self.invalidPwd)
        self.ts.mark(result,'LoginFailed')
        # assert result == True


    @pytest.mark.run(order=5)
    def test_validLogin(self):
        self.lp.login(self.validLoginId, self.validPwd)
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title_Verified")
        result2 = self.lp.verifyLoginSuccess()
        self.ts.markFinal("test_validLogin", result2, "SuccessfulLogin")
        sleep(1)


