from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Specify the correct path for geckodriver
geckodriver_path = "C:/Program Files/geckodriver/geckodriver.exe"

# Set up Firefox options
options = Options()
options.headless = False  # Change to True if you want to hide the browser UI

# Set up the service for geckodriver
service = Service(executable_path=geckodriver_path)

# Initialize the Firefox WebDriver with the specified service and options
driver = webdriver.Firefox(service=service, options=options)

# Define the URLs for the screenshots
urls = [
    "https://www.geeksforgeeks.org/",
    "https://www.wikipedia.org/",
    "https://www.python.org/"
]

# Loop through the URLs and take screenshots
for index, url in enumerate(urls, start=1):
    driver.get(url)  # Navigate to the URL
    time.sleep(2)  # Wait for the page to load
    screenshot_path = f"C:/Users/saisu/Desktop/screenshot_{index}.png"  # Save screenshots to your Desktop
    driver.save_screenshot(screenshot_path)  # Take a screenshot
    print(f"Screenshot saved for {url} as screenshot_{index}.png")

# Close the browser after taking screenshots
driver.quit()
