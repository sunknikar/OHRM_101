import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginClass:
    Enter_Username_Xpath = "//input[@placeholder='Username']"
    Enter_Password_Xpath = "//input[@placeholder='Password']"
    Click_LoginBtn_Xpath = "//button[@type='submit']"
    Click_LogoutOptionBtn_Xpath = "//span[@class='oxd-userdropdown-tab']"
    Click_LogoutBtn_Xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Enter_Username(self, username):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Enter_Username_Xpath)))
        self.driver.find_element(By.XPATH, self.Enter_Username_Xpath).send_keys(username)

    def Enter_Password(self, password):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Enter_Password_Xpath)))
        self.driver.find_element(By.XPATH, self.Enter_Password_Xpath).send_keys(password)

    def Click_LoginBtn(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Click_LoginBtn_Xpath)))
        self.driver.find_element(By.XPATH, self.Click_LoginBtn_Xpath).click()

    def VerifyLogin_Status(self):
        try:
            self.wait.until(
                expected_conditions.presence_of_element_located((By.XPATH, self.Click_LogoutOptionBtn_Xpath)))
            self.driver.find_element(By.XPATH, self.Click_LogoutOptionBtn_Xpath)
            return "Login Pass"
        except:
            return "Login Fail"

    def Click_LogoutOptionBtn(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Click_LogoutOptionBtn_Xpath)))
        self.driver.find_element(By.XPATH, self.Click_LogoutOptionBtn_Xpath).click()

    def Click_LogoutBtn(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Click_LogoutBtn_Xpath)))
        self.driver.find_element(By.XPATH, self.Click_LogoutBtn_Xpath).click()
