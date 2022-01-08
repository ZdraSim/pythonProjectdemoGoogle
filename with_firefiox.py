from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from testconst import ENDNOTE
from testconst import URL

driver: WebDriver = webdriver.Firefox(executable_path="C:\Program Files (x86)\selenium drivers/geckodriver.exe")
driver.get(URL)

title = driver.title
language = driver.find_element(By.ID, "SIvCob").text

print(title)
print(language)
print(ENDNOTE)

driver.quit()