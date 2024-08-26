from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the first URL
    driver.get("https://www.tutorialsfreak.com/")

    # Wait for the first button to be clickable and click it
    first_button_xpath = "/html/body/div/div[2]/div[2]/section[1]/div/div[1]/div/div/div/div[2]/button"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, first_button_xpath))).click()

    # Wait for the new tab to open (assuming it opens quickly, adjust the sleep time if necessary)
    time.sleep(10)  # Adjust this wait time as needed
    
    button=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[1]/a"))).click()
    time.sleep(10)
    # Open the second URL in a new tab using JavaScript
    second_url = "https://www.google.com"
    driver.execute_script(f"window.open('{second_url}', 'new_tab')")

    # Switch to the new tab (index 1 of window_handles)
    driver.switch_to.window(driver.window_handles[1])

    # Optionally, perform further operations on the second tab
    print("Current URL in second tab:", driver.current_url)

    # Example: Close the second tab after 5 seconds
    time.sleep(10)  # Wait for 10 seconds
    driver.close()

    # Switch back to the first tab (index 0 of window_handles)
    driver.switch_to.window(driver.window_handles[0])

    # Optionally, perform further operations on the first tab
    print("Current URL in first tab:", driver.current_url)

except Exception as e:
    print(f"Exception occurred: {str(e)}")

finally:
    # Close the browser session
    driver.quit()