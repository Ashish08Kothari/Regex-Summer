from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login_instagram(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)  # Wait for the page to load fully

    # Login
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Wait for login to complete
    time.sleep(5)

    # Handle "Save Your Login Info?" popup
    try:
        not_now_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
        not_now_button.click()
        time.sleep(3)
    except:
        pass  # Ignore if not present

    # Handle "Turn on Notifications" popup
    try:
        not_now_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
        not_now_button.click()
        time.sleep(3)
    except:
        pass  # Ignore if not present

    # Optional: Keep the browser open for inspection
    print("Logged in successfully. Browser will remain open for 30 seconds.")
    time.sleep(30)

    driver.quit()

if __name__ == "__main__":
    username = "username"
    password = "Password"
    login_instagram(username, password)
