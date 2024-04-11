from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

# Navigate to the desired website
driver.get("https://www.linkedin.com")

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Find and interact with elements
username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='session_key']")))
username_field.send_keys("pankajsoni7788@gmail.com")

password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='session_password']")))
password_field.send_keys("Pankaj.soni@321")

sign_in_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Sign in')]")))
sign_in_button.click()

# Wait for the page to load after sign-in
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))

search_field = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
company_name = input("Enter the company name: ")
number_of_pages = 5
search_field.send_keys(company_name)
time.sleep(1)
# //button[text()='People']

people_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='People']")))
people_btn.click()


search_field.send_keys(Keys.ENTER)
# Function to click all "Connect" buttons
while(number_of_pages!=0):
    def click_connect_buttons():
        connect_buttons = driver.find_elements(By.XPATH, "//span[text()='Connect']")
        for button in connect_buttons:
            button.click()
    
    # Navigate to the next page and click all "Connect" buttons
    next_page_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='{number_of_pages}']")))
    next_page_button.click()
    number_of_pages -=1


# Perform additional actions as needed

# Close the browser
driver.quit()