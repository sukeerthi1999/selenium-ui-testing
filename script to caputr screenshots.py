from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Use WebDriverManager to download and install the ChromeDriver automatically
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver with the service object
driver = webdriver.Chrome(service=service)

# Set browser window size
driver.set_window_size(1920, 1080)

try:
    # Open a webpage (example)
    driver.get("https://www.geeksforgeeks.org/myCourses")
    time.sleep(2)  # Wait for the page to load fully

    # Hide a dynamic element (if applicable)
    try:
        driver.execute_script("document.querySelector('.some-dynamic-class').style.display='none';")
    except Exception as e:
        print(f"Dynamic element not found or already hidden: {e}")

    # Take a screenshot and save it
    driver.save_screenshot("screenshot.png")
    print("Screenshot captured successfully!")

finally:
    # Close the browser
    driver.quit()
