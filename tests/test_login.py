import time
import pytest

from data.user_data import existing_user
from pages.login_page import LoginPage

# VALID_EMAIL = "anna12345@gmail.com"
# VALID_PASSWORD = "123456!Anna"

INVALID_EMAIL = "anna12345gmail.com"

# Positive
# 1. Registered user can log in with valid data
#@pytest.mark.skip (reason  = "passed, not relevant")
def test_login_success(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.confirmation_text()== "You are logged in success"
    login_page.close_window()

def test_login_success1(driver):
    login_page=LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.login(user.email,user.password)

    assert login_page.confirmation_text()== "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() is True

#---------------------------------------------
# Negative
# 1. Registered user can't log in with invalid email
def test_login_valid_pwd_invalid_email_registered_user(driver):
    login_page = LoginPage(driver)
    user = existing_user()
    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.alert_wrong_appeared() is True
    assert login_page.error_message_text() == "Wrong email format"
    assert login_page.submit_button_disabled()

# 2. Registered user can't log in with email field empty
def test_login_valid_pwd_empty_email_registered_user(driver):
    login_page = LoginPage(driver)
    user = existing_user()
    login_page.open_login_form()
    login_page.fill_email("")
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.alert_wrong_appeared() is True
    assert login_page.error_message_text() == "Email is required"
    assert login_page.submit_button_disabled()

# 3.Registered user can't log in with invalid password
def test_login_invalid_pwd_valid_email_registered_user(driver):
    login_page = LoginPage(driver)
    user = existing_user()
    wrong_password = "Totally_wrong_password"

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(wrong_password)
    login_page.submit_login()

    assert login_page.confirmation_text() == "Login failed"
    assert login_page.confirmation_message() == '"Login or Password incorrect"'

# 4. Registered user can't log in with password field empty
def test_login_empty_pwd_valid_email_registered_user(driver):
    login_page = LoginPage(driver)
    user = existing_user()
    empty_password = ""

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(empty_password)
    login_page.submit_login()

    assert login_page.alert_wrong_appeared() is True
    assert login_page.error_message_text() == "Password is required"
    assert login_page.submit_button_disabled()

# 5. Unregistered user can't log in with valid data
def test_login_not_success_unregister_user(driver):
    login_page = LoginPage(driver)
    user = existing_user()
    login_page.open_login_form()
    login_page.fill_email(f"A{user.email}")
    login_page.fill_password(f"7{user.password}")
    login_page.submit_login()

    assert login_page.confirmation_text() == "Login failed"
    assert login_page.confirmation_message() == '"Login or Password incorrect"'

#---------------------------------------------------
@pytest.mark.skip (reason  = "BUG")
# Upon user authorization, the header buttons update correctly
# (the "Login" button disappears and the "Logout" button appears).
# However, the footer buttons do not update — the "Login" button remains visible
# and "Logout" does not appear. This allows the user to log in repeatedly in a loop.
def test_login_success_7_times(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    for i in range(1, 6):
        print(f"\n[Login attempt {i} of 5]")
        login_page.open_login_form()
        login_page.fill_email(user.email)
        login_page.fill_password(user.password)
        login_page.submit_login()
        time.sleep(2)
        login_page.close_window_2()
        time.sleep(2)
        login_page.scroll_down()
        time.sleep(2)

