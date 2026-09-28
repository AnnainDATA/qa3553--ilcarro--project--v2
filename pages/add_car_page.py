import os.path
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class AddCarPage(BasePage):
    CAR_WORK_URL = "https://icarro-v1.netlify.app/let-car-work"
    CAR_WORK_BTN = (By.CSS_SELECTOR, "[href='/let-car-work']")
    CITY_INPUT = (By.XPATH, "//*[@id='city']")
    MANUFACTURE_INPUT = (By.CSS_SELECTOR, "[name='manufacture']")
    MODEL_INPUT = (By.CSS_SELECTOR, "[name='model']")
    YEAR_INPUT = (By.CSS_SELECTOR, "[name='year']")
    FUEL_SELECT = (By.CSS_SELECTOR, "[name='fuel']")
    GEAR_SELECT = (By.CSS_SELECTOR, "[name='gear']")
    WD_SELECT = (By.CSS_SELECTOR, "[name='wheelsDrive']")
    SEATS_INPUT = (By.CSS_SELECTOR, "[name='seats']")
    CAR_CLASS_INPUT = (By.CSS_SELECTOR, "[name='carClass']")
    SERIAL_NUMBER_INPUT = (By.CSS_SELECTOR, "[name='serialNumber']")
    PRICE_INPUT = (By.CSS_SELECTOR, "[name='pricePerDay']")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Submit']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error']")
    PHOTO_FILE_INPUT = (By.ID,"photo-file")

    def open_car_form(self):
        #self.click(self.CAR_WORK_BTN)
        self.driver.get(self.CAR_WORK_URL)
        time.sleep(2)

    def fill_city(self,city):
        self.fill(self.CITY_INPUT,city)
        option_locator = (By.CSS_SELECTOR, f"[data-testid='city-option'][data-value='{city}']")
        option = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(option_locator))
        option.click()
# -------------------------------------------------------
    def fill_city_not_in_list(self,city):
        self.fill(self.CITY_INPUT,city)
# -------------------------------------------------------
    def fill_manufacture(self,manufacture):
        self.fill(self.MANUFACTURE_INPUT,manufacture)

    def fill_model(self,model):
        self.fill(self.MODEL_INPUT,model)

    def fill_year(self,year):
        self.fill(self.YEAR_INPUT,year)

    def select_fuel(self,fuel):
        Select(self.find(self.FUEL_SELECT)).select_by_visible_text(fuel)

    def select_gear(self,gear):
        Select(self.find(self.GEAR_SELECT)).select_by_visible_text(gear)

    def select_wheels_drive(self,wheels_drive):
        Select(self.find(self.WD_SELECT)).select_by_visible_text(wheels_drive)

    def fill_seats(self,seats):
        self.fill(self.SEATS_INPUT,seats)

    def fill_car_class(self,car_class):
        self.fill(self.CAR_CLASS_INPUT,car_class)

    def fill_serial_number(self,serial_number):
        self.fill(self.SERIAL_NUMBER_INPUT,serial_number)

    def fill_price(self,price_per_day):
        self.fill(self.PRICE_INPUT,price_per_day)

    def submit_car(self):
        self.click(self.SUBMIT_BTN)
        time.sleep(3)

    def fill_car(self, car):
        self.fill_city(car.city)
        self.fill_manufacture(car.manufacture)
        self.fill_model(car.model)
        self.fill_year(car.year)
        self.select_fuel(car.fuel)
        self.select_gear(car.gear)
        self.select_wheels_drive(car.wheels_drive)
        self.fill_seats(car.seats)
        self.fill_car_class(car.car_class)
        self.fill_serial_number(car.serial_number)
        self.fill_price(car.price_per_day)
        if car.photo_path:
            self.upload_photo(car.photo_path)
#-------------------------------------------------------
    def fill_car_empty_city(self, car):
        #self.fill_city(car.city)
        self.fill_manufacture(car.manufacture)
        self.fill_model(car.model)
        self.fill_year(car.year)
        self.select_fuel(car.fuel)
        self.select_gear(car.gear)
        self.select_wheels_drive(car.wheels_drive)
        self.fill_seats(car.seats)
        self.fill_car_class(car.car_class)
        self.fill_serial_number(car.serial_number)
        self.fill_price(car.price_per_day)
        if car.photo_path:
            self.upload_photo(car.photo_path)

    def fill_car_empty_fuel(self, car):
        self.fill_city(car.city)
        self.fill_manufacture(car.manufacture)
        self.fill_model(car.model)
        self.fill_year(car.year)
        #self.select_fuel(car.fuel)
        self.select_gear(car.gear)
        self.select_wheels_drive(car.wheels_drive)
        self.fill_seats(car.seats)
        self.fill_car_class(car.car_class)
        self.fill_serial_number(car.serial_number)
        self.fill_price(car.price_per_day)
        if car.photo_path:
            self.upload_photo(car.photo_path)

    def fill_car_not_in_list(self, car):
        self.fill_city_not_in_list(car.city) #!not in list
        self.fill_manufacture(car.manufacture)
        self.fill_model(car.model)
        self.fill_year(car.year)
        self.select_fuel(car.fuel)
        self.select_gear(car.gear)
        self.select_wheels_drive(car.wheels_drive)
        self.fill_seats(car.seats)
        self.fill_car_class(car.car_class)
        self.fill_serial_number(car.serial_number)
        self.fill_price(car.price_per_day)
        if car.photo_path:
            self.upload_photo(car.photo_path)
# -------------------------------------------------------
    def error_message_text(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return element.text

    def upload_photo(self,file_path):
        absolute_path = os.path.abspath(file_path)
        self.find(self.PHOTO_FILE_INPUT).send_keys(absolute_path)

    def add_car_submit_button_disabled(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.SUBMIT_BTN)
        )
        return element.get_attribute("disabled") is not None

