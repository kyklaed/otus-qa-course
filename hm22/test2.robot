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
AddCategory
    OpenBrowserAdmin    ${LOGIN URL}    ${BROWSER}
    Login    ${USER LOGIN}    ${USER PASSWORD}    ${LOGIN BTN}
    ActionInCatalog    aaaaa    phone

DelCategory
    OpenBrowserAdmin    ${LOGIN URL}    ${BROWSER}
    Login    ${USER LOGIN}    ${USER PASSWORD}    ${LOGIN BTN}
    MenuCatigories
    DeleteCategories    aaaaa

AddProduct
    OpenBrowserAdmin    ${LOGIN URL}    ${BROWSER}
    Login    ${USER LOGIN}    ${USER PASSWORD}    ${LOGIN BTN}
    ActionInProduct    nokia    phone    n97

DeleteProduct
    OpenBrowserAdmin    ${LOGIN URL}    ${BROWSER}
    Login    ${USER LOGIN}    ${USER PASSWORD}    ${LOGIN BTN}
    MenuProduct
    DeleteProduct    nokia






