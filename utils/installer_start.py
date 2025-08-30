import logging
from pywinauto.application import Application
import subprocess

def start_installer(exe_path):
    try:
        installer_app = Application(backend="uia").start(exe_path)
        return installer_app
    except Exception as e:
        logging.error(f"Failed to start installer: {e}")
        return None





# def is_signed_correctly(file_path):
#     cmd = ['signtool', 'verify', '/pa', file_path]
#     result = subprocess.run(cmd, capture_output=True, text=True)
#
#     print(result.stdout)
#     print(result.stderr)
#
#     return result.returncode == 0
#
#
# file_path = r"C:\Users\VKalyniuk\Downloads\installer_9.1.60906.1183_internal"
#
# is_signed_correctly(file_path)