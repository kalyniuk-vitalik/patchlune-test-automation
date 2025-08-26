import psutil
import subprocess
from winreg import OpenKey, HKEY_CURRENT_USER, QueryValueEx



class BrowserProcessManager:
    def __init__(self):
        self.attrs = ["name"]
        self.schemes =("http", "https")

    def __iter__(self):
        return psutil.process_iter(self.attrs)

    def get_default_browser(self):
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
        for proc in self:
            try:
                if proc.info.get("name") == browser:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return False

    @staticmethod
    def kill_opened_browser(browser):
        try:
            result = subprocess.run(["taskkill", "/F", "/IM", browser, "/T"], capture_output=True, text=True)
            if result.returncode == 0:
                return True
            else:
                return False, f"taskkill for {browser} failed"
        except Exception as e:
            return False, f"exception: {e}"

    # def check_is_chrome_running(self):
    #     for proc in psutil.process_iter(self.attrs):
    #         if proc.name() == "chrome.exe":
    #             return True
    #     return False
    #
    # def check_is_firefox_running(self):
    #     for proc in psutil.process_iter(self.attrs):
    #         if proc.name() == "firefox.exe":
    #             return True
    #     return False
    #
    # def check_is_edge_running(self):
    #     for proc in psutil.process_iter(self.attrs):
    #         if proc.name() == "msedge.exe":
    #             return True
    #     return False

