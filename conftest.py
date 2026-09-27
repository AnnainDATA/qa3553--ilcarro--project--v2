import pytest
from selenium import webdriver

from data.user_data import existing_user
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://icarro-v1.netlify.app/search?page=0&size=10")

    yield driver

    driver.quit()

@pytest.fixture
def authenticated_driver(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(user.password)
    login_page.submit_login()
    login_page.close_window()

    return driver