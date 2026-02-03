Feature: Verifying Registration functionality

  Scenario: Registration with valid data
    Given User is on Registration Page
    When User enters firstname
    And User enters lastname
    And User enters month
    And User enters day
    And User enters year
    And User click gender
    And User enters email
    And User enters password
    And User click on signup button
    Then User should be registered successfully

  Scenario: Registration with duplicate email data
    Given User is on Registration Page
    When User enters firstname
    And User enters lastname
    And User enters month
    And User enters day
    And User enters year
    And User click gender
    And User enters email
    And User enters password
    And User click on signup button
    Then User should be registered with duplicate email successfully