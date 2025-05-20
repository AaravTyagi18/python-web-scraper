from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome driver with webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Flipkart search page
driver.get("https://www.flipkart.com/search?q=smartphones")

# Wait for content to load
time.sleep(5)  # Increase if internet is slow

# Close login popup if it appears
try:
    close_button = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    close_button.click()
except:
    pass  # Popup didn’t appear

# Extract product names and prices
product_names = driver.find_elements(By.CLASS_NAME, "_4rR01T")
product_prices = driver.find_elements(By.CLASS_NAME, "_30jeq3")

# Display data
for name, price in zip(product_names, product_prices):
    print(f"Product: {name.text} | Price: {price.text}")

# Close the browser
driver.quit()
