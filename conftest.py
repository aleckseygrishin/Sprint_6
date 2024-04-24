import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    mozilla_driver = webdriver.Firefox()

    yield mozilla_driver

    mozilla_driver.quit()
