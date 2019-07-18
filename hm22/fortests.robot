*** Keywords ***
OpenBrowserAdmin
    [Arguments]  ${url}  ${browser}
    Open Browser   ${url}    ${browser}
    Title Should be    Administration

OpenBrowserMain
    [Arguments]  ${url}  ${browser}
    Open Browser   ${url}    ${browser}

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

CheckWarningAfterInvalidLogin
        Get WebElement    css:div.alert.alert-danger.alert-dismissible

OpenCart
    ${btn} =   Get WebElement    css:div[id=cart] button
    Click Button    ${btn}

EmptyCart
    OpenCart
    Element Should Contain    css:ul.pull-right li p.text-center    Your shopping cart is empty!

InputTextInSearch
    [Arguments]  ${text}
    ${field} =   Get WebElement    css:div[id="search"] input
    Input Text    ${field}    ${text}

SubmitSearchBtn
    ${btn} =   Get WebElement    css:div[id="search"] button
    Click Button    ${btn}

FindSerchBtnInside
    Get WebElement    css:input[id="button-search"]

FindSlider
    Get WebElement    css:div[class="swiper-wrapper"]
