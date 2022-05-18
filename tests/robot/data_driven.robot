*** Settings ***
Documentation     Example test case using the data-driven (table) syntax.
Test Template     Start new game with player
Library           GameControllerLibrary.py

*** Test Cases ***      Provided     Actual
Provided player name    Arbitrary    Arbitrary
Blank player name       ${EMPTY}     Player


*** Keywords ***
Start new game with player
    [Arguments]    ${provided}    ${actual}
    Initialize controller
    Create player with name  ${provided}
    Player name should be    ${actual}


    *** Test Cases ***      Provided     Actual
(1,1)      count 2  D       (1,0)        count 3
(1,10)     count 3  U   


*** Keywords ***
Start new game with player
    [Arguments]    ${provided}    ${actual}
    Initialize controller
    Create player with name  ${provided}
    Player name should be    ${actual}