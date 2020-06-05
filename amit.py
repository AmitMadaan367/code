from selenium import webdriver
driver = webdriver.Chrome('chromedriver')
driver.get("https://www.google.com/")
print(driver.page_source)