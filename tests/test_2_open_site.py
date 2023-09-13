from selenium import webdriver
from selenium.webdriver.common.by import By            #"By" - это модуль, который содержит классы для локаторов (стратегий для поиска элементов на веб-странице) в Selenium WebDriver. Например, классы By.ID, By.XPATH, By.CSS_SELECTOR и другие предоставляют возможности для поиска элементов на странице по определенным атрибутам или условиям.
from selenium.common.exceptions import NoSuchDriverException    #"NoSuchDriverException" - это модуль, который содержит исключение, которое возникает, когда не удается найти соответствующий драйвер для запуска Selenium WebDriver. Оно позволяет обработать случай отсутствия требуемого драйвера и выполнить соответствующие действия, например, вывести сообщение об ошибке или выбрать альтернативный путь запуска WebDriver.

def test_site_visit():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, "header > a > img")
    except NoSuchDriverException:
        assert False
    assert True

