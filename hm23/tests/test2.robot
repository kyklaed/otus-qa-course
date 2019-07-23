*** Settings ***
Documentation    Suite description
Library  DatabaseLibrary
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
AddProduct
    OpenBrowserAdmin    ${LOGIN URL}    ${BROWSER}
    Login    ${USER LOGIN}    ${USER PASSWORD}    ${LOGIN BTN}
    ActionInProduct    nokia    phone    n97

CheckCountAfterAdd
    ConnectToDB
    ${count} =    SelectFromDB
    log    ${count}
    Should Be True    ${count} == 1

DeleteProduct
    OpenBrowserAdmin    ${LOGIN URL}    ${BROWSER}
    Login    ${USER LOGIN}    ${USER PASSWORD}    ${LOGIN BTN}
    MenuProduct
    DeleteProduct    nokia

CheckCountAfterDel
    ConnectToDB
    ${count} =    SelectFromDB
    log    ${count}
    Should Be True    ${count} == 0





