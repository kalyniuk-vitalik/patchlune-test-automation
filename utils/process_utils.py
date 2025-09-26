import time
import psutil

def wait_for_process_start(process_name):
    """Waits for a process with the given name to start within a timeout.

    Useful for synchronizing actions that depend on the launch of a specific process.
    """
    for _ in range(5 * 2):
        time.sleep(2)
        for proc in psutil.process_iter(["name"]):
            if proc.info.get("name") == process_name:
                return True

    return False
