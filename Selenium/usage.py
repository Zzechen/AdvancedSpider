# a auto test tool,Python+Selenium+PhantomJS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

baidu = 'http://www.baidu.com'
driver = webdriver.Chrome('C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
driver.get(baidu)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print driver.page_source