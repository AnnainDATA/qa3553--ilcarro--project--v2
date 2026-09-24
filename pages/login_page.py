import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    LOGIN_NAV_LINK = (By.CSS_SELECTOR,"[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR,"input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR,"input[name='password']")

    YALLA_BTN = (By.XPATH, "//button[text()='Y’alla!']")
    BTN_YALLA_DISABLED = (By.CSS_SELECTOR, "button.btn.btn--primary[disabled]") # not used

    CONFIRMATION_TEXT =(By.CSS_SELECTOR,"h3")   # Alert "Login failed" The first alert
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "p")   # Alert '"Login or Password incorrect"' The second alert

    OK_BTN =(By.XPATH,"//*[text()='OK']")
    OK_BTN_2 = (By.CSS_SELECTOR,"a.btn--primary[href='/search']")

    LOG_OUT_BTN = (By.XPATH,"//*[text()='Log out']")

#errors
    ERROR_MESSAGE = (By.CLASS_NAME, "error")
    ALERT_EMAIL_IS_REQUIRED = (By.XPATH,"//*[text()='Email is required']") #ERROR_MESSAGE = (By.CLASS_NAME, "error")
    ALERT_PASSWORD_IS_REQUIRED = (By.XPATH, "//*[text()='Password is required']") #ERROR_MESSAGE = (By.CLASS_NAME, "error")
    ALERT_WRONG_EMAIL_FORMAT = (By.XPATH, "//*[text()='Wrong email format']") #ERROR_MESSAGE = (By.CLASS_NAME, "error")

    ALERT_LOGIN_FAILED = (By.XPATH,"//*[text()='Login failed']")


    def __init__(self,driver):
        self.driver=driver

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV_LINK).click()
        time.sleep(2)

    def fill_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.YALLA_BTN).click()

# General method for filling in login and password
    def login(self,email,password):
        self.fill_email(email)
        self.fill_password(password)
        self.submit_login()
#---------------------------------------------------
    def confirmation_text(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.CONFIRMATION_TEXT))
        return element.text

    def confirmation_message(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.CONFIRMATION_MESSAGE))
        return element.text

    def close_window(self):
        self.driver.find_element(*self.OK_BTN).click()

# ---------------------------------------------------
    def close_window_2(self):
        ok_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.OK_BTN_2)
        )
        ok_btn.click()

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# ---------------------------------------------------

    def is_logged(self):
        try:
            WebDriverWait(self.driver,timeout=5).until(
                EC.visibility_of_element_located(self.LOG_OUT_BTN)
            )
            return True
        except TimeoutException:
            return False

    def alert_wrong_appeared(self):
        try:
            WebDriverWait(self.driver, timeout=15).until(
                EC.any_of(
                EC.visibility_of_element_located(self.ALERT_WRONG_EMAIL_FORMAT),
                EC.visibility_of_element_located(self.ALERT_EMAIL_IS_REQUIRED),
                EC.visibility_of_element_located(self.ALERT_LOGIN_FAILED),
                EC.visibility_of_element_located(self.ALERT_PASSWORD_IS_REQUIRED)
                )
             )
            return True
        except TimeoutException:
            return False

    def error_message_text(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return element.text

    def submit_button_disabled(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.YALLA_BTN)
        )
        return element.get_attribute("disabled") is not None

