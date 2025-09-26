import time
import pytest
from utils.browser_checker import BrowserProcessManager
from page_objects.installer.installer_window import InstallerWindow
from utils.installer_start import start_installer

@pytest.fixture(scope="session")
def exe_path():
    """Provides the path to the installer executable."""
    return r"C:\Users\VKalyniuk\Downloads\installer_10.1.63763.5338_signed_injected_internal.exe"

@pytest.fixture
def installer_app(exe_path):
    """Starts the installer application and ensures cleanup after tests."""
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
    """Creates an InstallerWindow object for the running installer."""
    return InstallerWindow(installer_app)

@pytest.fixture
def browser_manager():
    """Provides a BrowserProcessManager instance for browser operations."""
    return BrowserProcessManager()
