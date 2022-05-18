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



*** Keywords ***
Start new game with player
    [Arguments]    ${provided}    ${actual}
    Initialize controller
    Create player with name  ${provided}
    Player name should be    ${actual}

      
    ${provided}             Actual
   position count direction   position count
   (0,0)       0 L          (0,0)       1
   (0,0)       1 D          (0,0)       2
   (0,10)      2 U          (0,10)      3
   (0,10)      3 L          (0,10)      4
   (10,0)      4  R          (10,0)     5
   (10,0)      5  D          (10,0)     6
   (10,10)     6  L         (10,10)     7
   (10,10)     7  U         (10,10)     8
   (1,1)       8   D       (1,0)        9 
   (1,10)      9   L       (10,10)      10
   (2,1)       10  U       (2,2)        11
   (2,2)       11  R       (3,2)        12