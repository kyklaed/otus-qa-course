*** Settings ***
Documentation    Suite description

Library  SeleniumLibrary
Resource    fortests.robot
Suite Teardown  Close All Browsers

*** Variables ***
${LOGIN URL}    http://192.168.88.242/admin/
${BROWSER}    firefox
${USER LOGIN}    admin
${USER PASSWORD}    admin
${LOGIN BTN}    Login

*** Test Cases ***
ValidLogin
    OpenBrowser1    ${LOGIN URL}    ${BROWSER}
    InputUsername    ${USER LOGIN}
    InputPassword    ${USER PASSWORD}
    sleep  4s
    SubmitBtn   ${LOGIN BTN}
    sleep  4s



