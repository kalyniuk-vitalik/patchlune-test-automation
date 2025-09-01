from pywinauto.application import Application
from pywinauto.timings import TimeoutError
from page_objects.installer.locators import InstallerLocators
import logging

class BasePage:
    def __init__(self, app: Application):
        self.app = app
        self.window = app.window(**InstallerLocators.INSTALLER_WINDOW)
        self.wait_for_window()

    def wait_for_window(self, timeout=30):
        try:
            self.window.wait('ready', timeout=timeout, retry_interval=1)
            return True
        except TimeoutError:
            logging.error("Timeout waiting for installer window to be ready")
            return False

    def is_window_visible(self):
        return self.window.is_visible()

    def get_window_class_name(self):
        return self.window.class_name()

    def get_language_dropdown(self):
        return self.window.child_window(**InstallerLocators.LANGUAGE_DROPDOWN)

    def click_button(self, **kwargs):
        try:
            button = self.window.child_window(**kwargs)
            button.invoke()
            logging.info(f"Button  clicked successfully")
            return True
        except Exception as e:
            logging.error(f"Failed to click button: {e}")
            raise ValueError(f"Button not found or not clickable: {e}") from e

    def get_label(self, **kwargs):
        return self.window.child_window(**kwargs)