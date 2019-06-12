Feature: Appy loan

    Scenario: Navigate to loan page
        Given I load the Auden website
        When I click the apply for a loan button
        Then I verify the loan page

    Scenario Outline: Monthly loan with few instalments and repayment day as Weekend
        When I select loan amount "<loan_amount>" for "<loan_type>"
        And I select "<instalment_number>" for "<loan_type>"
        And I select the repayment date as "<date>"
        Then I verify that it display the first repayment date as "<date>"
    Examples:
        | loan_amount | instalment_number | loan_type    | date |
        | 200         | 2                 | MONTHLY      | 16   |
        | 1000        | 2                 | MONTHLY      | 16   |

    Scenario Outline: Weekly loan with few instalments and repayment day as Weekend
        When I select loan amount "<loan_amount>" for "<loan_type>"
        And I select "<instalment_number>" for "<loan_type>"
        And I select the repayment date as "<date>"
        Then I verify that it display the first repayment date as "<date>"
    Examples:
        | loan_amount | instalment_number | loan_type    | date |
        | 200         | 2                 | WEEKLY       | Fri  |
        | 1000        | 2                 | WEEKLY       | Fri  |