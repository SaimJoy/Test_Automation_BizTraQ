import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
time.sleep(5)

stn_btn=driver.find_element(By.XPATH, '//*[@id="mat-menu-panel-1"]/div/button[1]' )
stn_btn.click()
time.sleep(4)

#locate custom module
cust_mdl = driver.find_element(By.XPATH, '//*[@id="mat-tab-label-0-2"]/div/span')
cust_mdl.click()
time.sleep(3)
add_mdl = driver.find_element(By.XPATH, '/html/body/div[1]/app-root/div/main-nav/mat-drawer-container/mat-drawer-content/div/app-settings/mat-tab-group/mat-tab-header/div[2]/div/div/div[3]/div[1]/button/span[1]/mat-icon ' )
add_mdl.click()
time.sleep(3)

#frame locate
modal = WebDriverWait(driver, 12).until( EC.presence_of_element_located((By.ID, "cdk-overlay-1")) )
# Handle the modal pop-up
# # You can interact with the elements inside the modal using their locators
# # For example, you can click a button inside the modal pop-up:
time.sleep(2)
Name=modal.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/mat-dialog-container/new-module-add-dialog/div/div/mat-tab-group/div/mat-tab-body/div/form/mat-card/mat-card-content/div[1]/mat-form-field/div/div[1]/div/input')
time.sleep(2)
Name.send_keys("Test Module ")
#For random input
def generate_random_string(length=3):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
unique_value = generate_random_string()
Name.send_keys(unique_value)
time.sleep(2)
#description
#descp= driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/mat-dialog-container/new-module-add-dialog/div/div/mat-tab-group/div/mat-tab-body/div/form/mat-card/mat-card-content/div[2]/mat-form-field')
#time.sleep(3)
#descp.send_keys("This a test module")


sv_btn= driver.find_element(By.XPATH , '/html/body/div[4]/div[2]/div/mat-dialog-container/new-module-add-dialog/div/div/mat-tab-group/div/mat-tab-body/div/form/mat-card-actions/button[1]/span[1]')
sv_btn.click()

time.sleep(5)
modal_1 = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "mat-tab-label-4-1")) )
driver.execute_script("arguments[0].click();", modal_1)
#Permission check box

checkbox_1 = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/mat-dialog-container/new-module-add-dialog/div/div/mat-tab-group/div/mat-tab-body[2]/div/app-user-access-control/mat-card/mat-card-content/mat-checkbox[1]/label/span[2]')
driver.execute_script("arguments[0].click();", checkbox_1)
time.sleep(3)
#ACCESS CHECK BOX
checkbox_2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/mat-dialog-container/new-module-add-dialog/div/div/mat-tab-group/div/mat-tab-body[2]/div/app-user-access-control/mat-card/mat-card-content/mat-checkbox[2]')
driver.execute_script("arguments[0].click();", checkbox_2)
time.sleep(3)
submit_button=driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/mat-dialog-container/new-module-add-dialog/div/div/mat-tab-group/div/mat-tab-body[2]/div/div/button[1]")
driver.execute_script("arguments[0].click();", submit_button)

time.sleep(10)

#again check the added module is there or not



#referesh page
#driver.refresh()

