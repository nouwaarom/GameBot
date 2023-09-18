Feature: Commandline Options
    In order to specify and improve the behaviour of the program
    As a user
    I should be able to set parameters of the program

    Scenario: Start configuration
        Given I add the help flag 
        When I run the host 
        Then it should display help
