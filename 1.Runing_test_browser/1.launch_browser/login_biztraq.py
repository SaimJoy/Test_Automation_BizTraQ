from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time

#driver setup
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://biztraqonline.com/Login")

#locate element
username = driver.find_element(By.ID,"mat-input-0")
if username is not None:
    print("User Name Element found")
else:
    print("not found")
username.clear()
username.send_keys("joy.triulta")
time.sleep(5)

#nxt_btn= driver.find_element(By. "")
#if username is not None:
    #print("User Name Element found")
#else:
    #print("not found")

#nxt_btn.click()

#u_pass= driver.find_element(By.XPATH, ""


time.sleep(10)


