from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def check_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.ID, "user-name")
        driver.find_element(By.ID, "password")
        driver.find_element(By.CSS_SELECTOR, "#login-button")
        print("Элементы найдены")
    except NoSuchElementException:
        print("Элементы не найдены")
    finally:
        driver.quit()

check_elements()

