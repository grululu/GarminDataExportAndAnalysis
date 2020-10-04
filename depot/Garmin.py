from selenium import webdriver
from pyvirtualdisplay import Display
from GarminConnect import GarminConnect as GC
from Infos import GCuser, GCpass
from selenium.webdriver.chrome.options import Options

display = Display()
display.start()
options = Options()
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("prefs", {"download.default_directory": "/path/to/download/dir","download.prompt_for_download": False,})

chrome = webdriver.Chrome(chrome_options=options,service_args=["--verbose", "--log-path=/tmp/chrome.log"])
GC = GC(chrome)
GC.login(userName = GCuser, passWord = GCpass)
GC.getActivities()
GC.close()

