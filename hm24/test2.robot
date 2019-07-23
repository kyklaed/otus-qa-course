*** Settings ***
Documentation    Suite description

Library  ./lib/AllKey.py

*** Variables ***
${LOGIN URL}    http://192.168.88.242/admin/
${MAIN}    http://192.168.88.242/

*** Test Cases ***
ValidLoginAdmin
    WebDriverForAdmin
    open    ${LOGIN URL}
    set_username    admin
    set_password    admin
    loginTO
    close

ValidLoginUser
    WebDriverForClient
    openclient    ${MAIN}
    my_account
    loginpage
    set_email    client@gmail.com
    set_password_client    client
    login_btn
    close_brw



