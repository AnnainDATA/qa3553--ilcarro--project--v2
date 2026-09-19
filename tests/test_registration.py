import random
import time

from pages.registration_page import RegistrationPage
from models.user import User

#------Positive------
#------Check that User can register with correct values------
def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    random_suffix = random.randint(1,1000000)
    user=User(
        "Dolores",
        "Mary Eileen",
        f"dolores_{random_suffix}@gmail.com",
        "MaryE1971!"
    )
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.confirmation_text() == "Registered"
    assert registration_page.confirmation_message() == "You are logged in success"
    registration_page.close_window()

#------Negative------
#------Fall in registration with empty field "Name"------
def test_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "",
        "Mary Eileen",
        f"dolores_1971@gmail.com",
        "MaryE1971!"
    )
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Name is required"
    assert registration_page.submit_button_disabled()

#------Fall in registration with empty field "Last Name"------
def test_registration_with_empty_lastname(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "Dolores",
        "",
        f"dolores_1971@gmail.com",
        "MaryE1971!"
    )
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Last name is required"
    assert registration_page.submit_button_disabled()

#------Fall in registration with incorrect email------
def test_registration_with_wrong_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "Dolores",
        "Mary Eileen",
        f"dolores_1971gmail.com",
        "MaryE1971!"
    )
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Wrong email format"
    assert registration_page.submit_button_disabled()

#------Fall in registration with empty field "Email"------
def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "Dolores",
        "Mary Eileen",
        "",
        "MaryE1971!"
    )
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Email is required"
    assert registration_page.submit_button_disabled()

def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "Dolores",
        "Mary Eileen",
        f"dolores_1971@gmail.com",
        "Mary"
    )
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Password must contain minimum 6 symbols"
    assert registration_page.submit_button_disabled()

#------Fall in registration with incorrect pwd------
def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "Dolores",
        "Mary Eileen",
        f"dolores_1971@gmail.com",
        ""
    )
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Password is required"
    assert registration_page.submit_button_disabled()

#------Fall in registration with unsigned checkbox------
def test_registration_without_checkbox(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "Dolores",
        "Mary Eileen",
        f"dolores_1971@gmail.com",
        "MaryE1971!"
    )
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "You must accept the terms"
    assert registration_page.submit_button_disabled()

#------Fall in registration with 2 accounts with the same e-mail------
def test_registration_with_the_same_email(driver):
    registration_page = RegistrationPage(driver)
    random_suffix = random.randint(1, 1000000)

    user1 = User(
        "Dolores",
        "Mary Eileen",
        f"dolores_{random_suffix}@gmail.com",
        "MaryE1971!"
    )
    user2 = User(
        "Santa",
        "Barbara",
        f"dolores_{random_suffix}@gmail.com",
        "Sants1972!"
    )
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user1)
    registration_page.check_policy()
    time.sleep(5)
    registration_page.submit_registration()
    registration_page.close_window1()

    registration_page.fill_registration_form(user2)
    registration_page.check_policy()
    time.sleep(5)
    registration_page.submit_registration()

    assert registration_page.confirmation_text() == "Registration failed"
    #assert registration_page.confirmation_message() == '"[object Object]"' #why I can"t receive whis alert?
    registration_page.close_window1()