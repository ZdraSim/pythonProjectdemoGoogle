from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from testconst import ENDNOTE
from testconst import URL

driver: WebDriver = webdriver.Chrome(executable_path="C:\Program Files (x86)\selenium drivers/chromedriver.exe")

driver.get(URL)

title = driver.title
language = driver.find_element(By.ID, "SIvCob").text
print(title)
print(language)
print(ENDNOTE)
#element = WebDriverWait(driver, 10)
#element.until(EC.presence_of_element_located((By.ID, 'example')))


driver.quit()