import time
from pywinauto import Application
from conftest import installer_app
from resources.desktop_link_checker import verify_desktop_to_web_flow
from utils.browser_checker import  ProcessChecker
from conftest import chrome_browser, firefox_browser
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

def test_installer_links(installer_app):
    installer_window = InstallerWindow(installer_app)
    process_check = ProcessChecker()
    installer_window.click_privacy_policy()
    installer_window.click_licensing_agreement()
    time.sleep(5)

    privacy_policy_link_is_valid = verify_desktop_to_web_flow("privacy", "privacy", "English")
    if not privacy_policy_link_is_valid:
        assert False, "Privacy policy link redirect validation failed"

    license_agreement_is_valid = verify_desktop_to_web_flow("eula", "eula", "English")
    if not license_agreement_is_valid:
        assert False, "License agreement link redirect validation failed"




