Feature: Appy loan

    Scenario: Navigate to loan page
        Given I load the Auden website
        When I click the apply for a loan button
        Then I verify the loan page

    Scenario Outline: Monthly loan with few instalments and repayment day as Weekend
        When I select loan amount "<loan_amount>"
        And I select "<instalment_number>" for "<type>"
        And I select the repayment date as "<date>"
        Then I verify that it display the first repayment date as "<date>"
    Examples:
        | loan_amount | instalment_number | type    | date |
        | 200         | 2                 | MONTHLY | 16   |