import psutil
import subprocess
from winreg import OpenKey, HKEY_CURRENT_USER, QueryValueEx

class BrowserProcessManager:
    """Handles browser process management and default browser detection on Windows."""

    def __init__(self):
        """Initializes supported process attributes and URL schemes."""
        self.attrs = ["name"]
        self.schemes =("http", "https")

    def __iter__(self):
        """Returns an iterator over running processes for browser checks."""
        return psutil.process_iter(self.attrs)

    def get_default_browser(self):
        """Finds the default browser executable name from the Windows registry.

        Useful for determining which browser is set as default for web links.
        """
        browsers = {
            "chromehtml": "chrome.exe",
            "msedgehtm": "msedge.exe",
            "operastable": "opera.exe",
            "operagxstable": "opera.exe",
        }
        for s in self.schemes:
            try:
                with OpenKey(HKEY_CURRENT_USER,
                             rf"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\{s}\UserChoice") as k:
                    i = QueryValueEx(k, "ProgId")[0].lower()

                if i in browsers:
                    default_browser = browsers[i]
                    return default_browser
                elif i.startswith("firefox"):
                    default_browser = "firefox.exe"
                    return default_browser

            except FileNotFoundError:
                print(f"[WARN] default browser prog_id  not found: scheme={s}")
                continue
        return "browser not found"

    def check_is_browser_running(self, browser):
        """Checks if a browser process with the given name is currently running.

        Useful for verifying if a specific browser is active.
        """
        for proc in self:
            try:
                if proc.info.get("name") == browser:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return False

    @staticmethod
    def kill_opened_browser(browser):
        """Attempts to terminate all running processes of the specified browser.

        Useful for ensuring no browser instances are open before certain operations.
        """
        try:
            result = subprocess.run(["taskkill", "/F", "/IM", browser, "/T"], capture_output=True, text=True)
            if result.returncode == 0:
                return True
            else:
                return False, f"taskkill for {browser} failed"
        except Exception as e:
            return False, f"exception: {e}"
