import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
from datetime import datetime

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demo.dealsdray.com/')
wait = WebDriverWait(driver, 10)

time.sleep(2)
user_name = driver.find_element(By.XPATH,"//input[@id='mui-1']")
user_name.send_keys('prexo.mis@dealsdray.com')

password = driver.find_element(By.XPATH,"//input[@id='mui-2']")
password.send_keys('prexo.mis@dealsdray.com')
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//button[@class='MuiButtonBase-root has-submenu compactNavItem css-46up3a']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[@href='/mis/orders']//button[@name='child']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//button[normalize-space()='Add Bulk Orders']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[contains(@class,'MuiOutlinedInput-root MuiInputBase-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall css-uodm64')]").click()

time.sleep(3)

keyboard = Controller()
keyboard.type("C:\\Users\\Prasannan S\\Downloads\\demo-data.xlsx")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(4)
driver.find_element(By.XPATH,"//button[normalize-space()='Import']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Validate Data']").click()
time.sleep(3)

driver.switch_to.alert.accept()
time.sleep(5)
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
driver.save_screenshot(f"C:\\Users\\Prasannan S\\Documents\\screenshot-{timestamp}.png")
time.sleep(3)

driver.quit()
