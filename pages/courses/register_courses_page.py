# from SeleniumSelfPracticeAutomationFramework.base.selenium_driver import SeleniumDriver
from time import sleep
import logging
import utilities.custom_logger as cl
from traceback import print_stack
from selenium.webdriver.support.select import Select
from base.basepage import BasePage
from pages.home.login_page import LoginPage


class RegisterCoursePage(BasePage):

    # Locators and locator type
    allCourses = '//a[contains(text(),"ALL COURSES")]'
    allCourses_lt = 'xpath'

    srch_txtbox = '//input[@id="search"]'
    srch_txtbox_lt = 'xpath'

    srch_btn = '//button[@class="find-course search-course"]'
    srch_btnlt = 'xpath'

    dynamic_course = "//div[contains(@class,'course-list')]/a[contains(@href,'{0}')]"
    course_lt = 'xpath'

    enroll_course = '//button[contains(text(),"Enroll in Course")]'
    enroll_course_lt = 'xpath'


    cardnum_frame = '//iframe[@title="Secure card number input frame"]'
    cardnum_frame_lt = 'xpath'
    cardnum_txtbox = '//input[contains(@name,"cardnumber") and contains(@placeholder,"Card Number")]'
    cardnum_txtbox_lt = 'xpath'

    card_exp_frame = '//iframe[@title="Secure expiration date input frame"]'
    card_exp_frame_lt = 'xpath'
    card_exp_txtbox = '//input[@aria-label="Credit or debit card expiration date"]'
    card_exp_txtbox_lt = 'xpath'

    cvc_frame = '//iframe[@title="Secure CVC input frame"]'
    cvc_frame_lt = 'xpath'
    cvc_txtbox =  '//input[@name="cvc"]'
    cvc_txtbox_lt = 'xpath'

    country_loc = '//Select[@name="country-list"]'
    country_lt = 'xpath'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def allCoursesLink(self):
        self.elementClick(self.allCourses, self.allCourses_lt)
        course_list = []
        elements = self.getElementList('//div[contains(@class,"zen-course-title")]/h4', 'xpath')
        for course in elements:
            course_list.append(course.text)
        len(course_list)
        return course_list
        sleep(1)


    def searchCourse(self, srch_course,sel_course):
        self.allCoursesLink()
        # self.elementClick(self.allCourses, self.allCourses_lt)
        self.enterText(text=srch_course,locator=self.srch_txtbox, locator_type=self.srch_txtbox_lt)
        self.elementClick(self.srch_btn, self.srch_txtbox_lt)

        course_loc = self.dynamic_course.format(sel_course)
        self.elementClick(course_loc, self.course_lt)
        return True


    def enrollInCourse(self):
        sleep(1)
        self.elementClick(self.enroll_course, self.enroll_course_lt)
        self.driver.execute_script("window.scrollBy(0,700)")
        sleep(2)

    def makePayment(self, cardnum, mmyy, cvc, country):
        self.switchToFrame(xpath=self.cardnum_frame)
        self.enterText(text=cardnum, locator=self.cardnum_txtbox, locator_type=self.cardnum_txtbox_lt)
        self.driver.switch_to.parent_frame()

        self.switchToFrame(xpath=self.card_exp_frame)
        # self.driver.switch_to.frame(self.getElement(self.card_exp_frame,self.card_exp_frame_lt))
        self.enterText(mmyy, self.card_exp_txtbox, self.card_exp_txtbox_lt)
        self.driver.switch_to.default_content()
        # self.driver.switch_to.parent_frame()

        self.driver.switch_to.frame(self.getElement(self.cvc_frame, self.cvc_frame_lt))
        self.enterText(cvc, self.cvc_txtbox, self.cvc_txtbox_lt)
        self.driver.switch_to.parent_frame()

        country_drpdwn = self.getElement(self.country_loc, self.country_lt)
        sel_country = Select(country_drpdwn)
        sel_country.select_by_visible_text(country)

        # Rather than clicking on Buy button, just did a workaround of testing if Buy button is enabled.
        # self.elementClick('//div[@class="col-xs-12"]/button[@class="zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button"]', 'xpath')
        # element = self.getElement('//div[@class="alert alert-danger"]/p','xpath')
        # msg = element.text
        # return msg

        result = self.isEnabled(locator='//div[@class="col-xs-12"]/button[@class="zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button"]', locatorType='xpath')
        if result:
            return 'Your card was declined.'
        sleep(2)
