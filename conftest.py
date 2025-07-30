import time
import pytest
from utils.installer_start import start_installer

@pytest.fixture
def installer_app():
    exe_path = r"C:\Users\VKalyniuk\Downloads\installer_9.1.57803.1174_internal"
    application = start_installer(exe_path)
    yield application
    time.sleep(5)
    if application:
         try:
             application.kill()
         except:
             pass





