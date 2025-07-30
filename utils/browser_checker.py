import psutil

# def check_is_chrome_running(processes):
#     for process in processes:
#         if process.name() == "firefox.exe":
#             return True
#     print("Chrome is not running.")
#     return None

def check_is_firefox_running(processes):
    for process in processes:
        if process.name() == "firefox.exe":
            print(f"Firefox is running with PID: {process.pid}")
            return True
    print("Firefox is not running.")
    return None

check_is_firefox_running(psutil.process_iter(['pid', 'name', 'exe', 'cmdline', 'create_time']))