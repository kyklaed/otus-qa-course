import pytest


def test_opencart(request, app):
    print(app.url)
    driver = app.obj()
    driver.get(app.url)
    elem = driver.find_element_by_tag_name("footer").find_element_by_class_name("container")\
        .find_element_by_tag_name("p").find_element_by_tag_name("a").get_attribute("href")
    request.addfinalizer(driver.quit)
    assert elem == 'http://www.opencart.com/'