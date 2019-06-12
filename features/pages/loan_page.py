from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.common.action_chains import ActionChains
import time

class LoanPageLocator(object):
    # Search Results Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    LOAN_AMOUNT = (By.CLASS_NAME, "loan-amount__range-slider__input")
    INSTALMENT_MONTH = (By.ID, "monthly")
    INSTALMENT_WEEK = (By.ID, "weekly")
    INSTALMENT_SINGLE = (By.ID, "single")
    MONTHLY = (By.XPATH, "//button[@data-label-text='monthly']")
    WEEKLY = (By.XPATH, "//button[@data-label-text='weekly']")
    SINGLE = (By.XPATH, "//button[@data-label-text='single']")
    REPAYMENT_DATE = (By.CLASS_NAME, "loan-schedule__tab__panel__header__button__icon")
    DATE_16 = (By.XPATH, "//button[@value='16']")
    DATE_FRI = (By.XPATH, "//button[@value='5']")
    FIRST_REPAYMENT = (By.CLASS_NAME, "loan-schedule__tab__panel__detail__tag__label")

class LoanPage(Browser):
    # Search Results Page Actions

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title

    def get_header(self):
        return self.get_element(*LoanPageLocator.HEADER_TEXT).text

    def move_slider(self, *locator, offset):
        move = ActionChains(self.driver)
        slider = self.driver.find_element(*locator)
        move.click_and_hold(slider).move_by_offset(offset,0).release().perform()

    def select_loan_amount(self, loan_amount, loan_type):
        time.sleep(4)
        self.driver.implicitly_wait(10)
        #select = self.driver.find_element(*LoanPageLocator.LOAN_AMOUNT)
        #self.driver.execute_script("arguments[0].value = arguments[1]", select, "200")
        if loan_type == "MONTHLY":
            self.driver.find_element(*LoanPageLocator.MONTHLY).click()
        elif loan_type == "WEEKLY":
            self.driver.find_element(*LoanPageLocator.WEEKLY).click()
        elif loan_type == "SINGLE":
            self.driver.find_element(*LoanPageLocator.SINGLE).click()

        time.sleep(2)

        if loan_amount == "200":
            offset = -400
        elif loan_amount == "1000":
            offset = 1000
        elif loan_type == "SINGLE" and loan_amount == "600":
            offset = 1000
            
        move = ActionChains(self.driver)
        slider = self.driver.find_element(*LoanPageLocator.LOAN_AMOUNT)
        move.click_and_hold(slider).move_by_offset(offset,0).release().perform()
        time.sleep(2)

        return self.driver.find_element(*LoanPageLocator.LOAN_AMOUNT).get_attribute("value")

    def select_instalment(self, instalment_number, loan_type):
        time.sleep(1)
        self.driver.implicitly_wait(10)
        if loan_type == "MONTHLY":
            self.driver.find_element(*LoanPageLocator.MONTHLY).click()
            move = ActionChains(self.driver)
            select = self.driver.find_element(*LoanPageLocator.INSTALMENT_MONTH)
            move.click_and_hold(select).move_by_offset(-400,0).release().perform()
        elif loan_type == "WEEKLY":
            self.driver.find_element(*LoanPageLocator.WEEKLY).click()
            move = ActionChains(self.driver)
            select = self.driver.find_element(*LoanPageLocator.INSTALMENT_WEEK)
            move.click_and_hold(select).move_by_offset(-400,0).release().perform()
        elif loan_type == "SINGLE":
            self.driver.find_element(*LoanPageLocator.SINGLE).click()
            move = ActionChains(self.driver)
            select = self.driver.find_element(*LoanPageLocator.INSTALMENT_SINGLE)
            move.click_and_hold(select).move_by_offset(-400,0).release().perform()
            
        return select.get_attribute("value")

    def select_repayment_date(self, date):
        time.sleep(1)
        self.driver.implicitly_wait(10)
        self.driver.find_element(*LoanPageLocator.REPAYMENT_DATE).click()
        if date == "16":
            self.driver.find_element(*LoanPageLocator.DATE_16).click()
        elif date == "Fri":
            self.driver.find_element(*LoanPageLocator.DATE_FRI).click()
        time.sleep(5)

    def verify_repayment_date(self):
        return self.driver.find_element(*LoanPageLocator.FIRST_REPAYMENT).text
        time.sleep(1)

