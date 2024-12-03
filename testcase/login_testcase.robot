*** Settings ***
Library     OperatingSystem
Library     SeleniumLibrary
Resource    ../resources/keywords/org_hrms_keywords.robot
Resource    ../resources/login_functionality.robot

*** Test Cases ***
Login Scenarios
    [Documentation]     Positive Scenario testing
    ${output}   Valid Login and Verify Dashboard Page    Admin    admin123
    Log    ${output}
    Close Browser
    ${output2}  Valid Login and Verify Dashboard Page    Admin    admin1234
    Log    ${output2}
    Close Browser
    ${output3}  Valid Login and Verify Dashboard Page    ${EMPTY}    admin1234
    Log    ${output3}
    Close Browser