*** Settings ***
Documentation    This is for form fillup scenarioes
Library     SeleniumLibrary
Library     OperatingSystem
Library    String
Library    Collections
Resource    ../resources/env.robot
Resource    ../resources/locator.robot
Resource    login_testcase.robot

*** Variables ***
${tablerowelement}  //*[@id="HTML1"]/div[1]/table/tbody/tr
${tablecolselement}     //*[@id="HTML1"]/div[1]/table/tbody/tr/th     
${tableData}


*** Test Cases ***
Fillup the form
    Open Browser    ${base_url}    Chrome
    Maximize Browser Window
    Input Text    ${name_xpath}    John
    Input Text    ${email_xpath}    john@mail.com
    Input Text    ${phone_xpath}    +919658542552
    Input Text    ${address_xpath}    B-1 Street 1, Landmark, City, 321021
    Select Radio Button    ${radiobutton_group_name}    ${male_radio_value}
    Select Checkbox    ${sunday_cb_id}
    Select Checkbox    ${wednesday_cb_id}
    Select From List By Label    ${country_dropdown}    India
#    Select From List By Index    ${country_dropdown}    3
#    Select From List By Value    ${country_dropdown}    usa
    Select From List By Label    ${color_drodown}       Red
    Select From List By Label    ${color_drodown}       Green
    Click Link    ${home_btn}
    Sleep    5s

gloable test
