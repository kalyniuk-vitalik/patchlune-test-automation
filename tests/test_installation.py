import pytest
from page_objects.installer.locators import InstallerLocators
from conftest import exe_path
from utils.process_utils import wait_for_process_start
from utils.log_analyzer import verify_desktop_to_web_flow
from utils.signature_verifier import get_signature
from test_data.signatures import ADAWARE_SIGNATURE
from test_data.expected_log_patterns import LICENSE_AGREEMENT_EXPECTATIONS, PRIVACY_POLICY_EXPECTATIONS

def test_exe_signature(exe_path):
    assert get_signature(exe_path) == ADAWARE_SIGNATURE, "Signature verification failed!"

def test_visible_installer_window(installer_window):
    assert installer_window.is_installer_window_visible(), "Installer window is not visible"
    assert installer_window.get_installer_window_class_name() == "H-SMILE-FRAME-DC", "Installer window title does not match expected value"
    assert installer_window.get_install_button(**InstallerLocators.INSTALLER_BUTTON).exists(), "Install button is not visible"
    assert installer_window.get_privacy_policy_link().exists(), "Privacy policy link is not visible"
    assert installer_window.get_licensing_agreement_link().exists(), "Licensing agreement link is not visible"
    assert installer_window.get_installer_language_dropdown().exists(), "Language dropdown is not visible"

@pytest.mark.parametrize("lang_code", ["en"])
def test_click_license_agreement(installer_window, browser_manager, lang_code):
    data = LICENSE_AGREEMENT_EXPECTATIONS[lang_code]
    browser = browser_manager.get_default_browser()
    assert installer_window.click_license_agreement(), "Failed to click Licensing Agreement link"
    assert wait_for_process_start(browser), f"Browser process '{browser}' did not start"
    browser_manager.kill_opened_browser(browser)
    assert verify_desktop_to_web_flow(redirect = data["redirect"], custom_value = data["custom_value"], lang_of_url = data["lang_of_url"]), \
         f"[{lang_code}] Expected redirect not found"

@pytest.mark.parametrize("lang_code", ["en"])
def test_click_privacy_policy(installer_window, browser_manager, lang_code):
    data = PRIVACY_POLICY_EXPECTATIONS[lang_code]
    browser = browser_manager.get_default_browser()
    assert installer_window.click_privacy_policy(), "Failed to click Privacy Policy link"
    assert wait_for_process_start(browser), f"Browser process '{browser}' did not start"
    browser_manager.kill_opened_browser(browser)
    assert verify_desktop_to_web_flow(redirect = data["redirect"], custom_value = data["custom_value"], lang_of_url = data["lang_of_url"]), \
         f"[{lang_code}] Expected redirect not found"

# def test_start_instalation(installer_window):
#     installer_window.click_install()
