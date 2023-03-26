from time import sleep
import unittest
from pages.home.login_page import LoginPage
import logging
from traceback import print_stack
import utilities.custom_logger as cl
import pytest
from utilities.teststatus import TestStatus
from pages.courses.register_courses_page import RegisterCoursePage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    validLoginId = 'atestlogin2@email.com'
    validPwd = 'Ltest123'

    srch_course_txt = 'java'
    sel_course = 'selenium'
    cardnum = '3742 454554 00126'
    mmyy = 1223
    cvc = 111
    country = 'India'


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.rc = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)

    ## Different test cases
    def test_EnrollInCoursePaymentFailure(self):
        # self.lp.login(self.validLoginId, self.validPwd)
        # result1 = self.lp.verifyLoginSuccess()
        # self.ts.mark(result1, 'SuccessfulLogin')

        result2 = self.rc.searchCourse(self.srch_course_txt, self.sel_course)
        if result2:
            self.ts.mark(result2, 'CourseFound')
            self.rc.enrollInCourse()
            msg = self.rc.makePayment(self.cardnum, self.mmyy, self.cvc, self.country)
            if 'Your card was declined.' in msg:
                self.ts.markFinal('test_EnrollInCoursePaymentFailure', True, 'CardDeclined')
        else:
            self.ts.markFinal('test_EnrollInCoursePaymentFailure', result2, 'CourseNotFound')


