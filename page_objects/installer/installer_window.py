from page_objects.installer.base_page import BasePage
from page_objects.installer.locators import InstallerLocators

class InstallerWindow(BasePage):
    def __init__(self, app):
        """Initializes the InstallerWindow with the given app."""
        super().__init__(app)

    def is_installer_window_visible(self):
        """Checks if the installer window is visible."""
        return self.is_window_visible()

    def get_installer_window_class_name(self):
        """Gets the class name of the installer window."""
        return self.get_window_class_name()

    def get_install_button(self, **kwargs):
        """Returns the install button control."""
        return self.window.child_window(**kwargs)

    def get_privacy_policy_link(self):
        """Returns the privacy policy link control."""
        return self.window.child_window(**InstallerLocators.PRIVACY_POLICY_LINK)

    def get_licensing_agreement_link(self):
        """Returns the licensing agreement link control."""
        return self.window.child_window(**InstallerLocators.LICENSING_AGREEMENT_LINK)

    def get_installer_language_dropdown(self):
        """Returns the language dropdown control."""
        return self.get_language_dropdown()

    def click_license_agreement(self):
        """Clicks the licensing agreement link."""
        return self.click_button(**InstallerLocators.LICENSING_AGREEMENT_LINK)

    def click_privacy_policy(self):
        """Clicks the privacy policy link."""
        return self.click_button(**InstallerLocators.PRIVACY_POLICY_LINK)

    def click_install_button(self):
        """Clicks the install button."""
        return self.click_button(**InstallerLocators.INSTALLER_BUTTON)

    # def get_installation_label(self):
    #     """Returns the installation label control."""
    #     return self.get_label()
