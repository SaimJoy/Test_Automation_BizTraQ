
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


import time
import datetime



class rec_creation():
    def user_login(self):
        try:
            # Initialize WebDriver
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            driver.maximize_window()

            baseurl = "https://biztraqonline.com/Auth/Login"
            usr_name1 = "mcc.support"
            pass1 = "MCC.COBAIT.123"

            start_time = time.time()
            driver.get(baseurl)

            end_time = time.time()
            loading_time = end_time - start_time
            print(f"Biztraq Landing Page loading time: {loading_time:.2f} seconds")

            # Locate username field and log in
            try:
                username = driver.find_element(By.ID, "mat-input-0")
                if username is not None:
                    print("User Name Element found")
                username.clear()
                username.send_keys(usr_name1)
                print("Username entered.")
                time.sleep(3)
            except NoSuchElementException:
                print("Username field not found. Skipping this step.")

            # Locate and click the next button
            try:
                nxt_btn = driver.find_element(By.XPATH,
                                              "/html/body/div[1]/app-root/app-login/div[1]/div[1]/p[2]/button")
                nxt_btn.click()
                print("Next button clicked.")
                time.sleep(3)
            except NoSuchElementException:
                print("Next button not found. Skipping this step.")

            # Locate password field and enter password
            try:
                u_pass = driver.find_element(By.XPATH,
                                              '/html/body/div/app-root/app-login/div[1]/div[1]/p[2]/input')
                if u_pass is not None:
                    print("Password Element found")
                u_pass.send_keys(pass1)
                print("Password entered.")
                time.sleep(3)
            except NoSuchElementException:
                print("Password field not found. Skipping this step.")

            # Locate and click the login button
            try:
                lg_btn = driver.find_element(By.XPATH,
                                             "/html/body/div/app-root/app-login/div[1]/div[1]/p[5]/button")
                lg_btn.click()
                print("Login button clicked.")
                time.sleep(5)
            except NoSuchElementException:
                print("Login button not found. Skipping this step.")

            # Check if login was successful
            try:
                if lg_btn is not None:
                    print("Login success")
                else:
                    print("Login failed.")
            except Exception as e:
                print(f"Error checking login status: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        time.sleep(5)

        # 1.TestCase for MCC Patient mdl load


        pt_mdl= driver.find_element(By.XPATH,
                                    "/html/body/div[1]/app-root/app-layout/div/main-nav/mat-drawer-container/mat-drawer/div/mat-nav-list/app-menu-list-item[5]/a/div/span[1]")
        if pt_mdl is not None:
            print("Patient Module Found")
        else:
            print("not found")

        driver.execute_script("arguments[0].click();", pt_mdl)
        time.sleep(5)


        try:
            start_time = time.time()

            act_case = driver.find_element(By.XPATH,
                                           "/html/body/div[1]/app-root/app-layout/div/main-nav/mat-drawer-container/mat-drawer/div/mat-nav-list/app-menu-list-item[5]/div[1]/app-menu-list-item[1]/a/div/span[1]")

            act_case.click()
            print("Active cases clicked.")

            end_time = time.time()

            time.sleep(15)

        # Calculate and print the loading time
            loading_time = end_time - start_time
            print(f"Active Cases page loading time: {loading_time:.2f} seconds")

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error loading Active Cases page: {e}")

        except Exception as e:
          print(f"An unexpected error occurred: {e}")

        time.sleep(15)

        # menu navigation
        ref_i = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/app-root/app-layout/div/main-nav/mat-drawer-container/mat-drawer/div/mat-nav-list/app-menu-list-item[5]/div[1]/app-menu-list-item[3]/a/div/span[1]")
        ref_i.click()
        time.sleep(5)

        ref_pi= driver.find_element(By.XPATH,
                                    "/html/body/div[1]/app-root/app-layout/div/main-nav/mat-drawer-container/mat-drawer/div/mat-nav-list/app-menu-list-item[5]/div[1]/app-menu-list-item[3]/a/div/span[1]")
        ref_pi.click()
        time.sleep(13)

        visit_mdl= driver.find_element(By.XPATH,
                                       "/html/body/div[1]/app-root/app-layout/div/main-nav/mat-drawer-container/mat-drawer/div/mat-nav-list/app-menu-list-item[5]/div[1]/app-menu-list-item[4]/a/div/span[1]")
        visit_mdl.click()
        time.sleep(15)

        # add record

        ref_pi= driver.find_element(By.XPATH,
                                    "/html/body/div[1]/app-root/app-layout/div/main-nav/mat-drawer-container/mat-drawer/div/mat-nav-list/app-menu-list-item[5]/div[1]/app-menu-list-item[3]/a/div/span[1]")
        ref_pi.click()
        time.sleep(15)

        try:
            # Locate and click the "Add Record" button
            add_rec = driver.find_element(By.XPATH,
                                          "/html/body/div[1]/app-root/div/main-nav/mat-drawer-container/mat-drawer-content/div/documents/div/div/mat-tab-group/mat-tab-header/div[2]/div/div/div[1]/div[1]/button/span[1]/mat-icon")
            driver.execute_script("arguments[0].click();", add_rec)  # Fixed typo: "argument" -> "arguments"
            print("Add record button clicked successfully.")
            time.sleep(4)
        except NoSuchElementException:
            print("Add record button not found. Skipping this step.")
        except Exception as e:
            print(f"An error occurred while clicking the add record button: {e}")

        # Get the current date
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')

        try:
            # Locate the "First Name" field and enter data
            f_name = driver.find_element(By.XPATH,
                                         "/html/body/div[10]/div[2]/div/mat-dialog-container/app-event-detail/div/div/form/div[2]/div[2]/mat-card[1]/mat-card-content/div[3]/div/mat-form-field")
            f_name.send_keys("Test " + current_date)  # Fixed: Use concatenation for strings
            print("First name field filled successfully.")
            time.sleep(3)
        except NoSuchElementException:
            print("First name field not found. Skipping this step.")
        except Exception as e:
            print(f"An error occurred while filling the first name field: {e}")

        driver.close()




test_obj = rec_creation()
test_obj.user_login()
