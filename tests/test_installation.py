import pytest
from page_objects.installer.locators import InstallerLocators
from conftest import exe_path
from utils.process_utils import wait_for_process_start
from utils.log_analyzer import verify_desktop_to_web_flow
from utils.signature_verifier import get_signature
from test_data.signatures import NEUTRAL_SIGNATURE
from test_data.expected_log_patterns import LICENSE_AGREEMENT_EXPECTATIONS, PRIVACY_POLICY_EXPECTATIONS
import time

def test_exe_signature(exe_path):
    """Verifies that the installer executable has the expected digital signature."""
    assert get_signature(exe_path) == NEUTRAL_SIGNATURE, "Signature verification failed!"

def test_visible_installer_window(installer_window):
    """Checks that the installer window and all key UI elements are visible and have correct properties."""
    assert installer_window.is_installer_window_visible(), "Installer window is not visible"
    assert installer_window.get_installer_window_class_name() == "H-SMILE-FRAME-DC", "Installer window title does not match expected value"
    assert installer_window.get_install_button(**InstallerLocators.INSTALLER_BUTTON).exists(), "Install button is not visible"
    assert installer_window.get_privacy_policy_link().exists(), "Privacy policy link is not visible"
    assert installer_window.get_licensing_agreement_link().exists(), "Licensing agreement link is not visible"
    assert installer_window.get_installer_language_dropdown().exists(), "Language dropdown is not visible"

@pytest.mark.parametrize("lang_code", ["en"])
def test_click_license_agreement(installer_window, browser_manager, lang_code):
    """Verifies that clicking the Licensing Agreement link opens the browser and redirects to the correct URL."""
    data = LICENSE_AGREEMENT_EXPECTATIONS[lang_code]
    browser = browser_manager.get_default_browser()
    assert installer_window.click_license_agreement(), "Failed to click Licensing Agreement link"
    assert wait_for_process_start(browser), f"Browser process '{browser}' did not start"
    browser_manager.kill_opened_browser(browser)
    assert verify_desktop_to_web_flow(redirect = data["redirect"], custom_value = data["custom_value"], lang_of_url = data["lang_of_url"]), \
         f"[{lang_code}] Expected redirect not found"

@pytest.mark.parametrize("lang_code", ["en"])
def test_click_privacy_policy(installer_window, browser_manager, lang_code):
    """Verifies that clicking the Privacy Policy link opens the browser and redirects to the correct URL."""
    data = PRIVACY_POLICY_EXPECTATIONS[lang_code]
    browser = browser_manager.get_default_browser()
    assert installer_window.click_privacy_policy(), "Failed to click Privacy Policy link"
    assert wait_for_process_start(browser), f"Browser process '{browser}' did not start"
    browser_manager.kill_opened_browser(browser)
    assert verify_desktop_to_web_flow(redirect = data["redirect"], custom_value = data["custom_value"], lang_of_url = data["lang_of_url"]), \
         f"[{lang_code}] Expected redirect not found"

def test_start_installation (installer_window):
    """Checks that clicking the install button starts installation and displays the correct labels."""
    installer_window.click_install_button()
    installing_patchlune= installer_window.get_label(**InstallerLocators.INSTALLING_LABEL)
    do_not_turn_your_device_off = installer_window.get_label(**InstallerLocators.DO_NOT_TURN_OFF_LABEL)
    assert installing_patchlune.window_text() == "Installing", f"{installing_patchlune.window_text()}"
    assert do_not_turn_your_device_off.window_text() == "Please do not turn your device off", f"{do_not_turn_your_device_off.window_text()}"
