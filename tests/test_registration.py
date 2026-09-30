import random
import time
import pytest
from selenium.common import TimeoutException

from data.user_data import create_user
from pages.registration_page import RegistrationPage
from models.user import User

#------Positive------
#------Check that User can register with correct values------
def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    user = create_user()

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
    user = create_user(name = "")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Name is required"
    assert registration_page.submit_button_disabled()

#------Fall in registration with empty field "Last Name"------
def test_registration_with_empty_lastname(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(last_name="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Last name is required"
    assert registration_page.submit_button_disabled()

#------Fall in registration with incorrect email------
INVALID_EMAILS = [
    "",
    "simon@@gmail.com",
    "simongmail.com",
    "simon@gmail",
    "simon1@",
    "simonsimonsimonsimonsimonsimonsimonsimon@gmail.com",
    "simon@gmailgmail.com",
    "s@g",
    "gmail.com@סימון",
    "  simon@gmail.com",
    "simon@gmail.com   ",
    "##@gmail.com",
    "%%!!@gmail.com",
    "simon@gmail.com simon@gmail.com",
    "simon@gmail.comsimon@gmail.com"
]
PASSWORDS = []
@pytest.mark.parametrize("invalid_email", INVALID_EMAILS)
def test_registration_with_wrong_email(driver,invalid_email):

    registration_page = RegistrationPage(driver)
    user = create_user(email=invalid_email)
    PASSWORDS.append(user.password)

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    print(PASSWORDS)
    assert registration_page.error_message_text() == "Wrong email format"
    assert registration_page.submit_button_disabled()

#------Fall in registration with empty field "Email"------
def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(email="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Email is required"
    assert registration_page.submit_button_disabled()

#------Fall in registration with incorrect short password------
def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(password="MMM")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Password must contain minimum 6 symbols"
    assert registration_page.submit_button_disabled()

#------Fall in registration with empty Password------
def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(password="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Password is required"
    assert registration_page.submit_button_disabled()

#------Fall in registration with the 7 symbols pwd------
def test_registration_with_short_password(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(password="Mary11!")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.confirmation_text() == "Registration failed"
    assert registration_page.confirmation_message() == '"[object Object]"' # it's a wrong alert message!

#------Fall in registration with unsigned checkbox------
def test_registration_without_checkbox(driver):
    registration_page = RegistrationPage(driver)
    user = create_user()

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
    user1 = create_user(email = f"dolores_{random_suffix}@gmail.com")
    user2 = create_user(email=f"dolores_{random_suffix}@gmail.com")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user1)
    registration_page.check_policy()
    time.sleep(2)
    registration_page.submit_registration()
    registration_page.close_window1()

    registration_page.fill_registration_form(user2)
    registration_page.check_policy()
    time.sleep(2)
    registration_page.submit_registration()

    assert registration_page.confirmation_text() == "Registration failed"
    #assert registration_page.confirmation_message() == '"[object Object]"' #why I can"t get whis alert!?
    registration_page.close_window1()

#---------------------------------------------------
@pytest.mark.skip (reason  = "BUG")
# Expected result: After completing registration, the user should be redirected to the main page / login page
# or the page should refresh.
# Actual result: The page does not refresh after registration,
# allowing the user to register repeatedly in a loop.

def test_registration_success_five_times(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    for i in range(1, 6):
        random_suffix = random.randint(1, 1000000)
        email = f"dolores_{random_suffix}@gmail.com"

        user = User(
            "Dolores",
            "Mary Eileen",
            email,
            "MaryE1971!"
        )
        print(f"\n[Registration {i} from 5] User: {email}")
        registration_page.fill_registration_form(user)
        registration_page.check_policy()
        registration_page.submit_registration()
        registration_page.close_window()

# ---------------------------------------------------
# required
# min = 6-8
# (a-z, A-Z)
# min 1 digit 0-9
# !@#$%^&*
INVALID_PWD = [
    "",
    "      ",
    "123456789",
    "Anna1",
    "Marry!",
    "SimonSimonSimonSimon123456123456$$$!!!",
    "!@#$%^&*AAzz123456",
    " MaryE1971!",
    "MaryE1971! ",
    "MaryE 1971!",
    "СимонИ1971!",
    "MaryElvis^^@",
    "MaryEl1971"
    ]
@pytest.mark.skip (reason  = "not completed")
@pytest.mark.parametrize("invalid_password", INVALID_PWD)
def test_registration_with_incorrect_password(driver,invalid_password):
    registration_page = RegistrationPage(driver)
    user = create_user(password=invalid_password)

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    #assert registration_page.submit_button_disabled(), f"Submit button is enabled for password: {invalid_password}"

    try:
        error_text = registration_page.confirmation_text()
        expected_errors = [
        "Password must contain minimum 6 symbols",
        "Password must contain at least 1 letter and 1 number",
        "Password is required",
        "Registration failed"
        ]
        assert error_text in expected_errors, f"Unexpected error text '{error_text}' for password: {invalid_password}"
    except TimeoutException:
        pass

    # assert registration_page.error_message_text() == "Password must contain minimum 6 symbols"
    # assert registration_page.submit_button_disabled()
    # assert registration_page.submit_button_disabled()
    # assert registration_page.confirmation_text() == "Password must contain minimum 6 symbols"
    # assert registration_page.confirmation_text() == "Password must contain at least 1 letter and 1 number"
    # assert registration_page.confirmation_text() == "Password is required"
    # assert registration_page.confirmation_text() == "Registration failed"
    # assert registration_page.confirmation_message() == '"[object Object]"' # it's a wrong alert message!