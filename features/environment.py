from selenium import webdriver
from browser import Browser
from pages.home_page import HomePage
from pages.loan_page import LoanPage

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.loan_page = LoanPage()

def after_all(context):
    context.browser.close()
