from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace with your GitHub credentials
GITHUB_USERNAME = "PrashuGit1"
GITHUB_PASSWORD = "Git@prakash1"

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open GitHub login page
driver.get("https://github.com/login")

# Let page load
time.sleep(2)

# Find username and password fields and fill them
driver.find_element(By.XPATH, '//*[@id="login_fiel"]').send_keys(GITHUB_USERNAME)
driver.find_element(By.ID, "password").send_keys(GITHUB_PASSWORD)

# Click the "Sign in" button
driver.find_element(By.NAME, "commit").click()

# Wait a few seconds to observe the result
time.sleep(5)

# Optional: Close the browser
driver.quit()
