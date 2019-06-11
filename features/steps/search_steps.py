from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I load the Auden website')
def step_impl(context):
    context.home_page.navigate("https://auden.co.uk")
    assert_equal(context.home_page.get_page_title(), "Social Enterprise offering short term loans | Auden")

@step('I click the apply for a loan button')
def step_impl(context):
    context.home_page.click_loan_button()

@step('I verify the loan page')
def step_impl(context):
    assert_equal(context.loan_page.get_header(), "Hello, how much would you like to borrow?")

@step('I select loan amount "{loan_amount}"')
def step_impl(context, loan_amount):
    assert_equal(context.loan_page.select_loan_amount(loan_amount), "200")

@step('I select "{instalment_number}" for "{type}"')
def step_impl(context, instalment_number, type):
    page = Loan(context)

@step('I select the repayment date as "{date}"')
def step_impl(context, date):
    page = Loan(context)

@step ('I verify that it display the first repayment date as "{date}"')
def step_impl(context, date):
    context.loan_page.get_page_title
