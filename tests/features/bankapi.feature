Feature: Bank Application Endpoints

  Scenario: Bank Application endpoints - Get account
    Given Account is created and added to the database
    When I call "get_account" endpoint and store response
    Then I verify that response status code is equal to "200"
    And I verify that response contains the correct account data
