from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
import time

# Directory to save current screenshots
current_screenshots_dir = "current_screenshots/"

# Create directory if it doesn't exist
if not os.path.exists(current_screenshots_dir):
    os.makedirs(current_screenshots_dir)

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Set browser window size
driver.set_window_size(1920, 1080)

try:
    # Open the target website
    driver.get("https://www.geeksforgeeks.org")
    time.sleep(2)  # Wait for the page to load fully

    # Example: Hide a dynamic element (if applicable)
    try:
        driver.execute_script("document.querySelector('.some-dynamic-class').style.display='none';")
    except Exception as e:
        print(f"Dynamic element not found or already hidden: {e}")

    # Example: Take a screenshot of the homepage
    driver.save_screenshot(os.path.join(current_screenshots_dir, "homepage.png"))

    # Example: Navigate to another page and capture its screenshot
    try:
        driver.find_element("link text", "About Us").click()
        time.sleep(2)  # Wait for the page to load

        # Hide any dynamic elements on this page if needed
        try:
            driver.execute_script("document.querySelector('.another-dynamic-class').style.display='none';")
        except Exception as e:
            print(f"Dynamic element not found or already hidden: {e}")

        driver.save_screenshot(os.path.join(current_screenshots_dir, "about_us.png"))
    except Exception as e:
        print(f"Error navigating to 'About Us': {e}")

    # Repeat the above process for all other pages or components to be tested
finally:
    # Close the browser
    driver.quit()

print("Comparison screenshots captured successfully!")
