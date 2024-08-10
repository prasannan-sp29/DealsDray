import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

drivers = {
    'Chrome': webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
    'Firefox': webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())),
}

devices = {
    "Desktop": [
        {"name": "Desktop_1920x1080", "width": 1920, "height": 1080},
        {"name": "Desktop_1366x768", "width": 1366, "height": 768},
        {"name": "Desktop_1536x864", "width": 1536, "height": 864},
    ],
    "Mobile": [
        {"name": "Mobile_360x640", "width": 360, "height": 640},
        {"name": "Mobile_414x896", "width": 414, "height": 896},
        {"name": "Mobile_375x667", "width": 375, "height": 667},
    ]
}

def capture_screenshot(browser_name, device_name, resolution, driver):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    folder_path = f"./screenshots/{browser_name}/{device_name}/{resolution['name']}"
    os.makedirs(folder_path, exist_ok=True)
    file_path = f"{folder_path}/Screenshot-{timestamp}.png"

    driver.set_window_size(resolution['width'], resolution['height'])
    time.sleep(2)  
    driver.save_screenshot(file_path)
    # print(f"Screenshot saved to {file_path}")
    return file_path

for browser_name, driver in drivers.items():
    driver.get('https://www.getcalley.com/page-sitemap.xml')

    wait = WebDriverWait(driver, 10)
    for i in range(2, 7):
        link = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//tr)[{i}]/td/a")))
        link.click()
        time.sleep(1)
        for device_name, resolutions in devices.items():
            for resolution in resolutions:
                capture_screenshot(browser_name, device_name, resolution, driver)
        driver.back()
        wait.until(EC.element_to_be_clickable((By.XPATH, f"(//tr)[{i+1}]/td/a")))
        time.sleep(0.5)
    driver.quit()
