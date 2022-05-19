*** Settings ***
Documentation     Example test case using the data-driven (table) syntax.
Test Template     Create new player
Library           GameControllerLibrary.py

*** Test Cases ***      Provided     Actual
Create new player       Arbitrary    Arbitrary
Set Player position     (5,0)        (5,0)
Get Player position     (4,0)        (4,0)


*** Keywords ***
Create new player
    [Arguments]    ${provided}    ${actual}
    Initialize controller
    Create player with name  ${provided}
    Player name should be    ${actual}

Get Player position
     [Arguments]    ${provided}   ${actual}
    Initialize controller
    Create player with name  ${provided}
    Set position ${newposition}
    Get player position ${actual}
    Current position should be ${newposition}

Set Player position
    [Arguments]    ${provided}   ${actual}
    Initialize controller
    Create player with name  ${provided}
    Set position ${provided}
    New position should be ${actual}
