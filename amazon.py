from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
import time
driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//span[@id='nav-link-accountList-nav-line-1']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[@id='createAccountSubmit']").click()
time.sleep(2)
driver.find_element(By.NAME,"customerName").send_keys("Shekhar Tyagi")
time.sleep(1)
driver.find_element(By.XPATH,"//span[@class='a-dropdown-prompt']").click()
time.sleep(1)
driver.find_element(By.ID,"auth-country-picker_92").click()
time.sleep(1)
driver.find_element(By.ID,"ap_phone_number").send_keys(8826511508)
time.sleep(1)
driver.find_element(By.ID,"ap_email").send_keys("dhakashaka@gmail.com")
time.sleep(1)
driver.find_element(By.NAME,"password").send_keys("Tyagi@12345")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='continue']").click()
time.sleep(5)
driver.close()