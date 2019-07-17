
*** Keywords ***

OpenBrowser1
    [Arguments]  ${url}  ${browser}
    Open Browser   ${url}    ${browser}
    Title Should be    Administration

InputUsername
    [Arguments]  ${user}
    Input Text   username    ${user}

InputPassword
    [Arguments]  ${password}
    Input Text    id:input-password    ${password}
    sleep  5s

SubmitBtn
    [Arguments]  ${btn}
    Click Button    ${btn}