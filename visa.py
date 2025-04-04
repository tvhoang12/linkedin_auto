from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from twocaptcha import TwoCaptcha


# Khởi tạo trình duyệt
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
# link = "https://service2.diplo.de/rktermin/extern/appointment_showMonth.do?locationCode=hano&realmId=1407&categoryId=3389&zarsrc=30&utm_source=zalo&utm_medium=zalo&utm_campaign=zalo%20RK-Termin%20-%20Bereich%20w%C3%A4hlen"

def bypassFirstCaptcha(driver):
    wait = WebDriverWait(driver, 10)
    
    # Tìm phần tử CAPTCHA (có ảnh nền)
    captcha_div = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@style, 'background:white url')]")))

    # Chụp ảnh toàn bộ trang
    screenshot_path = "full_screenshot.png"
    driver.save_screenshot(screenshot_path)

    # Lấy tọa độ của CAPTCHA
    location = captcha_div.location  # Vị trí (x, y)
    size = captcha_div.size          # Kích thước (width, height)

    # Đọc ảnh chụp toàn màn hình
    img = mpimg.imread(screenshot_path)

    # Xác định tọa độ cắt ảnh
    left = int(location['x'])
    top = int(location['y'])
    right = left + int(size['width'])
    bottom = top + int(size['height'])

    # Cắt ảnh CAPTCHA
    cropped_img = img[top:bottom, left:right]

    # Lưu ảnh CAPTCHA đã cắt
    plt.imsave('captcha_cropped.png', cropped_img)
    print("Đã lưu ảnh CAPTCHA!")
    
    
    
def fillForm(driver):
    wait = WebDriverWait(driver, 30)
    
    driver.get("https://service2.diplo.de/rktermin/extern/choose_category.do?locationCode=hano&realmId=290&categoryId=2732")
    
    continueButton = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//a[contains(@href, "extern/appointment")]')))
    continueButton[0].click()
    time.sleep(1)
    
    # Chờ cho đến khi phần tử có ID 'captcha' xuất hiện
    # bypassFirstCaptcha(driver)
    time.sleep(5)
    
    setAppointment = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@onclick="return startCommitRequest();" and @class="arrow"]'))).click()
    time.sleep(1)
    
    bookThisAppointment = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Book this appointment')]"))).click()
    time.sleep(5)
    
    # capcha = wait.until(EC.presence_of_element_located((By.XPATH, '//captcha')))
    # bypassFirstCaptcha(driver)
    
    try:
        lastName = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="lastname"]'))).send_keys("Nguyen Thi")
        time.sleep(1)
        print("Đã nhập họ")
        firstName = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="firstname"]'))).send_keys("Quynh")
        time.sleep(1)
        print("Đã nhập tên")
        passport = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="passport"]'))).send_keys("C6795039")
        time.sleep(1)
        print("Đã nhập số hộ chiếu")
        email = driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("kiencgp@gmail.com")
        time.sleep(1)
        print("Đã nhập email")
        emailrepeat = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="emailrepeat"]'))).send_keys("kiencgp@gmail.com")
        time.sleep(1)
        print("Đã nhập lại email")
        phone = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="phone"]'))).send_keys("0913034286")
        time.sleep(1)
        print("Đã nhập số điện thoại")
        
        time.sleep(10)
        
    except Exception as e:
        print("Lỗi khi nhập thông tin:", e)
        return

fillForm(driver)
driver.quit()