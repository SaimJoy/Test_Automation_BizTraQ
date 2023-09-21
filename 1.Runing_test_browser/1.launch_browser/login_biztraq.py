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
driver.maximize_window()

#locate element
username = driver.find_element(By.ID,"mat-input-0")
if username is not None:
    print("User Name Element found")
else:
    print("not found")
username.clear()
username.send_keys("joy.triulta")
time.sleep(5)

#locate button element
nxt_btn= driver.find_element(By.XPATH,
                             "/html/body/div[1]/app-root/div/main-nav/mat-drawer-container/mat-drawer-content/div/app-login/div[1]/div[1]/p[2]/button")
nxt_btn.click()
time.sleep(5)

#locate password box
u_pass= driver.find_element(By.XPATH,'//*[@id="passwrdInput"]' )
if username is not None:
    print("Password Element found")
else:
    print("not found")
time.sleep(5)

u_pass.send_keys("12345678")
time.sleep(5)

lg_btn=driver.find_element(By.XPATH ," /html/body/div[1]/app-root/div/main-nav/mat-drawer-container/mat-drawer-content/div/app-login/div[1]/div[1]/p[5]/button")
lg_btn.click()
time.sleep(5)

#locate settins element
stn_icon= driver.find_element(By.XPATH,
                             "/html/body/div[1]/app-root/div/main-nav/mat-toolbar/mat-toolbar-row/div/button[1]/span[1]/mat-icon" )
driver.execute_script("arguments[0].click();", stn_icon)  #there is an overlapped element thats why we used this JS method
time.sleep(7)

stn_btn=driver.find_element(By.XPATH, '//*[@id="mat-menu-panel-1"]/div/button[1]' )
stn_btn.click()
time.sleep(5)

