from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class AutoSuggestionN:
    def Details(self):

        # Initialize the WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # Navigate to the Yatra website
        driver.get("https://www.yatra.com/")
        time.sleep(3)

        # Select the departure city
        driver.find_element(By.XPATH, "//p[@title='New Delhi']").click()
        time.sleep(2)

        departure_from = driver.find_element(By.XPATH, "//input[@id='input-with-icon-adornment']")
        departure_from.send_keys("New Delhi")
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[normalize-space()='New Delhi, (DEL)']").click()
        time.sleep(2)

        # Select the destination city
        depart_to_box = driver.find_element(By.XPATH, "//p[@title='Mumbai']")
        depart_to_box.click()
        time.sleep(2)

        depart_to_input = driver.find_element(By.XPATH, "//input[@id='input-with-icon-adornment']")
        depart_to_input.send_keys("New")
        time.sleep(2)

        # Fetch and filter suggestions starting with "New"
        suggestions = driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-134xwrj']//ul//div")
        with open("abhi.txt", 'w') as f:
            for suggestion in suggestions:
                if suggestion.text.lower().startswith("new"):
                    f.write(suggestion.text + "\n")

        for suggestion in suggestions:
            if "New York, (NYC)" in suggestion.text:
                suggestion.click()
                time.sleep(2)
                break

        # Select the departure date
        departure_date = driver.find_element(By.XPATH, "//div[@class='css-rd021u']")
        departure_date.click()
        time.sleep(2)

        date_list = driver.find_elements(By.XPATH, "//div[contains(@aria-label,'2024-12')]//div")
        for date in date_list:
            if date.get_attribute("aria-label") == 'Choose Wednesday, December 18th, 2024':
                date.click()
                time.sleep(2)
                break

        # Select the return date
        return_date = driver.find_element(By.XPATH, "(//span[@class='css-ft1j42'])[1]")
        return_date.click()
        time.sleep(2)

        return_date_list = driver.find_elements(By.XPATH, "//div[contains(@aria-label,'2024-12')]//div")
        for return_list in return_date_list:
            if return_list.get_attribute("aria-label") == "Choose Sunday, December 22nd, 2024":
                return_list.click()
                time.sleep(2)
                break

        print("done")

        # Click the search button
        Search = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
        Search.click()
        time.sleep(4)

        # Close the browser
        driver.quit()

# Create an instance and call the method
a = AutoSuggestionN()
a.Details()