from selenium import webdriver
from pyvirtualdisplay import Display
from GCExtract import GarminConnect as GC
#from dbSetup import con, meta, get_garmin_id
from ImportActivities import gpx2pg, csv2pg
from Infos import GCuser, GCpass
from selenium.webdriver.chrome.options import Options

def get_garmin_id():
        """Get from database the activities ids already saved"""
        return {}


# creating display
display = Display(visible = 0, size = (1200, 1200))
#display = Display(visible = 0, size = (1920, 1920))
display = Display()
display.start()
options = Options()
options.add_argument('--no-sandbox')
#options.add_argument('--disable-extensions')
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#options.add_argument('--disable-application-cache')
#options.add_argument("test-type")
#options.add_argument("--js-flags=--expose-gc")
#options.add_argument("--enable-precise-memory-info")
#options.add_argument("--disable-default-apps")
options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--start-maximized")
options.add_experimental_option("prefs", {"download.default_directory": "/path/to/download/dir","download.prompt_for_download": False,})

chrome = webdriver.Chrome(chrome_options=options,service_args=["--verbose", "--log-path=/tmp/chrome.log"])
GC = GC(chrome)
GC.login(userName = GCuser, passWord = GCpass)
saved_ids = get_garmin_id()
GC.getActivities(saved_ids)

#csv2pg(con, meta, inFolder, inFormat)
