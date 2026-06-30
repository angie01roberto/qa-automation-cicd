from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome for GitHub Actions
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Launch Chrome browser
driver = webdriver.Chrome(options=options)

# Open the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Enter valid username
driver.find_element(By.ID, "username").send_keys("student")

# Enter valid password
driver.find_element(By.ID, "password").send_keys("Password123")

# Click the Login button
driver.find_element(By.ID, "submit").click()

# Wait for page to load
time.sleep(2)

# Verify successful login
if "Logged In Successfully" in driver.page_source:
    print("TEST PASSED")
else:
    print("TEST FAILED")

# Close the browser
driver.quit()
