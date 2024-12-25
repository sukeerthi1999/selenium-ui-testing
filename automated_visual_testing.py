import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Define the base directory to save screenshots
base_dir = "C:/Users/saisu/Computer vision project/screenshots"

# Ensure that the required subdirectories exist
os.makedirs(os.path.join(base_dir, "baseline"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "current"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "anomalies"), exist_ok=True)

# Function to save screenshot
def save_screenshot(driver, page_name, img_type="baseline"):
    if img_type == "baseline":
        img_path = os.path.join(base_dir, "baseline", f"{page_name}_baseline.png")
    elif img_type == "current":
        img_path = os.path.join(base_dir, "current", f"{page_name}_current.png")
    elif img_type == "anomaly":
        img_path = os.path.join(base_dir, "anomalies", f"{page_name}_anomaly.png")

    driver.save_screenshot(img_path)  # Save screenshot at specified path
    print(f"Screenshot saved at {img_path}")

# Setup WebDriver
def setup_selenium_with_firefox():
    geckodriver_path = "C:/Program Files/geckodriver/geckodriver.exe"  # Specify geckodriver path
    service = Service(geckodriver_path)
    options = Options()
    options.headless = False  # Set to True for headless mode (no UI)

    # Initialize Firefox WebDriver
    driver = webdriver.Firefox(service=service, options=options)
    return driver

# Test the setup by visiting a few pages and saving screenshots
def test_screenshots():
    # Initialize WebDriver
    driver = setup_selenium_with_firefox()

    # List of webpages to visit
    pages = [
        {"url": "https://www.geeksforgeeks.org", "name": "geeks_for_geeks"},
        {"url": "https://www.wikipedia.org", "name": "wikipedia"},
        {"url": "https://www.python.org", "name": "python_org"}
    ]

    # Take and save screenshots for each page
    for page in pages:
        driver.get(page["url"])
        save_screenshot(driver, page["name"], "baseline")  # Save baseline screenshot

        # For demonstration, save a current screenshot after reloading the page (you can customize further)
        driver.get(page["url"])
        save_screenshot(driver, page["name"], "current")

        # Optional: Add code to highlight anomalies (this part depends on your anomaly detection logic)
        # Here we'll simply save another screenshot in the 'anomalies' folder for demonstration purposes
        save_screenshot(driver, page["name"], "anomaly")

    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    test_screenshots()
