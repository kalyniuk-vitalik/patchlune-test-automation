import time
import psutil

def wait_for_process_start(process_name):
    for _ in range(5 * 2):
        time.sleep(2)
        for proc in psutil.process_iter(["name"]):
            if proc.info.get("name") == process_name:
                return True

    return False
# Waits for a process with the given name to start. Checks every 0.5 seconds until timeout.
