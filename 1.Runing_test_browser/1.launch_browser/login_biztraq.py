from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import random
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
time.sleep(3)

stn_btn=driver.find_element(By.XPATH, '//*[@id="mat-menu-panel-1"]/div/button[1]' )
stn_btn.click()
time.sleep(3)

#locate custom module
cust_mdl = driver.find_element(By.XPATH, '//*[@id="mat-tab-label-0-2"]/div/span')
cust_mdl.click()
time.sleep(3)
add_mdl = driver.find_element(By.XPATH, '/html/body/div[1]/app-root/div/main-nav/mat-drawer-container/mat-drawer-content/div/app-settings/mat-tab-group/mat-tab-header/div[2]/div/div/div[3]/div[1]/button/span[1]/mat-icon ' )
add_mdl.click()
time.sleep(3)

#add new module
#generate random string for input

random_string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(10))

new_mdl_form = driver.find_element(By.NAME, 'siteName ')
new_mdl_form.send_keys(random_string)
time.sleep(4)