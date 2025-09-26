from pathlib import Path

def verify_desktop_to_web_flow(redirect, custom_value, lang_of_url):
    """Checks if the desktop-to-web redirect flow is present in the latest installer log.

    Useful for verifying that the correct redirect and custom parameters are logged during installation.
    """
    path = Path(r"C:\ProgramData\Avanquest\Driver Updater\logs")
    if not path.exists():
        raise FileNotFoundError(f"Log directory not found: {path}")

    installer = list(path.rglob("*installer*"))
    if not installer:
        raise FileNotFoundError("Not found installer log")

    log_file = max(installer, key=lambda p: p.stat().st_mtime)
    # opened_log_file = log_file.read_text(encoding="utf-8", errors="ignore")
    try:
        with open(log_file, encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f, 1):
                if f"redirect-to. name={redirect}" in line:
                    for j, line2 in enumerate(f, start=i+1):
                        if f"execute. what=\"https://paygw.adaware.com/redirect/custom/pch-driver-updater?customValue={custom_value}&lang={lang_of_url}\"" in line2:
                            return True
            return False
    except (OSError, IOError) as e:
        raise RuntimeError(f"Cannot read log file")
