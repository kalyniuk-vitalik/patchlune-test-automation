from page_objects.installer.base_page import BasePage
from page_objects.installer.locators import InstallerLocators

class InstallerWindow(BasePage):
    def __init__(self, app):
        super().__init__(app)

    def is_installer_window_visible(self):
        return self.is_window_visible()

    def get_installer_window_class_name(self):
        return self.get_window_class_name()

    def get_install_button(self, **kwargs):
        return self.window.child_window(**kwargs)

    def get_privacy_policy_link(self):
        return self.window.child_window(**InstallerLocators.PRIVACY_POLICY_LINK)

    def get_licensing_agreement_link(self):
        return self.window.child_window(**InstallerLocators.LICENSING_AGREEMENT_LINK)

    def get_installer_language_dropdown(self):
        return self.get_language_dropdown()

    def click_licensing_agreement(self):
        return self.click_button(**InstallerLocators.LICENSING_AGREEMENT_LINK)



