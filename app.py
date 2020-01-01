from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")
emailelement = driver.find_element(By.XPATH, './/*[@id="email"]')
emailelement.send_keys("08137045484")


passelement = driver.find_element(By.XPATH, './/*[@id="pass"]')
passelement.send_keys("modelfranc")


loginelement = driver.find_element(By.XPATH, './/*[@id="loginbutton"]')
loginelement.click()


with open("quotes.txt", "r") as f:
    # length = len(f.readlines())
    number = 27
    hut = 26
    while number > 0:
        post = f.readline()
        j = post + ".\n#"+str(hut) + "Left"
        number -= 1
        hut -= 1

        print(j)

        statusupdate = driver.find_element_by_class_name(
            "navigationFocus")
        time.sleep(5)

        statusupdate.send_keys(j)
        time.sleep(5)

        buttons = driver.find_elements_by_class_name('selected')
        time.sleep(5)

        for button in buttons:
            if button.text == 'Post':
                button.click()
                break

        time.sleep(5)
        driver.get("https://www.facebook.com")
