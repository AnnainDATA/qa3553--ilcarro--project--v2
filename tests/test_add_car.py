import glob
import os
import pytest
from data.car_data import create_car
from pages.add_car_page import AddCarPage

# --Positive--
# 1. An authorized user can create a car by filling in all fields with valid data
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "resources", "images")
PHOTO_PATHS = (
    glob.glob(os.path.join(IMAGES_DIR, "*.jpg"))
    + glob.glob(os.path.join(IMAGES_DIR, "*.png"))
    + glob.glob(os.path.join(IMAGES_DIR, "*.jpeg"))
)
CITIES = []
@pytest.mark.parametrize("photo_path", PHOTO_PATHS)
def test_add_car_all_fields_success(authenticated_driver,photo_path):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=photo_path)
    CITIES.append(car.city)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    print(CITIES)
    assert car_work_page.error_message_text() == "Failed to submit car"


# 2. An authorized user can create a car by filling in required fields with valid data
PHOTO_PASS = os.path.join(os.path.dirname(__file__),"..","resources","images","car_photo.jpg")

def test_add_car_required_fields_success(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(photo_path=PHOTO_PASS)
    CITIES.append(car.city)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()

# An unauthorized user cannot add a car
def test_add_car_unauthorized_user_negative(driver):
    car_work_page = AddCarPage(driver)
    car = create_car(city="Bnei Brak")

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Failed to submit car"

# A registered user cannot add duplicate cars with the same car registration number
@pytest.mark.parametrize("photo_path", PHOTO_PATHS)
def test_add_car_authorized_user_duplicate_car_negative(authenticated_driver,photo_path):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car(city="Bnei Brak", photo_path=photo_path)

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()
    assert car_work_page.error_message_text() == "Failed to submit car"