import glob
import os
import pytest
from faker import Faker
from selenium.common import TimeoutException
from data.car_data import create_car, swagger_cities_only
from pages.add_car_page import AddCarPage

fake = Faker()


# --POSITIVE--
# 1. An authorized user can create a car by filling in all fields with valid data (swagger cities only)
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "resources", "images2")
PHOTO_PATHS = (
    glob.glob(os.path.join(IMAGES_DIR, "*.jpg"))
    + glob.glob(os.path.join(IMAGES_DIR, "*.png"))
    + glob.glob(os.path.join(IMAGES_DIR, "*.jpeg"))
)
@pytest.mark.parametrize("photo_path", PHOTO_PATHS)
def test_add_car_all_fields_success1(authenticated_driver,photo_path):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(city = fake.random_element(swagger_cities_only) ,photo_path=photo_path)

    car_work_page.open_car_form()
    car_work_page.fill_car_not_in_list(car)
    car_work_page.submit_car()


# 2. An authorized user can create a car by filling in all fields with valid data (matching cities only)
IMAGES_DIR1 = os.path.join(os.path.dirname(__file__), "..", "resources", "images")
PHOTO_PATHS1 = (
    glob.glob(os.path.join(IMAGES_DIR1, "*.jpg"))
    + glob.glob(os.path.join(IMAGES_DIR1, "*.png"))
    + glob.glob(os.path.join(IMAGES_DIR1, "*.jpeg"))
)
@pytest.mark.parametrize("photo_path", PHOTO_PATHS1)
def test_add_car_all_fields_success(authenticated_driver,photo_path):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=photo_path)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Failed to submit car"


# 3. An authorized user can create a car by filling in required fields with valid data
@pytest.mark.parametrize("photo_path", PHOTO_PATHS)
def test_add_car_required_fields_success(authenticated_driver,photo_path):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=photo_path, gear=None, wheels_drive=None)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    try:
        car_work_page.error_message_text()
        assert False, (
        )
    except TimeoutException:
        pass

#----------------------------------------------------------------------------------------------------------
# --NEGATIVE--
# 1. An unauthorized user can't add a car
PHOTO_PATH = os.path.join(
    os.path.dirname(__file__),"..","resources","images","car_photo_1.jpg"
)
def test_add_car_unauthorized_user_negative(driver):
    car_work_page = AddCarPage(driver)
    car = create_car(photo_path = PHOTO_PATH)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Failed to submit car"

# 2. A registered user can't add duplicate cars with the same car registration number
PHOTO_PATH2 = os.path.join(
    os.path.dirname(__file__),"..","resources","images2","6.jpg"
)
def test_add_car_authorized_user_duplicate_car_negative(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path = PHOTO_PATH2)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Failed to submit car"

# 3. A registered user can't add a car with field [CITY] empty
def test_add_car_empty_city_negative(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path = PHOTO_PATH2)

    car_work_page.open_car_form()
    car_work_page.fill_car_empty_city(car)    #!empty city
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Failed to submit car"

# 4. A registered user can't add a car with field [MANUFACTURE/MAKE] empty
def test_add_car_empty_manufacture_negative(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(manufacture="", photo_path = PHOTO_PATH2)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Required"
    assert car_work_page.add_car_submit_button_disabled()

# 5. A registered user can't add a car with field [MODEL] empty
def test_add_car_empty_model_negative(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(model="", photo_path = PHOTO_PATH2)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Required"
    assert car_work_page.add_car_submit_button_disabled()

# 6. A registered user can't add a car with field [YEAR] empty
def test_add_car_empty_year_negative(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(year="", photo_path = PHOTO_PATH2)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Required"
    assert car_work_page.add_car_submit_button_disabled()

# 7. A registered user can't add a car with field [FUEL] empty
def test_add_car_empty_fuel_negative(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path = PHOTO_PATH2)

    car_work_page.open_car_form()
    car_work_page.fill_car_empty_fuel(car)   #!empty_fuel
    car_work_page.submit_car()
    assert car_work_page.add_car_submit_button_disabled()

# 8. A registered user can't add a car with field [SEATS] empty
def test_add_car_empty_seats_negative(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(seats="", photo_path = PHOTO_PATH2)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Required"
    assert car_work_page.add_car_submit_button_disabled()

# 9. A registered user can't add a car with field [CAR CLASS] empty
def test_add_car_empty_car_class_negative(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(car_class="", photo_path = PHOTO_PATH2)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Required"
    assert car_work_page.add_car_submit_button_disabled()

# 10. A registered user can't add a car with field [REGISTRATION NUMBER] empty
def test_add_car_empty_serial_number_negative(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(serial_number="", photo_path = PHOTO_PATH2)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Required"
    assert car_work_page.add_car_submit_button_disabled()

# 11. A registered user can't add a car with field [PRICE] empty
def test_add_car_empty_price_negative(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(price_per_day="", photo_path = PHOTO_PATH2)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Required"
    assert car_work_page.add_car_submit_button_disabled()
