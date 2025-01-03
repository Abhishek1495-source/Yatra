import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from faker import Faker
# name=Faker().name()
# print(name)
class FindElement:
    def Detsild(self):
        # Initialize the WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()


        parent_window = driver.current_window_handle

        # Interact with the "Join Yatra Prime" banner
        driver.find_element(By.XPATH, "//img[@alt='Yatra Prime Banner']").click()
        time.sleep(2)

        # Navigate back to the main page
        driver.back()

        # Interact with the "Corporates/SME" section
        driver.find_element(By.XPATH, "//span[contains(text(),'Corporates/SME')]").click()
        time.sleep(2)

        # Click on "Corporate Travel"
        driver.find_element(By.XPATH, "//div[@id='simple-popover']//p[1]").click()
        time.sleep(2)

        # Switch back to the parent window
        driver.switch_to.window(parent_window)
        time.sleep(2)

        # Switch again to the "Corporate Travel" section
        all_windows = driver.window_handles
        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                time.sleep(3)
                driver.close()
                time.sleep(2)
                break

        # Add verification or further actions here
        print("Switched to Corporate Travel")
        time.sleep(4)
        driver.switch_to.window(parent_window)
        time.sleep(2)
        driver.find_element(By.XPATH,"//span[@type='travel-agent']").click()
        time.sleep(2)

        driver.switch_to.window(parent_window)
        time.sleep(2)
        login=driver.find_element(By.XPATH,"//span[contains(text(),'Login / Signup')]")
        login.click()
        time.sleep(2)
        Create_account = driver.find_element(By.XPATH, "//p[normalize-space()='Login or Create Account']")
        Create_account.click()
        time.sleep(2)

        input_field = driver.find_element(By.XPATH, "//input[@id='login-input']")
        input_field.click()
        input_field.send_keys("Abhishek@mydocsy.com")
        time.sleep(2)
        input_field.send_keys(Keys.ENTER)
        time.sleep(3)
        # Close the driver
        driver.quit()

# Create an instance of the class and call the method
a = FindElement()
a.Detsild()
