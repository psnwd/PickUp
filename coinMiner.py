import os
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
load_dotenv()

print("""\


                        ██████╗░██╗░█████╗░██╗░░██╗██╗░░░██╗██████╗░
                        ██╔══██╗██║██╔══██╗██║░██╔╝██║░░░██║██╔══██╗
                        ██████╔╝██║██║░░╚═╝█████═╝░██║░░░██║██████╔╝
                        ██╔═══╝░██║██║░░██╗██╔═██╗░██║░░░██║██╔═══╝░
                        ██║░░░░░██║╚█████╔╝██║░╚██╗╚██████╔╝██║░░░░░
                        ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░
                           PickUp Automated Test Coin Miner v1.0.0 
                                    Developed by BlackCAT
                                            MIT
    """)

url = os.getenv('DOMAIN')
env_type = os.getenv('ENV_TYPE')
address = ""

# Account address
if (env_type == "PROD"):
    address = os.getenv('ADDRESS')
else:
    address = input("[INPUT] Enter your address: ")

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

print("--------------- Booting Up ---------------")


def GetCoin():
    try:
        browser = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=options)
        browser.get(url)

        # 5 min loop
        threading.Timer(300.0, GetCoin).start()

        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div[1]/div/div/div/div[5]/div/div[2]/div/input'))).send_keys(address)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div[1]/div/div/div/div[6]/div/div/button'))).click()

        time.sleep(5)

        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/button'))).click()

        time.sleep(5)

        try:
            isFailed = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[1]'))).text

            print(isFailed)
            if (isFailed == "Transfer Failed"):
                waitSec = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]'))).text

            waitSec = str(waitSec).replace(
                "you are grey listed for ", "You need to wait ")

            print(waitSec)

            return
        except:
            None

        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div/div[1]/a'))).click()

        print("[INFO] Coin added successful")
    except:
        print("[ERROR] Something went wrong")

    print("HI")
    browser.quit()


GetCoin()
