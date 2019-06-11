from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.common.action_chains import ActionChains
import time

class LoanPageLocator(object):
    # Search Results Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    LOAN_AMOUNT = (By.CLASS_NAME, "loan-amount__range-slider__input")

class LoanPage(Browser):
    # Search Results Page Actions

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title

    def get_header(self):
        return self.get_element(*LoanPageLocator.HEADER_TEXT).text

    def select_loan_amount(self, loan_amount):
        time.sleep(4)
        move = ActionChains(self.driver)
        slider = self.driver.find_element(*LoanPageLocator.LOAN_AMOUNT)
        move.click_and_hold(slider).move_by_offset(200,0).release().perform()
        time.sleep(4)
        return self.driver.find_element(*LoanPageLocator.LOAN_AMOUNT).get_attribute("value")
