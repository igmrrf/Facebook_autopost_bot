from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")
emailelement = driver.find_element(By.XPATH, './/*[@id="email"]')
emailelement.send_keys("your_email_or_mobile")


passelement = driver.find_element(By.XPATH, './/*[@id="pass"]')
passelement.send_keys("your_password")


loginelement = driver.find_element(By.XPATH, './/*[@id="loginbutton"]')
loginelement.click()

# Using a local file for quotes/status
with open("quotes.txt", "r") as file:
    total_number_of_quotes = 24
    for line in file:
        quote = line + ".\n#"+str(total_number_of_quotes - 1) + "Left"
        print(quote)

        statusupdate = driver.find_element_by_class_name(
            "navigationFocus")
        time.sleep(5)

        statusupdate.send_keys(quote)
        time.sleep(5)

        buttons = driver.find_elements_by_class_name('selected')
        time.sleep(5)

        for button in buttons:
            if button.text == 'Post':
                button.click()
                break

        time.sleep(5)
        driver.get("https://www.facebook.com")

# Calling an api for random quotes/status
