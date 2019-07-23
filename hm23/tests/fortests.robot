*** Keywords ***
OpenBrowserAdmin
    [Arguments]  ${url}  ${browser}
    Open Browser   ${url}    ${browser}
    Title Should be    Administration

OpenBrowserMain
    [Arguments]  ${url}  ${browser}
    Open Browser   ${url}    ${browser}

Login
    [Arguments]   ${USER LOGIN}  ${USER PASSWORD}  ${LOGIN BTN}
    InputUsername    ${USER LOGIN}
    InputPassword    ${USER PASSWORD}
    sleep  1s
    SubmitBtn   ${LOGIN BTN}
    sleep  1s

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

MenuCatigories
    sleep  1s
    ${field} =   Get WebElement    css:a[href="#collapse1"]
    Click Element    ${field}
    sleep  1s
    Click Element    css:ul.in li a[href*=catalog]

ActionInCatalog
    [Arguments]  ${name_catalog}  ${name_tag}
    MenuCatigories
    sleep  6s
    Click Element    css:div.pull-right a.btn-primary
    Input Text    css:input[id="input-name1"]    ${name_catalog}
    Input Text    css:input[id="input-meta-title1"]    ${name_tag}
    Click Button    css:button[type="submit"]
    Get WebElement    xpath://td[contains(text(), "${name_catalog}")]

DeleteCategories
    [Arguments]  ${name_catalog}
    Click Element    xpath://td[contains(text(), "${name_catalog}")]/parent::*[1]/td[1]/input
    Click Button    css:button.btn-danger
    Handle Alert

MenuProduct
    sleep  1s
    ${field} =   Get WebElement    css:a[href="#collapse1"]
    Click Element    ${field}
    sleep  1s
    Click Element    css:ul.in li a[href*=product]

ActionInProduct
    [Arguments]  ${name_product}  ${name_tag}  ${name_model}
    MenuProduct
    sleep  6s
    Click Element    css:div.pull-right a.btn-primary
    Input Text    css:input[id="input-name1"]    ${name_product}
    Input Text    css:input[id="input-meta-title1"]    ${name_tag}
    Click Element    css:a[href="#tab-data"]
    Input Text    css:input[id="input-model"]    ${name_model}
    Click Button    css:button[type="submit"]
    Get WebElement    xpath://td[contains(text(), "${name_product}")]

DeleteProduct
    [Arguments]  ${name_product}
    Click Element    xpath://td[contains(text(), "${name_product}")]/parent::*[1]/td[1]/input
    Click Button    css:button.btn-danger
    Handle Alert

ConnectToDB
    Connect To Database    MySQLdb    opencart    admin    pass    192.168.88.242    3306

SelectFromDB
    ${query} =    Query   SELECT COUNT(*) FROM oc_product;
    [return]    ${query[0][0]}