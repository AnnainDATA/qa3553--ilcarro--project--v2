import pytest

from pages.login_page import LoginPage

VALID_EMAIL = "anna12345@gmail.com"
VALID_PASSWORD = "123456!Anna"

VALID_EMAIL_UNREGISTERED="anna.anikeenko@gmail.com"
VALID_PASSWORD_UNREGISTERED="A13579!Ann"

# Positive
# 1. Registered user can log in with valid data
#@pytest.mark.skip (reason  = "passed, not relevant")
def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.confirmation_text()== "You are logged in success"
    login_page.close_window()

#@pytest.mark.skip (reason  = "passed, not relevant")
def test_login_success1(driver):
    login_page=LoginPage(driver)

    login_page.open_login_form()
    login_page.login(VALID_EMAIL,VALID_PASSWORD)

    assert login_page.confirmation_text()== "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() is True

# Negative
# 1. Registered user can't log in with invalid email
#@pytest.mark.skip (reason  = "passed, not relevant")
def test_login_valid_pwd_invalid_email_registered_user(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email("anna.anikeenkogmail.com")
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.alert_wrong_appeared() is True
    assert login_page.error_message_text() == "Wrong email format"
    assert login_page.submit_button_disabled()

# 2. Registered user can't log in with email field empty
#@pytest.mark.skip (reason  = "passed, not relevant")
def test_login_valid_pwd_empty_email_registered_user(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email("")
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.alert_wrong_appeared() is True
    assert login_page.error_message_text() == "Email is required"
    assert login_page.submit_button_disabled()

# 3.Registered user can't log in with invalid password
def test_login_invalid_pwd_valid_email_registered_user(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password("000")
    login_page.submit_login()

    assert login_page.confirmation_text() == "Login failed"
    assert login_page.confirmation_message() == '"Login or Password incorrect"'


# 4. Registered user can't log in with password field empty
def test_login_empty_pwd_valid_email_registered_user(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password("")
    login_page.submit_login()

    assert login_page.alert_wrong_appeared() is True
    assert login_page.error_message_text() == "Password is required"
    assert login_page.submit_button_disabled()


# 5. Unregistered user can't log in with valid data
def test_login_not_success_unregister_user(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL_UNREGISTERED)
    login_page.fill_password(VALID_PASSWORD_UNREGISTERED)
    login_page.submit_login()

    assert login_page.confirmation_text() == "Login failed"
    assert login_page.confirmation_message() == '"Login or Password incorrect"'
