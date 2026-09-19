import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class RegistrationPage:

    NAV_REGISTRATION_BTN = (By.CSS_SELECTOR,"[href='/register']")
    NAME_INPUT = (By.CSS_SELECTOR,"[name='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR,"[name='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR,"[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR,"[name='password']")
    YALLA_BTN = (By.XPATH, "//button[text()='Y’alla!']")
    CHECK_BOX = (By.ID,"terms-of-use")

    OK_BTN = (By.XPATH, "//*[text()='OK']")

    ERROR_MESSAGE = (By.CLASS_NAME, "error")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, "h3")  # Alert "Login failed" The first alert
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "p")  # Alert '"Login or Password incorrect"' The second alert

    def __init__(self,driver):
        self.driver=driver

    def open_registration_form(self):
        self.driver.find_element(*self.NAV_REGISTRATION_BTN).click()
        time.sleep(2)

    def fill_name(self,name):
        self.driver.find_element(*self.NAME_INPUT).clear()
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def fill_last_name(self,last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def fill_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

#----------------------------------
    def fill_registration_form(self,user):
        self.fill_name(user.name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_password(user.password)
#-----------------------------------

    def check_policy(self):
        self.driver.find_element(*self.CHECK_BOX).click()

    def submit_registration(self):
        self.driver.find_element(*self.YALLA_BTN).click()
        time.sleep(3)

#---------------------------------------------------
    def confirmation_text(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.CONFIRMATION_TEXT))
        return element.text

    def confirmation_message(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.CONFIRMATION_MESSAGE))
        return element.text
# ---------------------------------------------------
    def close_window(self):
        self.driver.find_element(*self.OK_BTN).click()

# --------------------------------------------------------------------
    def close_window1(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.OK_BTN)
        )
        ActionChains(self.driver).move_to_element_with_offset(element, 0, 5).click().perform()
# --------------------------------------------------------------------

    def error_message_text(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return element.text

    def submit_button_disabled(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.YALLA_BTN)
        )
        return element.get_attribute("disabled") is not None