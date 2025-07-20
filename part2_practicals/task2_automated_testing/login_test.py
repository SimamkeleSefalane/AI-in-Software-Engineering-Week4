from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

# Navigate to test site
driver.get("https://the-internet.herokuapp.com/login")

# VALID LOGIN
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME, "radius").click()
time.sleep(2)

# Check result
if "Secure Area" in driver.title:
    print("✅ Valid login passed")
else:
    print("❌ Valid login failed")

# INVALID LOGIN
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.CLASS_NAME, "radius").click()
time.sleep(2)

# Check result
error_message = driver.find_element(By.ID, "flash").text
if "Your password is invalid!" in error_message:
    print("✅ Invalid login handled correctly")
else:
    print("❌ Invalid login test failed")

driver.quit()
