*** Settings ***
Documentation     Example test case using the data-driven (table) syntax.
Test Template     Move player position
Library           GameControllerLibrary.py

*** Test Cases ***          Direction       Position          NewPosition         ExistingCount   NewCount
Move player ArbitraryCase1  Arbitrary       (0,0)              (0,0)                0               1
Move player EdgeCase1           s           (0,0)              (0,0)                1               2           
Move Player EdgeCase2           n           (0,10)             (0,10)               2               3
Move Player EdgeCase3           w           (0,10)             (0,10)               3               4
Move Player EdgeCase4           e           (10,0)             (10,0)               4               5
Move Player EdgeCase5           s           (10,0)             (10,0)               5               6
Move Player EdgeCase6           w           (10,10)            (10,10)              6               7
Move Player EdgeCase7           n           (10,10)            (10,10)              7               8      
Move player HappyPath1          s           (1,1)              (1,0)                8               9
Move player HappyPath2          w           (1,10)             (10,10)              9              10
Move player HappyPath3          n           (2,1)              (2,2)                10             11
Move player HappyPath4          e           (2,2)              (3,2)                11             12

 

*** Keywords ***
Move player position
    [Arguments]    ${direction}    ${position}    ${newPosition}     ${existingCount}     ${newCount} 
    Initialize controller
    Move player     ${direction}
    Position should be    ${position}
    New Position should be ${newPosition}
    Increment count   ${existingCount}
    Update count   ${newCount} 