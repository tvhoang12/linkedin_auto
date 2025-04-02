import csv
from datetime import date
import random
from time import sleep
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from time import sleep
from random import randint, randrange
import time
import json
import read_xpath

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument("start-maximized")
options.add_argument("--incognito")
#browser = webdriver.Chrome(options=options)
link = "https://www.linkedin.com/login"
account = "htvhtv1239@gmail.com"
passwd = "Hoang@11204"
# Thời gian bắt đầu
start_time = time.time()
# Thời gian chạy của vòng lặp (24 giờ = 86400 giây)
loop_duration = 2 * 60
# Từ khóa tìm kiếm nhóm
searchKey = "Artificial"

def load_xpath(file_path="xpath.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def loginLink(browser, link, account):
    browser.get(link)
    wait1 = WebDriverWait(browser, 30)  # Maximum wait time of 10 seconds
    username = wait1.until(EC.visibility_of_element_located((By.XPATH, read_xpath.EmailField)))
    sleep(randint(5, 7))

    username.send_keys(account)
    wait2 = WebDriverWait(browser, 30)  # Maximum wait time of 10 seconds
    password = wait2.until(EC.visibility_of_element_located((By.XPATH, read_xpath.PasswordField)))
    sleep(randint(5, 7))
    password.send_keys(passwd)
    sleep(randint(2, 5))

    wait3 = WebDriverWait(browser, 30)  # Maximum wait time of 10 seconds
    signin = wait3.until(EC.element_to_be_clickable((By.XPATH, read_xpath.LoginButton)))
    sleep(randint(5, 7))
    signin.click()
    #đợi 10s, có thể await
    sleep(randint(7, 12))
    
user_info = {
    "email": "testuser@gmail.com",
    "username": "testuser123",
    "password": "Test@1234",
    "confirm_password": "Test@1234",
    "first_name": "Test",
    "last_name": "User",
    "phone": "0987654321",
}

def register(browser, user_data, xpath_data):
    wait = WebDriverWait(browser, 10)

    for field_name, input_value in user_data.items():
        try:
            # Lấy XPath từ file JSON
            field_xpath = xpath_data.get(field_name, "")
            if field_xpath:
                input_element = wait.until(EC.visibility_of_element_located((By.XPATH, field_xpath)))
                input_element.send_keys(input_value)
                print(f"✔ Nhập {field_name}: {input_value}")
            else:
                print(f"⚠ Không tìm thấy XPath cho {field_name}")
        except Exception as e:
            print(f"❌ Lỗi khi nhập {field_name}: {e}")

    # Nhấn nút đăng ký (giả sử XPath của nút lưu trong JSON)
    try:
        register_button_xpath = xpath_data.get("register_button", "")
        if register_button_xpath:
            register_button = wait.until(EC.element_to_be_clickable((By.XPATH, register_button_xpath)))
            register_button.click()
            print("✔ Đã nhấn nút đăng ký")
        else:
            print("⚠ Không tìm thấy XPath của nút đăng ký")
    except Exception as e:
        print(f"❌ Lỗi khi nhấn nút đăng ký: {e}")