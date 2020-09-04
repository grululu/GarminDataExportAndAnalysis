from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class GarminConnect:
    def __init__(self, driver):
        self.driver = driver
        self.urlLogin = 'https://sso.garmin.com/sso/login?service=https%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&webhost=olaxpw-connect04&source=https%3A%2F%2Fconnect.garmin.com%2Fen-US%2Fsignin&redirectAfterAccountLoginUrl=https%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&redirectAfterAccountCreationUrl=https%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&gauthHost=https%3A%2F%2Fsso.garmin.com%2Fsso&locale=en_US&id=gauth-widget&cssUrl=https%3A%2F%2Fstatic.garmincdn.com%2Fcom.garmin.connect%2Fui%2Fcss%2Fgauth-custom-v1.1-min.css&clientId=GarminConnect&rememberMeShown=true&rememberMeChecked=false&createAccountShown=true&openCreateAccount=false&usernameShown=false&displayNameShown=false&consumeServiceTicket=false&initialFocus=true&embedWidget=false&generateExtraServiceTicket=false'
        self.urlActivities = 'https://connect.garmin.com/modern/activities'
        self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': "/media/Activities"}}
        command_result = self.driver.execute("send_command", params)

    def login(self, userName, passWord):
        """Function to login to Garmin Connect page"""
        self.driver.get(self.urlLogin)
        assert "GARMIN Authentication Application" in self.driver.title
        self.driver.find_element_by_id("username").send_keys(userName)
        self.driver.find_element_by_id("password").send_keys(passWord)
        self.driver.find_element_by_id("login-btn-signin").click()
        print("Logged in!")
        return self.driver


    def getActivities(self):
        """Function to navigate on activities page and download data"""
        self.driver.get(self.urlActivities)
        assert "Garmin Connect" in self.driver.title
        print("Getting Activities")
        self.driver.set_window_size(1920, 1080)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "export-btn"))).click()
        print("Download Complete?")

    def getClose(self):
        self.driver.close()
