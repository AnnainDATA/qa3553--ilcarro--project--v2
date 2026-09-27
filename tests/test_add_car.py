from data.car_data import create_car
from pages.add_car_page import AddCarPage


def test_add_car_success(authenticated_driver):
    car_work_page = AddCarPage(authenticated_driver)
    car = create_car()
    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()

    car_work_page.open_car_form()
    car_work_page.fill_car(car)
    car_work_page.submit_car()

    #assert car_work_page.error_message_text() == "Failed to submit car"