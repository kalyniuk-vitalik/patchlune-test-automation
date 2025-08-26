import time
from email.utils import decode_rfc2231

import pytest
from utils.browser_checker import BrowserProcessManager
from page_objects.installer.installer_window import InstallerWindow
from utils.installer_start import start_installer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def installer_app():
    exe_path = r"C:\Users\VKalyniuk\Downloads\installer_9.1.60906.1183_internal"
    application = start_installer(exe_path)
    yield application
    time.sleep(5)
    if application:
         try:
             application.kill()
         except:
             pass

@pytest.fixture
def installer_window(installer_app):
    return InstallerWindow(installer_app)

# @pytest.fixture
# def default_browser():
#     browser = BrowserProcessManager()
#     return browser.get_default_browser()

@pytest.fixture
def browser_manager():
    return BrowserProcessManager()



@pytest.fixture
def chrome_browser():
    chrome_options = Options()
    debug_profile = "debug profile path"
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument(f"--user-data-dir={debug_profile}")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-sync")
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def firefox_browser():
    firefox_options = webdriver.FirefoxOptions()
    # firefox_options.add_argument("--private")

    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()
