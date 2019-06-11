from selenium.webdriver.common.by import By
from browser import Browser

class HomePageLocator(object):
    # Home Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    APPLY_BUTTON = (By.XPATH, "//*[contains(text(), 'apply for a loan')]")


class HomePage(Browser):
    # Home Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def click_loan_button(self):
        self.click_element(*HomePageLocator.APPLY_BUTTON)
