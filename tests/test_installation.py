from conftest import installer_app
from page_objects.installer.base_page import BasePage
from page_objects.installer.installer_window import InstallerWindow
from page_objects.installer.locators import InstallerLocators

def test_visible_installer_window(installer_app):
    installer_window = InstallerWindow(installer_app)

    assert installer_window.is_installer_window_visible(), "Installer window is not visible"
    assert installer_window.get_installer_window_class_name() == "H-SMILE-FRAME-DC", "Installer window title does not match expected value"
    assert installer_window.get_install_button(**InstallerLocators.INSTALLER_BUTTON).exists(), "Install button is not visible"
    assert installer_window.get_privacy_policy_link().exists(), "Privacy policy link is not visible"
    assert installer_window.get_licensing_agreement_link().exists(), "Licensing agreement link is not visible"
    assert installer_window.get_installer_language_dropdown().exists(), "Language dropdown is not visible"


def test_click_licensing_agreement(installer_app):
    installer_window = InstallerWindow(installer_app)

    assert installer_window.click_licensing_agreement(), "Failed to click Licensing Agreement link"
