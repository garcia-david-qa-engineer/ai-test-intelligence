```gherkin
Feature: Multi-Factor Authentication during login

  Background:
    Given a user account exists with email "user@example.com" and password "securePassword"
    And MFA is enabled for the account

  Scenario: Successful login with valid credentials and MFA
    When the user enters "user@example.com" as email
    And the user enters "securePassword" as password
    And the user receives a one-time code via SMS
    And the user enters the received one-time code
    Then the user should be logged in successfully

  Scenario: Failed login due to incorrect password
    When the user enters "user@example.com" as email
    And the user enters "wrongPassword" as password
    Then the user should see an error message "Invalid credentials"
    And the system should log the failed login attempt

  Scenario: Account lockout after three failed login attempts
    When the user enters "user@example.com" as email
    And the user enters "wrongPassword" as password
    And the user attempts to log in three times with incorrect password
    Then the account should be locked for 15 minutes
    And the user should see a message "Account locked. Please try again later."

  Scenario: Successful resend of one-time code after SMS failure
    When the user enters "user@example.com" as email
    And the user enters "securePassword" as password
    And the SMS code fails to send
    Then the user should see an option to resend the code
    When the user requests to resend the code
    Then the user should receive a new one-time code via SMS

  Scenario: Expired one-time code
    When the user enters "user@example.com" as email
    And the user enters "securePassword" as password
    And the user receives a one-time code via SMS
    And the user waits for 3 minutes
    When the user enters the expired one-time code
    Then the user should see an error message "The code has expired"
    And the system should log the failed attempt

  Scenario: Successful login with valid credentials but expired one-time code
    When the user enters "user@example.com" as email
    And the user enters "securePassword" as password
    And the user receives a one-time code via SMS
    And the user waits for 3 minutes
    When the user attempts to log in with the expired code
    Then the user should see an error message "The code has expired"
    And the system should log the failed attempt

  Scenario: Successful login with valid credentials and valid one-time code
    When the user enters "user@example.com" as email
    And the user enters "securePassword" as password
    And the user receives a one-time code via SMS
    And the user enters the valid one-time code
    Then the user should be logged in successfully

  Scenario: Brute-force attack prevention
    Given the user account is locked
    When the user attempts to log in with any password
    Then the user should see a message "Account locked. Please try again later."
    And the system should not allow any login attempts for 15 minutes
```