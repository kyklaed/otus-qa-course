*** Settings ***
Documentation    Suite description

Library  SeleniumLibrary
Resource    fortests.robot
Suite Teardown  Close All Browsers

*** Variables ***
${LOGIN URL}    http://192.168.88.242/admin/
${MAIN URL}    http://192.168.88.242/
${BROWSER}    firefox
${USER LOGIN}    admin
${USER PASSWORD}    admin
${BAD USER PASSWORD}    adm
${LOGIN BTN}    Login


*** Test Cases ***
ValidLogin
    OpenBrowserAdmin    ${LOGIN URL}    ${BROWSER}
    InputUsername    ${USER LOGIN}
    InputPassword    ${USER PASSWORD}
    sleep  1s
    SubmitBtn   ${LOGIN BTN}
    sleep  1s

InvadlidLogin
    OpenBrowserAdmin    ${LOGIN URL}    ${BROWSER}
    InputUsername    ${USER LOGIN}
    InputPassword    ${BAD USER PASSWORD}
    sleep  1s
    SubmitBtn   ${LOGIN BTN}
    sleep  1s
    CheckWarningAfterInvalidLogin

CheckEmptyCart
    OpenBrowserMain    ${MAIN URL}    ${BROWSER}
    EmptyCart

SearchIsWork
    OpenBrowserMain    ${MAIN URL}    ${BROWSER}
    InputTextInSearch    Hello
    SubmitSearchBtn
    FindSerchBtnInside

CheckCentralImgSlider
    OpenBrowserMain    ${MAIN URL}    ${BROWSER}
    FindSlider






