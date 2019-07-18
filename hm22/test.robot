*** Settings ***
Documentation    Suite description

Library  SeleniumLibrary
Resource    fortests.robot
Suite Teardown  Close All Browsers

*** Variables ***
#${LOGIN URL}    http://192.168.88.242/admin/
${LOGIN URL}    http://demo23.opencart.pro/admin/
${BROWSER}    firefox
${USER LOGIN}    admin
${USER PASSWORD}    admin
${BAD USER PASSWORD}    adm
${LOGIN BTN}    Login

*** Test Cases ***
ValidLogin
    OpenBrowser1    ${LOGIN URL}    ${BROWSER}
    InputUsername    ${USER LOGIN}
    InputPassword    ${USER PASSWORD}
    sleep  1s
    SubmitBtn   ${LOGIN BTN}
    sleep  1s

InvadlidLogin
    OpenBrowser1    ${LOGIN URL}    ${BROWSER}
    InputUsername    ${USER LOGIN}
    InputPassword    ${BAD USER PASSWORD}
    sleep  1s
    SubmitBtn   ${LOGIN BTN}
    sleep  1s




