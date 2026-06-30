from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

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