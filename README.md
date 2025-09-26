# 🚀 Driver Updater Automation Testing Framework

A Python-based automation testing framework for Driver Updater.  
This project uses **pytest** and **pywinauto** for UI automation, structured with the **Page Object Model (POM)** to ensure maintainability, scalability, and reliability.  
Utility modules extend functionality with process management, log analysis, signature verification, and browser handling.

---

## 📂 Project Structure

```text
project-root/
├── page_objects/      # Page Object Model classes for installer UI automation
│   ├── base_page.py
│   ├── installer_window.py
│   └── locators.py
│
├── utils/             # Utility modules (browser management, installer startup, logging, etc.)
│   ├── browser_checker.py
│   ├── installer_start.py
│   ├── log_analyzer.py
│   ├── process_utils.py
│   └── signature_verifier.py
│
├── tests/             # Test cases for installer automation
│   └── test_installation.py
│
├── test_data/         # Static test data and resources
│   ├── expected_log_patterns.py
│   └── signatures.py
│
├── conftest.py        # Pytest fixtures and configuration
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## ⚙️ Installation

**Clone the repository:**

```bash
git clone <repository-url>
cd <project-root>
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests

**Run all tests:**

```bash
pytest
```

**Run a single test file:**

```bash
pytest tests/test_installation.py::test_exe_signature
```

---

## 🛠 Technologies Used

* **Python 3.12.2**
* [pytest](https://pytest.org/) — test framework  
* [pywinauto](https://pywinauto.github.io/) — Windows UI automation  
* **Page Object Model (POM)** — design pattern for maintainable test code  
* [psutil](https://pypi.org/project/psutil/) — process management (browser and installer monitoring)  
* **Windows Registry (`winreg`)** — detecting default browser settings  
* **PowerShell (`Get-AuthenticodeSignature`)** — verifying digital signatures of executables  
* [pathlib](https://docs.python.org/3/library/pathlib.html) — filesystem operations  
* [logging](https://docs.python.org/3/library/logging.html) — error/info logging  
* [subprocess](https://docs.python.org/3/library/subprocess.html) — running system commands  
* [json](https://docs.python.org/3/library/json.html) — parsing signature verification results  
* [time](https://docs.python.org/3/library/time.html) — waiting for processes  

---

## 📌 Non-Functional Requirements

* **Operating System:** Windows 10 or later (required for pywinauto and registry access)  
* **Performance:** Tests should execute efficiently, ideally within 30–60 seconds each (if it possible)  
* **Maintainability:** Modular structure using Page Object Model and utility modules ensures easy updates and scalability  

---

## 📖 Notes

* **Page Object Model** separates UI interactions from test logic  
* **Utility modules** (`utils/`) provide reusable helpers for browsers, processes, logs, and signatures  
* **Test data** is centralized under `test_data/` for maintainability  
* **Logs** are automatically analyzed to verify installer behavior  

---
