from pywinauto.application import Application
from pywinauto.timings import TimeoutError
from page_objects.installer.locators import InstallerLocators
import logging

class BasePage:
    def __init__(self, app: Application):
        """Initializes the BasePage with the given application."""
        self.app = app
        self.window = app.window(**InstallerLocators.INSTALLER_WINDOW)
        self.wait_for_window()

    def wait_for_window(self, timeout=30):
        """Waits for the installer window to be ready."""
        try:
            self.window.wait('ready', timeout=timeout, retry_interval=1)
            return True
        except TimeoutError:
            logging.error("Timeout waiting for installer window to be ready")
            return False

    def is_window_visible(self):
        """Checks if the installer window is visible."""
        return self.window.is_visible()

    def get_window_class_name(self):
        """Gets the class name of the installer window."""
        return self.window.class_name()

    def get_language_dropdown(self):
        """Returns the language dropdown control."""
        return self.window.child_window(**InstallerLocators.LANGUAGE_DROPDOWN)

    def click_button(self, **kwargs):
        """Clicks a button in the installer window."""
        try:
            button = self.window.child_window(**kwargs)
            button.invoke()
            logging.info(f"Button clicked successfully")
            return True
        except Exception as e:
            logging.error(f"Failed to click button: {e}")
            raise ValueError(f"Button not found or not clickable: {e}") from e

    def get_label(self, **kwargs):
        """Returns a label control from the installer window."""
        return self.window.child_window(**kwargs)