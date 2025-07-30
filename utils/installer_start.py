import logging
import time

from pywinauto.application import Application

def start_installer(exe_path):
    try:
        installer_app = Application(backend="uia").start(exe_path)
        return installer_app
    except Exception as e:
        logging.error(f"Failed to start installer: {e}")
        return None

