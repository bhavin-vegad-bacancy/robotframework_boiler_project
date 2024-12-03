*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Resource    ../login_functionality.robot

*** Keywords ***
Valid Login and Verify Dashboard Page
    [Documentation]    Test to verify login and dashboard page
    [Arguments]     ${username}     ${password}
    Open Browser    ${base_url}    Chrome
    Maximize Browser Window
    Sleep    2s
    Input Text      ${USERNAME_XPATH}    ${username}
    Input Text      ${PASSWORD_XPATH}    ${password}
    Click Element    ${LOGIN_BTN_XPATH}
    ${currentUrl}       Get Location
    Sleep    2s
    IF    $currentUrl != $base_url
        Wait Until Page Contains Element    ${DASHBOARD_PAGE_XPATH}
        ${dashboard_text}    Get Text    ${DASHBOARD_PAGE_XPATH}
        Should Be Equal As Strings    ${dashboard_text}    Dashboard
        ${output}   Set Variable    User Logged-in.
        RETURN  ${output}
    ELSE
        ${output}   Set Variable    Opps!! There is something wrong with data
        Capture Page Screenshot
        RETURN  ${output}
    END