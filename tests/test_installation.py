
from page_objects.installer.locators import InstallerLocators
from utils.process_utils import wait_for_process_start
from utils.log_analyzer import verify_desktop_to_web_flow


def test_visible_installer_window(installer_window):
    assert installer_window.is_installer_window_visible(), "Installer window is not visible"
    assert installer_window.get_installer_window_class_name() == "H-SMILE-FRAME-DC", "Installer window title does not match expected value"
    assert installer_window.get_install_button(**InstallerLocators.INSTALLER_BUTTON).exists(), "Install button is not visible"
    assert installer_window.get_privacy_policy_link().exists(), "Privacy policy link is not visible"
    assert installer_window.get_licensing_agreement_link().exists(), "Licensing agreement link is not visible"
    assert installer_window.get_installer_language_dropdown().exists(), "Language dropdown is not visible"

def test_click_license_agreement(installer_window, browser_manager):
    redirect = "eula"
    custom_value = "eula"
    lang_of_url = "English"
    browser = browser_manager.get_default_browser()
    assert installer_window.click_license_agreement(), "Failed to click Licensing Agreement link"
    assert wait_for_process_start(browser), f"Browser process '{browser}' did not start"
    browser_manager.kill_opened_browser(browser)
    assert verify_desktop_to_web_flow(redirect, custom_value, lang_of_url), \
         f"Expected redirect flow not found in logs for redirect={redirect}, custom_value={custom_value}, lang={lang_of_url}"




