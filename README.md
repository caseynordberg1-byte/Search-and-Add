# Selenium Python Automation Framework

A robust test automation framework built with Selenium WebDriver, Python, and pytest using the Page Object Model (POM) design pattern.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Writing New Tests](#writing-new-tests)
- [Test Reports](#test-reports)
- [Best Practices](#best-practices)

---

## ✨ Features

- **Page Object Model (POM)** - Organized, maintainable test code
- **Multi-browser support** - Chrome, Firefox, Edge
- **Automatic driver management** - No manual driver downloads needed
- **HTML test reports** - Beautiful, detailed test execution reports
- **Configurable waits** - Robust element interaction handling
- **Test categorization** - Organize tests with custom markers (smoke, regression, etc.)
- **Logging** - Comprehensive test execution logs
- **Reusable components** - Base page with common actions

---

## 🔧 Prerequisites

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Chrome/Firefox/Edge browser** - At least one browser installed

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/selenium-python-framework.git
cd selenium-python-framework
```

### 2. Create a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create reports directory

```bash
mkdir reports
```

---

## ⚙️ Configuration

### Update Application URLs

Edit the page object files to point to your application:

**`pages/home_page.py`:**
```python
HOME_URL = "https://your-application-url.com"
```

**`pages/login_page.py`:**
```python
LOGIN_URL = "https://your-application-url.com/login"
```

### Update Locators

Inspect your application's HTML and update element locators in each page object file:

```python
# Example: Update search box locator
SEARCH_BOX = (By.ID, "your-search-box-id")
```

**How to find locators:**
1. Open your application in Chrome
2. Right-click element → Inspect
3. Look for `id`, `name`, `class`, or `data-*` attributes
4. Test in console: `document.querySelector("#your-id")`

---

## 🧪 Running Tests

### Run all tests

```bash
pytest
```

### Run specific test file

```bash
pytest tests/test_login.py
```

### Run specific test

```bash
pytest tests/test_login.py::TestLogin::test_successful_login
```

### Run tests by marker

```bash
# Run only smoke tests
pytest -m smoke

# Run only login tests
pytest -m login

# Run regression tests
pytest -m regression

# Exclude slow tests
pytest -m "not slow"
```

### Run with specific browser

```bash
# Firefox
pytest --browser=firefox

# Edge
pytest --browser=edge

# Chrome (default)
pytest --browser=chrome
```

### Verbose output

```bash
pytest -v
```

### Run tests and open HTML report

```bash
pytest
# Report saved to: reports/report.html
```

---

## 📝 Writing New Tests

### 1. Create a new page object

```python
# pages/new_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NewPage(BasePage):
    # Locators
    SOME_ELEMENT = (By.ID, "element-id")
    
    # Actions
    def click_element(self):
        self.click(self.SOME_ELEMENT)
    
    # Verifications
    def is_element_visible(self) -> bool:
        return self.is_visible(self.SOME_ELEMENT)
```

### 2. Create a new test file

```python
# tests/test_new_feature.py

import pytest
from pages.new_page import NewPage


class TestNewFeature:
    
    @pytest.mark.smoke
    def test_something(self, driver):
        page = NewPage(driver)
        page.open("https://example.com")
        page.click_element()
        assert page.is_element_visible()
```

### 3. Add custom markers (optional)

Edit `pytest.ini`:
```ini
markers =
    smoke: Quick smoke tests
    regression: Full regression suite
    your_marker: Description here
```

---

## 📊 Test Reports

### HTML Report

After test execution, open `reports/report.html` in a browser:

```bash
# macOS
open reports/report.html

# Windows
start reports/report.html

# Linux
xdg-open reports/report.html
```

### Log File

Detailed logs are saved to `reports/test_log.txt`

---

## 🎯 Best Practices

### 1. **Keep page objects clean**
- Only actions and verifications, no assertions
- One locator per element
- Group related actions into composite methods

### 2. **Write descriptive test names**
```python
# Good
def test_user_can_add_product_to_cart_and_checkout(self, driver):

# Bad
def test_cart(self, driver):
```

### 3. **Use appropriate waits**
- Avoid `time.sleep()` - use explicit waits instead
- Base page already handles waits automatically

### 4. **Follow AAA pattern**
```python
def test_example(self, driver):
    # Arrange
    page = LoginPage(driver)
    
    # Act
    page.login("user", "pass")
    
    # Assert
    assert page.is_login_successful()
```

### 5. **Use markers to organize tests**
```python
@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(self, driver):
    ...
```

---
