Feature: Draughts arbitrator
    In order to play a fair game of draughts
    As a user and as an AI
    I want that the validity of a move is checked

Scenario: Forced move
    Given a forced move is available
    When  the player doesnt do the forced move
    Then  the arbitrator should refuse the move

Scenario: Legal move
    Given a legal move is available
    And   no forced move is available
    When  the player does a legal move
    Then  the arbitrator should allow the move

Scenario: Illegal move
    Given a legal move is available
    When  the player does an illegal move
    Then  the arbitrator should refuse the move
