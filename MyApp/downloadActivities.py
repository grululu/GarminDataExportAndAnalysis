from selenium import webdriver
from pyvirtualdisplay import Display
from Infos import GCuser, GCpass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class GarminConnect:
    def __init__(self, driver):
        self.driver = driver
        self.urlActivities = 'https://connect.garmin.com/modern/activities'
        self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': "/MyApp"}}
        command_result = self.driver.execute("send_command", params)

    def getActivities(self,userName,passWord):
        """Function to navigate on activities page and download data"""
        self.driver.get(self.urlActivities)
        print ('Title is '+self.driver.title)
        self.driver.save_screenshot("/tmp/garminConnectEntryPage.png")
        assert "Garmin SSO Portal" in self.driver.title
        self.driver.save_screenshot("/tmp/activities.png")
        print("Getting Activities")
        self.driver.set_window_size(1920, 1080)
        self.driver.save_screenshot("/tmp/activities1.png")
        frameLogin= self.driver.find_element_by_id("gauth-widget-frame-gauth-widget")
        self.driver.switch_to.frame(frameLogin)
        self.driver.find_element_by_id("username").send_keys(userName)
        self.driver.find_element_by_id("password").send_keys(passWord)
        print("Username "+userName)
        self.driver.find_element_by_id("login-btn-signin").click()


        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "export-btn"))).click()
        except Exception as err:
            exception_type = type(err).__name__
            print(exception_type)
            self.driver.save_screenshot("/tmp/activities2.png")
        print("Download Complete")

    def close(self):
        self.driver.close()


display = Display()
display.start()
options = Options()
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("prefs", {"download.default_directory": "/path/to/download/dir","download.prompt_for_download": False,})

chrome = webdriver.Chrome(chrome_options=options,service_args=["--verbose", "--log-path=/tmp/chrome.log"])
GC = GarminConnect(chrome)
GC.getActivities(userName = GCuser, passWord = GCpass)
GC.close()
