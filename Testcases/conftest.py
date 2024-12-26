import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    request.cls.driver=driver
    request.cls.wait=wait
    request.cls.actions=actions
    request.cls.request=request
    yield
    driver.close()