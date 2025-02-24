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
from time import sleep
from random import randint, randrange
import time
import threading
from datetime import datetime
import logging
import sys
import pyodbc
from database_interact import Log_FacebookBot
import read_xpath

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument("start-maximized")
options.add_argument("--incognito")
#browser = webdriver.Chrome(options=options)
link = "https://www.linkedin.com/login"
listAccount = ["Vietnamtopapp@gmail.com"]
passwd = "Langnghiem@79"
lock = threading.Lock()
# Thời gian bắt đầu
start_time = time.time()
# Thời gian chạy của vòng lặp (24 giờ = 86400 giây)
loop_duration = 2 * 60

def logFile(account, link, status, timeAcc):
    with lock:
        try:
            with open("log.txt", "a") as file2:
                file2.write("Account: "+account + "\n" + "Link: " +link+ "\n" + "Status: " + status + "\n" + "Time: " + timeAcc + "\n")
        except FileNotFoundError:
            print("File not found.")

def openFile(href):
    with lock:
        try:
            with open("check.txt", 'r') as file:
                file_content = file.read()
                if href not in file_content:
                    with open("check.txt", "a") as file2:
                        file2.write(href+"\n")
                    print(f"Link {href} đã được chạy rồi")
                    return True
                else:
                    return False
        except FileNotFoundError:
            print("File not found checkLink.")
            return False

def create_content():
    quotes = [
        "Cuộc sống không phải là chờ đợi bão tố qua đi, mà là học cách điều chỉnh cho tốt nhất trong cơn bão.",
        "Hãy là thay đổi mà bạn muốn thấy trong thế giới."
        "Hãy sống như thể bạn đang sống lần cuối, và hãy học như thể bạn sẽ sống mãi mãi.",
        "Không có gì quý giá hơn tự do và độc lập.",
        "Hãy là thay đổi mà bạn muốn thấy trong thế giới.",
        "Hạnh phúc không phải là mục tiêu cuối cùng của cuộc sống, mà là cách sống.",
        "Cuộc sống không có ý nghĩa, trừ khi bạn tìm ra ý nghĩa cho nó.",
        "Không có thành công nào cao cả nếu bạn không hạnh phúc.",
        "Hãy làm việc với đam mê và không bao giờ từ bỏ. Bởi vì nếu bạn làm điều bạn thích, bạn sẽ không bao giờ phải làm việc một ngày nào trong đời.",
        "Cuộc sống không phải là về việc chờ đợi mưa tạnh, mà là về việc học cách mua một cây dù.",
        "Hãy làm điều bạn có thể, với những gì bạn có, tại nơi bạn đang đứng.",
        "Hãy sống theo cách bạn muốn, không phải theo cách người khác muốn bạn sống.",
        "Thành công không phải là chìa khóa của hạnh phúc. Hạnh phúc là chìa khóa của thành công. Nếu bạn yêu những gì bạn đang làm, bạn sẽ thành công.",
        "Thay đổi không bao giờ đến nếu bạn chỉ ngồi đó chờ đợi nó.",
        "Hãy tin tưởng vào chính mình. Bạn đang có trí tuệ, kiến thức và khả năng làm việc. Hãy sử dụng chúng để điều chỉnh cuộc sống của mình.",
        "Đừng để ai đó làm cho bạn cảm thấy như mình là một người bình thường. Bạn không phải là như vậy.",
        "Cuộc sống là những gì xảy ra với chúng ta trong khi chúng ta đang bận rộn lên kế hoạch cho những kế hoạch khác.",
        "Không có ngày mai nào tuyệt vời hơn hôm nay để bắt đầu.",
        "Lớn lên không phải là việc mất đi những giấc mơ, mà là việc biết mà vẫn có thể bay cao.",
        "Thất bại là cơ hội để bắt đầu lại một cách thông minh hơn.",
        "Cuộc sống là sự kết hợp của những giấc mơ và hành động.",
        "Hãy sống một cuộc sống mà bạn tự hào khi nhìn lại.", "Hãy yêu bản thân mình trước khi bạn yêu ai đó.",
        "Đừng bao giờ từ bỏ. Thất bại là một phần không thể tránh được của hành trình của chúng ta. Hãy học từ nó và tiếp tục đi.",
        "Hãy sống mỗi ngày như thể đó là ngày cuối cùng của cuộc sống.",
        "Hãy làm một điều mà bạn sợ hãi, và bạn sẽ khám phá ra rằng không có gì sợ hãi nữa."
    ]
    return random.choice(quotes)


def post_to_facebook(browser):
        # Tìm và nhấp vào ô "Bạn đang nghĩ gì?"
        post_box = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, read_xpath.PostBox))
        )
        post_box.click()

        # Nhập nội dung bài viết từ create_content()
        post_content = create_content()
        post_area = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.XPATH, read_xpath.PostArea))
        )
        post_area.send_keys(post_content)

        # Đợi một chút trước khi đăng
        time.sleep(10)

        # Nhấn nút "Đăng"
        post_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, read_xpath.PostButton))
        )
        post_button.click()

        print(f" Đã đăng bài: {post_content}")

        time.sleep(5)

def loginlinkedin(browser, link, account):
    browser.get(link)
    wait1 = WebDriverWait(browser, 30)  # Maximum wait time of 10 seconds
    username = wait1.until(EC.visibility_of_element_located((By.XPATH, read_xpath.EmailField)))
    sleep(randint(5, 7))
    username.send_keys(account)
    #username.send_keys("saturnlle01@gmail.com")
    wait2 = WebDriverWait(browser, 30)  # Maximum wait time of 10 seconds
    password = wait2.until(EC.visibility_of_element_located((By.XPATH, read_xpath.PasswordField)))
    sleep(randint(5, 7))
    password.send_keys(passwd)
    sleep(20)
    try:
        wait3 = WebDriverWait(browser, 30)  # Maximum wait time of 10 seconds
        login = wait3.until(EC.element_to_be_clickable((By.XPATH, read_xpath.LoginButtonEn)))
        sleep(randint(5, 7))
        login.click()
    except:
        wait3 = WebDriverWait(browser, 30)  # Maximum wait time of 10 seconds
        login = wait3.until(EC.element_to_be_clickable((By.XPATH, read_xpath.LoginButtonVi)))
        sleep(randint(5, 7))
        login.click()
    #đợi 10s, có thể await
    sleep(randint(7, 12))


    """
    
    # Duyệt tất cả các nhóm
    wait4 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
    clickGroup = wait4.until(EC.element_to_be_clickable((By.XPATH, read_xpath.GroupsTab)))
    clickGroup.click()
    sleep(5)
    wait5 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
    clickGroup = wait5.until(
            EC.element_to_be_clickable((By.XPATH, read_xpath.JoinedGroups)))
    clickGroup.click()
    sleep(5)
    # Cuộn xuống tìm tất cả thẻ
    try:
            print('access to scrollbar1')
            i = 0
            while i < 10:
                # Cuộn xuống
                browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                # Chờ một chút để trang cuộn xuống
                print("xuống cuối1")
                sleep(2)
                i += 1
    except:
            print('cannot access to scrollbar1')

    # Lấy tất cả các nhóm
    print("div to 1")
    wait = WebDriverWait(browser, 10)
    elementTo = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, read_xpath.GroupList)))
    print("div to 1 into")
    browser.implicitly_wait(10)
    element = elementTo.find_elements(By.XPATH, read_xpath.GroupLinks)
    print(f"Tong so link: {len(element)}")
    for i in element:
        href = i.get_attribute("href")
        print(f"ban oi: {href}")
    """

def scanUser(browser):
        wait4 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
        clickGroup = wait4.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/friends/']")))
        clickGroup.click()
        sleep(5)
        wait4 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
        clickGroup = wait4.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/friends/list/']")))
        clickGroup.click()
        sleep(5)
        try:
            print('access to scrollbar')
            i = 0
            while i < 10:
                # Cuộn xuống
                browser.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
                 # Chờ một chút để trang cuộn xuống
                print("xuống cuối")
                sleep(2)
                i += 1
            sleep(randint(20, 40))
        except:
            print('cannot access to scrollbar')
        wait4 = WebDriverWait(browser, 10)
        element = wait4.until(
            EC.visibility_of_all_elements_located
                ((By.XPATH, '//a[starts-with(@href, "https://www.facebook.com/profile.php?id=") and @role="link"]')))
        for i in element:
            href = i.get_attribute("href")
            print(f"ban oi: {href}")
            i.click()
            sleep(5)
            wait4 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
            clickGroup = wait4.until(EC.element_to_be_clickable((By.XPATH, f'//a[@href="{href}&sk=about" and @role="tab"]')))
            clickGroup.click()
            sleep(5)
            wait4 = WebDriverWait(i, 10)
            element = wait4.until(
                EC.visibility_of_element_located
                ((By.XPATH,
                  "//*[contains(concat(' ', @class, ' '), 'x78zum5 xdt5ytf x1wsgfga x9otpla')]")))
            print(f'Ten tui la: {element.text}')
            wait4 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
            clickGroup = wait4.until(
                EC.element_to_be_clickable((By.XPATH, f'//a[@href="{href}&sk=about_overview" and @role="link"]')))
            clickGroup.click()
            sleep(5)
            wait4 = WebDriverWait(i, 10)
            element = wait4.until(
                EC.visibility_of_all_elements_located
                ((By.XPATH,
                  "//*[contains(concat(' ', @class, ' '), 'x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xamitd3 xsyo7zv x16hj40l x10b6aqq x1yrsyyn')]")))
            print(f"about_overview {len(element)}")
            for iz in element:
                print(iz.text)

            #about_work_and_education
            wait4 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
            clickGroup = wait4.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//a[@href="{href}&sk=about_work_and_education" and @role="link"]')))
            clickGroup.click()
            sleep(5)
            wait4 = WebDriverWait(i, 10)
            element = wait4.until(
                EC.visibility_of_all_elements_located
                ((By.XPATH, "//*[contains(concat(' ', @class, ' '), 'x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xamitd3 xsyo7zv x16hj40l x10b6aqq x1yrsyyn')]")))
            print(f"about_work_and_education {len(element)}")
            for iz in element:
                print(iz.text)

            #&sk=about_places
            wait4 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
            clickGroup = wait4.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//a[@href="{href}&sk=about_places" and @role="link"]')))
            clickGroup.click()
            sleep(5)
            wait4 = WebDriverWait(i, 10)
            element = wait4.until(
                EC.visibility_of_all_elements_located
                ((By.XPATH, "//*[contains(concat(' ', @class, ' '), 'x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xamitd3 xsyo7zv x16hj40l x10b6aqq x1yrsyyn')]")))
            print(f"about_work_and_education {len(element)}")
            for iz in element:
                print(iz.text)

            #&sk=about_contact_and_basic_info
            wait4 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
            clickGroup = wait4.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//a[@href="{href}&sk=about_contact_and_basic_info" and @role="link"]')))
            clickGroup.click()
            sleep(5)
            wait4 = WebDriverWait(i, 10)
            element = wait4.until(
                EC.visibility_of_all_elements_located
                ((By.XPATH, "//*[contains(concat(' ', @class, ' '), 'x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xamitd3 xsyo7zv x16hj40l x10b6aqq x1yrsyyn')]")))
            print(f"about_work_and_education {len(element)}")
            for iz in element:
                print(iz.text)

            #&sk=about_family_and_relationships
            wait4 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
            clickGroup = wait4.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//a[@href="{href}&sk=about_family_and_relationships" and @role="link"]')))
            clickGroup.click()
            sleep(5)
            wait4 = WebDriverWait(i, 10)
            element = wait4.until(
                EC.visibility_of_all_elements_located
                ((By.XPATH, "//*[contains(concat(' ', @class, ' '), 'x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xamitd3 xsyo7zv x16hj40l x10b6aqq x1yrsyyn')]")))
            print(f"about_work_and_education {len(element)}")
            for iz in element:
                print(iz.text)

            #&sk=about_details
            wait4 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
            clickGroup = wait4.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//a[@href="{href}&sk=about_details" and @role="link"]')))
            clickGroup.click()
            sleep(5)
            wait4 = WebDriverWait(i, 10)
            element = wait4.until(
                EC.visibility_of_all_elements_located
                ((By.XPATH, "//*[contains(concat(' ', @class, ' '), 'x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xamitd3 xsyo7zv x16hj40l x10b6aqq x1yrsyyn')]")))
            print(f"about_work_and_education {len(element)}")
            for iz in element:
                print(iz.text)

            #&&sk=about_life_events
            wait4 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
            clickGroup = wait4.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//a[@href="{href}&sk=about_life_events" and @role="link"]')))
            clickGroup.click()
            sleep(5)
            wait4 = WebDriverWait(i, 10)
            element = wait4.until(
                EC.visibility_of_all_elements_located
                ((By.XPATH, "//*[contains(concat(' ', @class, ' '), 'x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xamitd3 xsyo7zv x16hj40l x10b6aqq x1yrsyyn')]")))
            print(f"about_work_and_education {len(element)}")
            for iz in element:
                print(iz.text)

def messageOthers(browser):
        print("messageOthers")

def autoReply(browser):
        # Duyệt tất cả các nhóm
        wait4 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
        clickGroup = wait4.until(EC.element_to_be_clickable((By.XPATH, read_xpath.GroupsTab)))
        clickGroup.click()
        sleep(5)
        wait5 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
        clickGroup = wait5.until(
            EC.element_to_be_clickable((By.XPATH, read_xpath.JoinedGroups)))
        clickGroup.click()
        sleep(5)
        # Cuộn xuống tìm tất cả thẻ
        try:
            print('access to scrollbar1')
            i = 0
            while i < 10:
                # Cuộn xuống
                browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                # Chờ một chút để trang cuộn xuống
                print("xuống cuối1")
                sleep(2)
                i += 1
        except:
            print('cannot access to scrollbar1')

        # Lấy tất cả các nhóm
        print("div to 1")
        wait = WebDriverWait(browser, 10)
        elementTo = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, read_xpath.GroupList)))
        print("div to 1 into")
        browser.implicitly_wait(10)
        element = elementTo.find_elements(By.XPATH, read_xpath.GroupLinks)
        print(f"Tong so link: {len(element)}")
        for i in element:
            href = i.get_attribute("href")
            print(f"ban oi: {href}")
        # Duyệt từng nhóm.
        ez = 0
        sleep(randint(5, 7))
        for i in element:
            if ez >2:
                try:
                        href = i.get_attribute("href")
                        print(f"ban oi: {href}")
                        # click từng link vào nhóm
                        wait6 = WebDriverWait(i, 30)  # Maximum wait time of 10 seconds
                        eachGroup = wait6.until(
                                EC.element_to_be_clickable((By.XPATH, read_xpath.ClickGroup)))
                        eachGroup.click()
                        print('passsssssss1x')

                        # Check popup "Rời khỏi Trang"
                        try:
                            browser.implicitly_wait(5)
                            close = browser.find_element(By.XPATH,
                                                        read_xpath.LeavePagePopupVi).click()
                        except:
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            read_xpath.LeavePagePopupEn).click()
                            except:
                                print("khong popup leavepage")

                        # dosomethings
                        sleep(randint(5, 10))
                        # Check popup "Quảng cáo"
                        try:
                            browser.implicitly_wait(5)
                            close = browser.find_element(By.XPATH,
                                                        f"read_xpath.CloseAdPopupVi").click()
                        except:
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            read_xpath.CloseAdPopupEn).click()
                            except:
                                print("khong popup quang cao")
                        # nếu đến link thứ 3 thì bắt đầu click truy cập vào nhóm
                        print("Toidayroi")
                        # phải sleep
                        sleep(randint(3, 5))
                        # Tìm GroupFeed chứa tất cả các bài Post
                        try:
                            wait7 = WebDriverWait(i, 10)
                            GroupFeed = wait7.until(
                                EC.visibility_of_element_located
                                ((By.XPATH, read_xpath.GroupFeed)))
                        except:
                            wait7 = WebDriverWait(i, 10)
                            GroupFeed = wait7.until(
                                EC.visibility_of_element_located
                                ((By.XPATH, read_xpath.GroupPreview)))
                        print('passsssssss1x')
                        # Lướt xuống để bot thấy được lượng bài post nhất định
                        # Tạo đối tượng ActionChains
                        actions = ActionChains(browser)
                        # Cuộn trang web xuống
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        sleep(5)

                        wait9 = WebDriverWait(GroupFeed, 10)
                        feedx = wait9.until(
                            EC.presence_of_all_elements_located
                            ((By.XPATH, read_xpath.PostsContainer)))
                        print('passsssssss1x')
                        print(f'thuc su co may: {len(feedx)}')
                        izzz =1
                        for i in feedx:
                            print(izzz)
                            if izzz ==2:
                                break
                            print(f'thuc su co may: {i.text}')
                            try:
                                sleep(randint(5, 6))
                                browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", i)
                                browser.implicitly_wait(10)
                                clickReplyde = i.find_element(By.XPATH,'(//div[@role="button" and text()="Phản hồi"])[1]').click()
                                print("clickReplyde")
                                sleep(randint(5, 6))
                                browser.implicitly_wait(10)
                                replyDe = i.find_element(By.XPATH,'//div[@aria-label="Viết phản hồi công khai…"]/p/span[2]')
                                replyDe.send_keys("http://leduymanh.com/vi/elementor-1226/")
                                sleep(randint(5, 6))
                                replyDe.send_keys(Keys.RETURN)
                                print("DaReply")
                                sleep(randint(12, 15))
                                with open("logGroupReply.txt", "a") as file:
                                    file.write(f"So reply: {izzz} \nLink: {href}")
                                izzz+=1

                            except Exception as e:
                                print(e)
                                print("chuaReply")
                                break

                            sleep(randint(2, 3))
                except Exception as e:
                        try:
                            wait6 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
                            eachGroup = wait6.until(
                                EC.element_to_be_clickable((By.XPATH, read_xpath.ClickGroup)))
                            eachGroup.click()
                            print('passsssssss2x')
                            # dosomething
                            # Check popup "Rời khỏi Trang"
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            read_xpath.LeavePagePopupVi).click()
                            except:
                                try:
                                    browser.implicitly_wait(5)
                                    close = browser.find_element(By.XPATH,
                                                                read_xpath.LeavePagePopupEn).click()
                                except:
                                    print("khong popup leavepage")

                            # dosomethings
                            sleep(randint(5, 10))
                            # Check popup "Quảng cáo"
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            f"read_xpath.CloseAdPopupVi").click()
                            except:
                                try:
                                    browser.implicitly_wait(5)
                                    close = browser.find_element(By.XPATH,
                                                                read_xpath.CloseAdPopupEn).click()
                                except:
                                    print("khong popup quangcao")
                            # nếu đến link thứ 3 thì bắt đầu click truy cập vào nhóm
                            print("Toidayroi")
                            # phải sleep
                            sleep(randint(3, 5))
                            # Tìm GroupFeed chứa tất cả các bài Post
                            try:
                                wait7 = WebDriverWait(i, 10)
                                GroupFeed = wait7.until(
                                    EC.visibility_of_element_located
                                    ((By.XPATH, read_xpath.GroupFeed)))
                            except:
                                wait7 = WebDriverWait(i, 10)
                                GroupFeed = wait7.until(
                                    EC.visibility_of_element_located
                                    ((By.XPATH, read_xpath.GroupPreview)))
                            print('passsssssss1x')
                            # Lướt xuống để bot thấy được lượng bài post nhất định
                            # Tạo đối tượng ActionChains
                            actions = ActionChains(browser)
                            # Cuộn trang web xuống
                            actions.send_keys(Keys.PAGE_DOWN).perform()
                            actions.send_keys(Keys.PAGE_DOWN).perform()
                            actions.send_keys(Keys.PAGE_DOWN).perform()
                            sleep(5)

                            wait9 = WebDriverWait(GroupFeed, 10)
                            feedx = wait9.until(
                                EC.presence_of_all_elements_located
                                ((By.XPATH, read_xpath.PostsContainer)))
                            print('passsssssss1x')
                            print(f'thuc su co may: {len(feedx)}')
                            izzz =1
                            for i in feedx:
                                print(izzz)
                                if izzz ==2:
                                    break
                                print(f'thuc su co may: {i.text}')
                                try:
                                    sleep(randint(5, 6))
                                    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", i)
                                    browser.implicitly_wait(10)
                                    clickReplyde = i.find_element(By.XPATH,'(//div[@role="button" and text()="Phản hồi"])[1]').click()
                                    print("clickReplyde")
                                    sleep(randint(5, 6))
                                    browser.implicitly_wait(10)
                                    replyDe = i.find_element(By.XPATH,'//div[@aria-label="Viết phản hồi công khai…"]/p/span[2]')
                                    replyDe.send_keys("http://leduymanh.com/vi/elementor-1226/")
                                    sleep(randint(5, 6))
                                    replyDe.send_keys(Keys.RETURN)
                                    print("DaReply")
                                    sleep(randint(12, 15))
                                    with open("logGroupReply.txt", "a") as file:
                                        file.write(f"So reply: {izzz} \nLink: {href}")
                                    izzz+=1
                                    #Lấy Xpath Restricted POST
                                    try:
                                        browser.implicitly_wait(5)
                                        restricted = browser.find_element(By.XPATH, read_xpath.RestrictedPost)
                                        print("Restricted")

                                        try:
                                            browser.implicitly_wait(5)
                                            close = browser.find_element(By.XPATH,
                                                                         f"read_xpath.CloseAdPopupVi").click()
                                        except:
                                            try:
                                                browser.implicitly_wait(5)
                                                close = browser.find_element(By.XPATH,
                                                                             read_xpath.CloseAdPopupEn).click()
                                            except:
                                                print("khong popup quangcao")
                                        #Suspend 1 hours, do other thing before break
                                        #Do any else
                                        interval_minutes = 5
                                        ack_suspension_hours = 1
                                        suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                        interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                        # Wait for the specified interval and check if 2 hours have passed
                                        elapsed_time = 0
                                        while elapsed_time < suspension_duration:
                                            print("Checking after every {} minutes...".format(interval_minutes))
                                            time.sleep(interval_duration)
                                            elapsed_time += interval_duration
                                        #Break
                                    except:
                                        try:
                                            browser.implicitly_wait(5)
                                            restricted = browser.find_element(By.XPATH, read_xpath.RestrictedAll)
                                            print("Restricted All")
                                            try:
                                                browser.implicitly_wait(5)
                                                close = browser.find_element(By.XPATH,
                                                                             f"read_xpath.CloseAdPopupVi").click()
                                            except Exception as e:
                                                print(f"khong popup quangcao: {e}")
                                                try:
                                                    browser.implicitly_wait(5)
                                                    close = browser.find_element(By.XPATH,
                                                                                 read_xpath.CloseAdPopupEn).click()
                                                except Exception as e:
                                                    print(f"khong popup quangcao: {e}")
                                            # Suspend 1 hours, do other thing before break
                                            # Do any else
                                            interval_minutes = 5
                                            ack_suspension_hours = 1
                                            suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                            interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                            # Wait for the specified interval and check if 2 hours have passed
                                            elapsed_time = 0
                                            while elapsed_time < suspension_duration:
                                                print("Checking after every {} minutes...".format(interval_minutes))
                                                time.sleep(interval_duration)
                                                elapsed_time += interval_duration
                                        except Exception as e:
                                            print(f"No Restrict: {e}")
                                except Exception as e:
                                    print(e)
                                    print("chuaReply")
                                    break

                                sleep(randint(2, 3))
                        except Exception as ex:
                            print(ex)
                            print('notpasssssssssx')
                            break
            ez+=1

def autoComment(browser): #Hàm comment trong group đã Join
    # Duyệt tất cả các nhóm
    wait4 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
    clickGroup = wait4.until(EC.element_to_be_clickable((By.XPATH, read_xpath.GroupsTab)))
    clickGroup.click()
    sleep(5)
    wait5 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
    clickGroup = wait5.until(
        EC.element_to_be_clickable((By.XPATH, read_xpath.JoinedGroups)))
    clickGroup.click()
    sleep(5)
    # Cuộn xuống tìm tất cả thẻ
    try:
        print('access to scrollbar1')
        i = 0
        while i < 10:
            # Cuộn xuống
            browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            # Chờ một chút để trang cuộn xuống
            print("xuống cuối1")
            sleep(2)
            i += 1
    except:
        print('cannot access to scrollbar1')

    # Lấy tất cả các nhóm
    print("div to 1")
    wait = WebDriverWait(browser, 10)
    elementTo = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, read_xpath.GroupList)))
    print("div to 1 into")
    browser.implicitly_wait(10)
    element = elementTo.find_elements(By.XPATH, read_xpath.GroupLinks)
    print(f"Tong so link: {len(element)}")
    for i in element:
        href = i.get_attribute("href")
        print(f"ban oi: {href}")
    # Duyệt từng nhóm.
    ez = 0
    sleep(randint(5, 7))
    for i in element:
        if ez > 2:
            try:
                href = i.get_attribute("href")
                print(f"ban oi: {href}")
                # click từng link vào nhóm
                wait6 = WebDriverWait(i, 30)  # Maximum wait time of 10 seconds
                eachGroup = wait6.until(
                    EC.element_to_be_clickable((By.XPATH, read_xpath.ClickGroup)))
                eachGroup.click()
                print('passsssssss1x')

                # Check popup "Rời khỏi Trang"
                try:
                    browser.implicitly_wait(5)
                    close = browser.find_element(By.XPATH,
                                                    read_xpath.LeavePagePopupVi).click()
                except:
                    try:
                        browser.implicitly_wait(5)
                        close = browser.find_element(By.XPATH,
                                                        read_xpath.LeavePagePopupEn).click()
                    except:
                        print("khong popup leavepage")

                # dosomethings
                sleep(randint(5, 10))
                # Check popup "Quảng cáo"
                try:
                    browser.implicitly_wait(5)
                    close = browser.find_element(By.XPATH,
                                                    read_xpath.CloseAdPopupVi).click()
                except:
                    try:
                        browser.implicitly_wait(5)
                        close = browser.find_element(By.XPATH,
                                                        read_xpath.CloseAdPopupEn).click()
                    except:
                        print("khong popup quangcao")
                # nếu đến link thứ 3 thì bắt đầu click truy cập vào nhóm
                print("Toidayroi")
                # phải sleep
                sleep(randint(3, 5))
                # Tìm GroupFeed chứa tất cả các bài Post
                try:
                    wait7 = WebDriverWait(i, 10)
                    GroupFeed = wait7.until(
                        EC.visibility_of_element_located
                        ((By.XPATH, read_xpath.GroupFeed)))
                except:
                    wait7 = WebDriverWait(i, 10)
                    GroupFeed = wait7.until(
                        EC.visibility_of_element_located
                        ((By.XPATH, read_xpath.GroupPreview)))
                print('passsssssss1x')
                # Lướt xuống để bot thấy được lượng bài post nhất định
                # Tạo đối tượng ActionChains
                actions = ActionChains(browser)
                # Cuộn trang web xuống
                actions.send_keys(Keys.PAGE_DOWN).perform()
                actions.send_keys(Keys.PAGE_DOWN).perform()
                actions.send_keys(Keys.PAGE_DOWN).perform()
                sleep(5)
                wait9 = WebDriverWait(GroupFeed, 10)
                feedx = wait9.until(
                    EC.presence_of_all_elements_located
                    ((By.XPATH, read_xpath.PostsContainer)))
                print('passsssssss1x')
                print(f'thuc su co may: {len(feedx)}')
                izzz = 1
                for i in feedx:
                    print(izzz)
                    if izzz == 3:
                        break
                    print(f'thuc su co may: {i.text}')
                    try:
                        sleep(randint(5, 6))
                        browser.execute_script("arguments[0].scrollIntoView({block: 'end'});", i)
                        browser.implicitly_wait(10)
                        commentDe0 = i.find_element(By.XPATH, read_xpath.CommentButton)
                        browser.execute_script("arguments[0].click();", commentDe0)
                        browser.implicitly_wait(10)
                        commentDe = i.find_element(By.XPATH, read_xpath.CommentBox)
                        commentDe.send_keys(Comment)
                        sleep(randint(5, 6))
                        commentDe.send_keys(Keys.RETURN)
                        print("Dacomment")
                        sleep(randint(12, 15))
                        with open("logGroupComment.txt", "a") as file:
                            file.write(f"So like: {izzz} \nLink: {href}")
                        izzz += 1
                        # Lấy Xpath Restricted POST
                        try:
                            browser.implicitly_wait(5)
                            restricted = browser.find_element(By.XPATH, read_xpath.RestrictedPost)
                            print("Restricted")
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                                read_xpath.CloseAdPopupVi).click()
                            except:
                                try:
                                    browser.implicitly_wait(5)
                                    close = browser.find_element(By.XPATH,
                                                                    read_xpath.CloseAdPopupEn).click()
                                except:
                                    print("khong popup quangcao")
                                # Suspend 1 hours, do other thing before break

                                # Do any else
                                interval_minutes = 5
                                ack_suspension_hours = 1
                                suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                # Wait for the specified interval and check if 2 hours have passed
                                elapsed_time = 0
                                while elapsed_time < suspension_duration:
                                    print("Checking after every {} minutes...".format(interval_minutes))
                                    time.sleep(interval_duration)
                                    elapsed_time += interval_duration
                                # Break
                        except:
                            try:
                                browser.implicitly_wait(5)
                                restricted = browser.find_element(By.XPATH,
                                                                    read_xpath.RestrictedAll)
                                print("Restricted All")
                                try:
                                    browser.implicitly_wait(5)
                                    close = browser.find_element(By.XPATH,
                                                                    read_xpath.CloseAdPopupVi).click()
                                except Exception as e:
                                    print(f"khong popup quang cao: {e}")
                                    try:
                                        browser.implicitly_wait(5)
                                        close = browser.find_element(By.XPATH,
                                                                        read_xpath.CloseAdPopupEn).click()
                                    except Exception as e:
                                        print(f"khong popup quang cao: {e}")
                                    # Suspend 1 hours, do other thing before break
                                    # Do any else
                                    interval_minutes = 5
                                    ack_suspension_hours = 1
                                    suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                    interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                    # Wait for the specified interval and check if 2 hours have passed
                                    elapsed_time = 0
                                    while elapsed_time < suspension_duration:
                                        print("Checking after every {} minutes...".format(interval_minutes))
                                        time.sleep(interval_duration)
                                        elapsed_time += interval_duration
                            except Exception as e:
                                print(f"No Restrict: {e}")
                    except Exception as e:
                        print(e)
                        print("chua Comment")
                        break

                    sleep(randint(2, 3))
            except Exception as e:
                try:
                    wait6 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
                    eachGroup = wait6.until(
                        EC.element_to_be_clickable((By.XPATH, read_xpath.ClickGroup)))
                    eachGroup.click()
                    print('passsssssss2x')
                    # dosomething
                    # Check popup "Rời khỏi Trang"
                    try:
                        browser.implicitly_wait(5)
                        close = browser.find_element(By.XPATH, read_xpath.LeavePagePopupVi).click()
                    except:
                        try:
                            browser.implicitly_wait(5)
                            close = browser.find_element(By.XPATH, read_xpath.LeavePagePopupEn).click()
                        except:
                            print("khong popup leave page")

                    # dosomethings
                    sleep(randint(5, 10))
                    # Check popup "Quảng cáo"
                    try:
                        browser.implicitly_wait(5)
                        close = browser.find_element(By.XPATH, read_xpath.CloseAdPopupVi).click()
                    except:
                        try:
                            browser.implicitly_wait(5)
                            close = browser.find_element(By.XPATH, read_xpath.CloseAdPopupEn).click()
                        except:
                            print("khong popup quang cao")
                    # nếu đến link thứ 3 thì bắt đầu click truy cập vào nhóm
                    print("Toidayroi")
                    # phải sleep
                    sleep(randint(3, 5))
                    # Tìm GroupFeed chứa tất cả các bài Post
                    try:
                        wait7 = WebDriverWait(i, 10)
                        GroupFeed = wait7.until(
                            EC.visibility_of_element_located((By.XPATH, read_xpath.GroupFeed)))
                    except:
                        wait7 = WebDriverWait(i, 10)
                        GroupFeed = wait7.until(
                            EC.visibility_of_element_located((By.XPATH, read_xpath.GroupPreview)))
                    print('passsssssss1x')
                    # Lướt xuống để bot thấy được lượng bài post nhất định
                    # Tạo đối tượng ActionChains
                    actions = ActionChains(browser)
                    # Cuộn trang web xuống
                    actions.send_keys(Keys.PAGE_DOWN).perform()
                    actions.send_keys(Keys.PAGE_DOWN).perform()
                    actions.send_keys(Keys.PAGE_DOWN).perform()
                    sleep(5)

                    wait9 = WebDriverWait(GroupFeed, 10)
                    feedx = wait9.until(
                        EC.presence_of_all_elements_located
                        ((By.XPATH, read_xpath.PostsContainer)))
                    print('passsssssss1x')
                    print(f'thuc su co may: {len(feedx)}')
                    izzz = 1
                    for i in feedx:
                        print(f'thuc su co may: {i.text}')
                        if i == 3:
                            break
                        print(f'thuc su co may: {i.text}')
                        try:
                            sleep(randint(5, 6))
                            browser.execute_script("arguments[0].scrollIntoView({block: 'end'});", i)
                            browser.implicitly_wait(10)
                            commentDe = i.find_element(By.XPATH, read_xpath.CommentPublic)
                            commentDe.send_keys(Comment)
                            sleep(randint(5, 6))
                            commentDe.send_keys(Keys.RETURN)
                            print("Dacomment")
                            sleep(randint(12, 15))
                            with open("logGroupComment.txt", "a") as file:
                                file.write(f"So like: {izzz} \nLink: {href}")
                            izzz += 1
                        except Exception as e:
                            print(e)
                            print("chuaComment")
                            sleep(randint(2, 3))
                except:
                    print('notpasssssssssx')
                    break
        ez += 1

def robotLike(browser, groupLink, accountLike):
    try:
        wait7 = WebDriverWait(groupLink, 10)
        GroupFeed = wait7.until(
            EC.visibility_of_element_located
            ((By.XPATH, read_xpath.GroupFeed)))
    except:
        wait7 = WebDriverWait(groupLink, 10)
        GroupFeed = wait7.until(
            EC.visibility_of_element_located
            ((By.XPATH, read_xpath.GroupPreview)))
    print('passsssssss1x')

    # Lướt xuống để bot thấy được lượng bài post nhất định
    # Tạo đối tượng ActionChains
    actions = ActionChains(browser)
    listFeedResult = []
    numberPost = True
    while numberPost:

        # Cuộn trang web xuống
        actions.send_keys(Keys.PAGE_DOWN).perform()
        sleep(5)

        wait9 = WebDriverWait(GroupFeed, 10)
        listFeed = wait9.until(
            EC.presence_of_all_elements_located
            ((By.XPATH, read_xpath.PostsContainer)))
        print('passsssssss1x')
        print(f'thuc su co may: {len(listFeed)}')
        #Cuộn đến bài đăng cuối
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", listFeed[len(listFeed)-1])

        if len(listFeed)-5>=0:
            try:

                browser.implicitly_wait(5)
                likeDe = listFeed[len(listFeed)-1].find_element(By.XPATH, '//*[@class="xq8finb x16n37ib"]')
                browser.implicitly_wait(5)
                unlike = likeDe.find_element(By.XPATH, '//div[@aria-label="Gỡ Thích" and @role="button"]')

                #browser.execute_script("arguments[0].click();", likeDe)
                print("Cuộn tiếp")
            except:
                try:
                    browser.implicitly_wait(5)
                    likeDe2 = listFeed[len(listFeed) - 1].find_element(By.XPATH, '//*[@class="xq8finb x16n37ib"]')
                    browser.implicitly_wait(5)
                    unlike = likeDe2.find_element(By.XPATH, '//div[@aria-label="Remove Like" and @role="button"]')
                    #browser.execute_script("arguments[0].click();", likeDe)
                    print("Cuộn tiếp")
                except:
                    try:
                        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});",
                                               listFeed[len(listFeed) - 5])
                        browser.implicitly_wait(5)
                        likeDe = listFeed[len(listFeed) - 1].find_element(By.XPATH, '//*[@class="xq8finb x16n37ib"]')
                        browser.implicitly_wait(5)
                        unlike = likeDe.find_element(By.XPATH, '//div[@aria-label="Thích" and @role="button"]')
                        #List có bài like và tối thiểu 5 bài chưa like
                        for feed in listFeed:
                            try:
                                browser.implicitly_wait(5)
                                likeDe = listFeed[len(listFeed) - 1].find_element(By.XPATH,
                                                                                  '//*[@class="xq8finb x16n37ib"]')
                                browser.implicitly_wait(5)
                                unlike = likeDe.find_element(By.XPATH,
                                                             '//div[@aria-label="Thích" and @role="button"]')
                                listFeedResult.append(feed)
                                if len(listFeedResult) ==5:
                                    numberPost = False
                                    break
                            except:
                                pass
                    except:
                        print("Cuộn tiếp")
    demLike = 1

    for like in listFeedResult:
        sleep(5)
        # Cuộn đến bài đăng cuối
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", like)
        browser.implicitly_wait(5)
        likeDe3 = like.find_element(By.XPATH, '//*[@class="xq8finb x16n37ib"]')
        browser.implicitly_wait(5)
        clickLike = likeDe3.find_element(By.XPATH, '//div[@aria-label="Thích" and @role="button"]')

        browser.execute_script("arguments[0].click();", clickLike)
        print(f"Dalike: {demLike}/5")
        demLike+=1
        # Lấy thời gian hiện tại
        current_datetime = datetime.now()
        with lock:
            try:
                log_save_database = Log_FacebookBot(accountLike, current_datetime,"Content",
                                                    "Like",
                                                    "No", groupLink.get_attribute("href"))
                log_save_database.saveDB()
            except Exception as e:
                print(f"Exception: {e}")

def autoLike(browser):
    # Duyệt tất cả các nhóm
    wait4 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
    clickGroup = wait4.until(EC.element_to_be_clickable((By.XPATH, read_xpath.GroupsTab)))
    clickGroup.click()
    sleep(5)
    wait5 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
    clickGroup = wait5.until(
        EC.element_to_be_clickable((By.XPATH, read_xpath.JoinedGroups)))
    clickGroup.click()
    sleep(5)
    # Cuộn xuống tìm tất cả thẻ
    try:
        print('access to scrollbar1')
        i = 0
        while i < 10:
            # Cuộn xuống
            browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            # Chờ một chút để trang cuộn xuống
            print("xuống cuối1")
            sleep(2)
            i += 1
    except:
        print('cannot access to scrollbar1')

    # Lấy tất cả các nhóm
    print("div to 1")
    wait = WebDriverWait(browser, 10)
    elementTo = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, read_xpath.GroupList)))
    print("div to 1 into")
    browser.implicitly_wait(10)
    element = elementTo.find_elements(By.XPATH, read_xpath.GroupLinks)
    print(f"Tong so link: {len(element)}")
    for i in element:
        href = i.get_attribute("href")
        print(f"ban oi: {href}")
    # Duyệt từng nhóm.
    ez = 0
    sleep(randint(5, 7))
    for i in element:
        if ez >2:
            try:
                    href = i.get_attribute("href")
                    print(f"ban oi: {href}")
                    # click từng link vào nhóm
                    wait6 = WebDriverWait(i, 30)  # Maximum wait time of 10 seconds
                    eachGroup = wait6.until(
                            EC.element_to_be_clickable((By.XPATH, read_xpath.ClickGroup)))
                    eachGroup.click()
                    print('passsssssss1x')

                    # Check popup "Rời khỏi Trang"
                    try:
                        browser.implicitly_wait(5)
                        close = browser.find_element(By.XPATH,
                                                    read_xpath.LeavePagePopupVi).click()
                    except:
                        try:
                            browser.implicitly_wait(5)
                            close = browser.find_element(By.XPATH,
                                                        read_xpath.LeavePagePopupEn).click()
                        except:
                            print("khong popup leavepage")

                    # dosomethings
                    sleep(randint(5, 10))
                    # Check popup "Quảng cáo"
                    try:
                        browser.implicitly_wait(5)
                        close = browser.find_element(By.XPATH,
                                                    read_xpath.CloseAdPopupVi).click()
                    except:
                        try:
                            browser.implicitly_wait(5)
                            close = browser.find_element(By.XPATH,
                                                        read_xpath.CloseAdPopupEn).click()
                        except:
                            print("khong popup quangcao")
                    # nếu đến link thứ 3 thì bắt đầu click truy cập vào nhóm
                    print("Toidayroi")
                    # phải sleep
                    sleep(randint(3, 5))
                    # Tìm GroupFeed chứa tất cả các bài Post
                    try:
                        wait7 = WebDriverWait(i, 10)
                        GroupFeed = wait7.until(
                            EC.visibility_of_element_located
                            ((By.XPATH, read_xpath.GroupFeed)))
                    except:
                        wait7 = WebDriverWait(i, 10)
                        GroupFeed = wait7.until(
                            EC.visibility_of_element_located
                            ((By.XPATH, read_xpath.GroupPreview)))
                    print('passsssssss1x')
                    # Lướt xuống để bot thấy được lượng bài post nhất định
                    # Tạo đối tượng ActionChains
                    actions = ActionChains(browser)
                    # Cuộn trang web xuống
                    actions.send_keys(Keys.PAGE_DOWN).perform()
                    sleep(1)
                    actions.send_keys(Keys.PAGE_DOWN).perform()
                    sleep(1)
                    actions.send_keys(Keys.PAGE_DOWN).perform()
                    sleep(5)

                    wait9 = WebDriverWait(GroupFeed, 10)
                    feedx = wait9.until(
                        EC.presence_of_all_elements_located
                        ((By.XPATH, read_xpath.PostsContainer)))
                    print('passsssssss1x')
                    print(f'thuc su co may: {len(feedx)}')
                    izzz =1
                    for i in feedx:
                        print(f'thuc su co may: {i.text}')
                        try:
                            sleep(randint(5, 6))
                            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", i)

                            try:
                                browser.implicitly_wait(5)
                                likeDe = i.find_element(By.XPATH, read_xpath.LikeButton)
                                browser.execute_script("arguments[0].click();", likeDe)
                                print("Dalike1")

                            except:
                                browser.implicitly_wait(5)
                                likeDe = i.find_element(By.XPATH, read_xpath.LikeButton)
                                browser.execute_script("arguments[0].click();", likeDe)
                                print("Dalike2")


                            with open("logGroupLike.txt", "a") as file:
                                file.write(f"So like: {izzz} \nLink: {href}")
                            izzz+=1

                            # Lấy Xpath Restricted POST
                            try:
                                browser.implicitly_wait(5)
                                restricted = browser.find_element(By.XPATH, read_xpath.RestrictedPost)
                                print("Restricted")

                                try:
                                    browser.implicitly_wait(5)
                                    close = browser.find_element(By.XPATH,
                                                                read_xpath.CloseAdPopupVi).click()
                                except:
                                    try:
                                        browser.implicitly_wait(5)
                                        close = browser.find_element(By.XPATH,
                                                                        read_xpath.CloseAdPopupEn).click()
                                    except:
                                        print("khong popup quangcao")
                                # Suspend 1 hours, do other thing before break
                                # Do any else
                                interval_minutes = 5
                                ack_suspension_hours = 1
                                suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                # Wait for the specified interval and check if 2 hours have passed
                                elapsed_time = 0
                                while elapsed_time < suspension_duration:
                                    print("Checking after every {} minutes...".format(interval_minutes))
                                    time.sleep(interval_duration)
                                    elapsed_time += interval_duration
                                # Break
                            except:
                                try:
                                    browser.implicitly_wait(5)
                                    restricted = browser.find_element(By.XPATH,
                                                                        read_xpath.RestrictedAll)
                                    print("Restricted All")
                                    try:
                                        browser.implicitly_wait(5)
                                        close = browser.find_element(By.XPATH,
                                                                    read_xpath.CloseAdPopupVi).click()
                                    except Exception as e:
                                        print(f"khong popup quangcao: {e}")
                                        try:
                                            browser.implicitly_wait(5)
                                            close = browser.find_element(By.XPATH,
                                                                            read_xpath.CloseAdPopupEn).click()
                                        except Exception as e:
                                            print(f"khong popup quangcao: {e}")
                                    # Suspend 1 hours, do other thing before break
                                    # Do any else
                                    interval_minutes = 5
                                    ack_suspension_hours = 1
                                    suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                    interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                    # Wait for the specified interval and check if 2 hours have passed
                                    elapsed_time = 0
                                    while elapsed_time < suspension_duration:
                                        print("Checking after every {} minutes...".format(interval_minutes))
                                        time.sleep(interval_duration)
                                        elapsed_time += interval_duration
                                except Exception as e:
                                    print(f"No Restrict: {e}")
                        except Exception as e:
                            print(e)
                            print("chuaLike")
                            break

                        sleep(randint(2, 3))
            except Exception as e:
                    try:
                        wait6 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
                        eachGroup = wait6.until(
                            EC.element_to_be_clickable((By.XPATH, read_xpath.ClickGroup)))
                        eachGroup.click()
                        print('passsssssss2x')
                        # dosomething
                        # Check popup "Rời khỏi Trang"
                        try:
                            browser.implicitly_wait(5)
                            close = browser.find_element(By.XPATH,
                                                        read_xpath.LeavePagePopupVi).click()
                        except:
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            read_xpath.LeavePagePopupEn).click()
                            except:
                                print("khong popup leavepage")

                        # dosomethings
                        sleep(randint(5, 10))
                        # Check popup "Quảng cáo"
                        try:
                            browser.implicitly_wait(5)
                            close = browser.find_element(By.XPATH,
                                                        f"read_xpath.CloseAdPopupVi").click()
                        except:
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            read_xpath.CloseAdPopupEn).click()
                            except:
                                print("khong popup quangcao")
                        # nếu đến link thứ 3 thì bắt đầu click truy cập vào nhóm
                        print("Toidayroi")
                        # phải sleep
                        sleep(randint(3, 5))
                        # Tìm GroupFeed chứa tất cả các bài Post
                        try:
                            wait7 = WebDriverWait(i, 10)
                            GroupFeed = wait7.until(
                                EC.visibility_of_element_located
                                ((By.XPATH, read_xpath.GroupFeed)))
                        except:
                            wait7 = WebDriverWait(i, 10)
                            GroupFeed = wait7.until(
                                EC.visibility_of_element_located
                                ((By.XPATH, read_xpath.GroupPreview)))
                        print('passsssssss1x')
                        # Lướt xuống để bot thấy được lượng bài post nhất định
                                                # Tạo đối tượng ActionChains
                        actions = ActionChains(browser)
                        # Cuộn trang web xuống
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        sleep(5)
                        wait9 = WebDriverWait(GroupFeed, 10)
                        feedx = wait9.until(
                            EC.presence_of_all_elements_located
                            ((By.XPATH, read_xpath.PostsContainer)))
                        print('passsssssss1x')
                        print(f'thuc su co may: {len(feedx)}')
                        for i in feedx:
                            print(f'thuc su co may: {i.text}')
                            try:
                                browser.execute_script("arguments[0].scrollIntoView({block: 'end'});", i)
                                sleep(randint(5, 6))
                                browser.implicitly_wait(10)
                                likeDe = i.find_element(By.XPATH,'//div[@aria-label="Thích" and @role="button"]')
                                browser.execute_script("arguments[0].click();", likeDe)
                                print("Dalike")
                            except Exception as e:
                                print(e)
                                print("chuaLike")
                                break
                            sleep(randint(2, 3))
                    except:
                        print('notpasssssssssx')
                        break
        ez+=1

def autoShare(browser):
        # Duyệt tất cả các nhóm
        wait4 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
        clickGroup = wait4.until(EC.element_to_be_clickable((By.XPATH, read_xpath.GroupsTab)))
        clickGroup.click()
        sleep(5)
        wait5 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
        clickGroup = wait5.until(
            EC.element_to_be_clickable((By.XPATH, read_xpath.JoinedGroups)))
        clickGroup.click()
        sleep(5)
        # Cuộn xuống tìm tất cả thẻ
        try:
            print('access to scrollbar1')
            i = 0
            while i < 10:
                # Cuộn xuống
                browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                # Chờ một chút để trang cuộn xuống
                print("xuống cuối1")
                sleep(2)
                i += 1
        except:
            print('cannot access to scrollbar1')

        # Lấy tất cả các nhóm
        print("div to 1")
        wait = WebDriverWait(browser, 10)
        elementTo = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, read_xpath.GroupList)))
        print("div to 1 into")
        browser.implicitly_wait(10)
        element = elementTo.find_elements(By.XPATH, read_xpath.GroupLinks)
        print(f"Tong so link: {len(element)}")
        for i in element:
            href = i.get_attribute("href")
            print(f"ban oi: {href}")
        # Duyệt từng nhóm.
        ez = 0
        sleep(randint(5, 7))
        for i in element:
            if ez >2:
                try:
                        href = i.get_attribute("href")
                        print(f"ban oi: {href}")
                        # click từng link vào nhóm
                        wait6 = WebDriverWait(i, 30)  # Maximum wait time of 10 seconds
                        eachGroup = wait6.until(
                                EC.element_to_be_clickable((By.XPATH, read_xpath.ClickGroup)))
                        eachGroup.click()
                        print('passsssssss1x')

                        # Check popup "Rời khỏi Trang"
                        try:
                            browser.implicitly_wait(5)
                            close = browser.find_element(By.XPATH,
                                                        read_xpath.LeavePagePopupVi).click()
                        except:
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            read_xpath.LeavePagePopupEn).click()
                            except:
                                print("khong popup leavepage")

                        # dosomethings
                        sleep(randint(5, 10))
                        # Check popup "Quảng cáo"
                        try:
                            browser.implicitly_wait(5)
                            close = browser.find_element(By.XPATH,
                                                        f"read_xpath.CloseAdPopupVi").click()
                        except:
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            read_xpath.CloseAdPopupEn).click()
                            except:
                                print("khong popup quangcao")
                        # nếu đến link thứ 3 thì bắt đầu click truy cập vào nhóm
                        print("Toidayroi")
                        # phải sleep
                        sleep(randint(3, 5))
                        # Tìm GroupFeed chứa tất cả các bài Post
                        try:
                            wait7 = WebDriverWait(i, 10)
                            GroupFeed = wait7.until(
                                EC.visibility_of_element_located
                                ((By.XPATH, read_xpath.GroupFeed)))
                        except:
                            wait7 = WebDriverWait(i, 10)
                            GroupFeed = wait7.until(
                                EC.visibility_of_element_located
                                ((By.XPATH, read_xpath.GroupPreview)))
                        print('passsssssss1x')
                        # Lướt xuống để bot thấy được lượng bài post nhất định
                        # Tạo đối tượng ActionChains
                        actions = ActionChains(browser)
                        # Cuộn trang web xuống
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        sleep(5)

                        wait9 = WebDriverWait(GroupFeed, 10)
                        feedx = wait9.until(
                            EC.presence_of_all_elements_located
                            ((By.XPATH, read_xpath.PostsContainer)))
                        print('passsssssss1x')
                        print(f'thuc su co may: {len(feedx)}')
                        izzz=1
                        for i in feedx:
                            print(f'thuc su co may: {i.text}')
                            if izzz == 3:
                                break
                            try:
                                sleep(randint(5, 6))
                                browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", i)
                                browser.implicitly_wait(10)
                                shareDe = i.find_element(By.XPATH,'//div[@aria-label="Gửi nội dung này cho bạn bè hoặc đăng lên trang cá nhân của bạn." and @role="button"]')
                                browser.execute_script("arguments[0].click();", shareDe)
                                sleep(randint(2, 4))
                                print("DaClickShare")
                                browser.implicitly_wait(10)
                                shareNhomDe = i.find_element(By.XPATH,'//span[text()="Chia sẻ ngay"]')
                                browser.execute_script("arguments[0].click();", shareNhomDe)
                                print("DaClickShareNhom")
                                sleep(randint(2, 4))
                                
                                """
                                    browser.implicitly_wait(10)
                                    share1NhomDe = i.find_elements(By.XPATH,"//div[@role='listitem']")
                                    print(f"Nhom nay có:{len(share1NhomDe)}")
                                    share1NhomDe[1].click()
                                    print("DaClick1Nhom")
                                    sleep(randint(2, 4))
                                """
                                try:
                                            # Nhấn vào nút "Chia sẻ" trên bài viết vừa đăng
                                            sleep(randint(5, 6))
                                            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", i)
                                            browser.implicitly_wait(10)
                                            shareDe = i.find_element(By.XPATH,'//div[@aria-label="Gửi nội dung này cho bạn bè hoặc đăng lên trang cá nhân của bạn." and @role="button"]')
                                            browser.execute_script("arguments[0].click();", shareDe)
                                            sleep(randint(2, 4))
                                            print("DaClickShare")

                                            # Chọn "Chia sẻ vào nhóm"
                                            share_in_group = WebDriverWait(browser, 10).until(
                                                EC.element_to_be_clickable((By.XPATH, "//span[text()='Nhóm']"))
                                            )
                                            share_in_group.click()
                                            sleep(randint(3, 5))

                                            # Lấy danh sách nhóm có thể share
                                            group_elements = WebDriverWait(browser, 10).until(
                                                EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listitem']"))
                                            )

                                            print(f"Tìm thấy {len(group_elements)} nhóm, bắt đầu chia sẻ...")

                                            for group in group_elements:
                                                try:
                                                    group = browser.find_element(By.XPATH, "//*[@id='mount_0_0_xg']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/div/div")
                                                    group.click()

                                                    # Nếu tìm thấy phần tử
                                                    if group_elements:
                                                        group = group_elements[0]  # Lấy nhóm đầu tiên

                                                        # Cuộn vào tầm nhìn
                                                        browser.execute_script("arguments[0].scrollIntoView(true);", group)
                                                        sleep(2)  # Đợi trang cập nhật

                                                        # Dùng ActionChains để click
                                                        actions = ActionChains(browser)
                                                        actions.move_to_element(group).click().perform()
                                                        sleep(2)
                                                    else:
                                                        print("Không tìm thấy nhóm!")

                                                    # Nhấn nút "Đăng" để chia sẻ bài viết vào nhóm
                                                    print("Đang tìm nút 'Đăng'")
                                                    post_button = WebDriverWait(browser, 10).until(
                                                        EC.element_to_be_clickable((By.XPATH, read_xpath.PostButton))
                                                    )
                                                    print("Đang nhấp vào nút 'Đăng'")
                                                    post_button.click()
                                                    print("Đã chia sẻ vào một nhóm")

                                                    sleep(randint(5, 10))  # Tránh bị Facebook block

                                                    # Nhấn nút quay lại danh sách nhóm để tiếp tục chia sẻ
                                                    print("Đang tìm nút 'Quay lại'")
                                                    back_button = WebDriverWait(browser, 5).until(
                                                        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Quay lại']"))
                                                    )
                                                    print("Đang nhấp vào nút 'Quay lại'")
                                                    back_button.click()
                                                    sleep(randint(3, 5))  # Tránh bị Facebook block lại

                                                except Exception as e:
                                                    print(f"Lỗi khi chia sẻ vào nhóm: {e}")

                                except Exception as e:
                                            print(f"Lỗi trong quá trình chia sẻ: {e}")
                                
                                try:
                                    browser.implicitly_wait(5)
                                    restricted = browser.find_element(By.XPATH, read_xpath.RestrictedPost)
                                    print("Restricted")

                                    try:
                                        browser.implicitly_wait(5)
                                        close = browser.find_element(By.XPATH,
                                                                     f"read_xpath.CloseAdPopupVi").click()
                                    except:
                                        try:
                                            browser.implicitly_wait(5)
                                            close = browser.find_element(By.XPATH,
                                                                         read_xpath.CloseAdPopupEn).click()
                                        except:
                                            print("khong popup quangcao")
                                    # Suspend 1 hours, do other thing before break
                                    # Do any else
                                    interval_minutes = 5
                                    ack_suspension_hours = 1
                                    suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                    interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                    # Wait for the specified interval and check if 2 hours have passed
                                    elapsed_time = 0
                                    while elapsed_time < suspension_duration:
                                        print("Checking after every {} minutes...".format(interval_minutes))
                                        time.sleep(interval_duration)
                                        elapsed_time += interval_duration
                                    # Break
                                except:
                                    try:
                                        browser.implicitly_wait(5)
                                        restricted_elements = browser.find_elements(By.XPATH, read_xpath.RestrictedAll)
                                        if restricted_elements:
                                            restricted = restricted_elements[0]
                                            print("Restricted All")
                                            try:
                                                browser.implicitly_wait(5)
                                                close = browser.find_element(By.XPATH, f"read_xpath.CloseAdPopupVi").click()
                                            except Exception as e:
                                                print(f"khong popup quangcao: {e}")
                                                try:
                                                    browser.implicitly_wait(5)
                                                    close = browser.find_element(By.XPATH, read_xpath.CloseAdPopupEn).click()
                                                except Exception as e:
                                                    print(f"khong popup quangcao: {e}")
                                            # Suspend 1 hours, do other thing before break
                                            interval_minutes = 5
                                            ack_suspension_hours = 1
                                            suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                            interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                            elapsed_time = 0
                                            while elapsed_time < suspension_duration:
                                                print("Checking after every {} minutes...".format(interval_minutes))
                                                time.sleep(interval_duration)
                                                elapsed_time += interval_duration
                                        else:
                                            print("No Restrict: Element not found")
                                    except Exception as e:
                                        print(f"No Restrict: {e}")
                            except Exception as e:
                                print(e)
                                print("chuaShare")
                                break
                            sleep(randint(2, 3))
                except Exception as e:
                        try:
                            wait6 = WebDriverWait(i, 10)  # Maximum wait time of 10 seconds
                            eachGroup = wait6.until(
                                EC.element_to_be_clickable((By.XPATH, read_xpath.ClickGroup)))
                            eachGroup.click()
                            print('passsssssss2x')
                            # dosomething
                            # Check popup "Rời khỏi Trang"
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            read_xpath.LeavePagePopupVi).click()
                            except:
                                try:
                                    browser.implicitly_wait(5)
                                    close = browser.find_element(By.XPATH,
                                                                read_xpath.LeavePagePopupEn).click()
                                except:
                                    print("khong popup leavepage")

                            # dosomethings
                            sleep(randint(5, 10))
                            # Check popup "Quảng cáo"
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            read_xpath.CloseAdPopupVi).click()
                            except:
                                try:
                                    browser.implicitly_wait(5)
                                    close = browser.find_element(By.XPATH,
                                                                read_xpath.CloseAdPopupEn).click()
                                except:
                                    print("khong popup quangcao")
                            # nếu đến link thứ 3 thì bắt đầu click truy cập vào nhóm
                            print("Toidayroi")
                            # phải sleep
                            sleep(randint(3, 5))
                            # Tìm GroupFeed chứa tất cả các bài Post
                            try:
                                wait7 = WebDriverWait(i, 10)
                                GroupFeed = wait7.until(
                                    EC.visibility_of_element_located
                                    ((By.XPATH, read_xpath.GroupFeed)))
                            except:
                                wait7 = WebDriverWait(i, 10)
                                GroupFeed = wait7.until(
                                    EC.visibility_of_element_located
                                    ((By.XPATH, read_xpath.GroupPreview)))
                            print('passsssssss1x')
                            # Lướt xuống để bot thấy được lượng bài post nhất định
                            # Tạo đối tượng ActionChains
                            actions = ActionChains(browser)
                            # Cuộn trang web xuống
                            actions.send_keys(Keys.PAGE_DOWN).perform()
                            actions.send_keys(Keys.PAGE_DOWN).perform()
                            actions.send_keys(Keys.PAGE_DOWN).perform()
                            sleep(5)

                            wait9 = WebDriverWait(GroupFeed, 10)
                            feedx = wait9.until(
                                EC.presence_of_all_elements_located
                                ((By.XPATH, read_xpath.PostsContainer)))
                            print('passsssssss1x')
                            print(f'thuc su co may: {len(feedx)}')
                            izzz=1
                            for i in feedx:
                                print(f'thuc su co may: {i.text}')
                                if izzz == 3:
                                    break
                        except:
                            print('notpasssssssssx')
                            break
            ez+=1

def post2(browser, account, postContent):
        # Duyệt tất cả các nhóm
        wait4 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
        clickGroup = wait4.until(EC.element_to_be_clickable((By.XPATH, read_xpath.GroupsTab)))
        clickGroup.click()
        print('passs')
        sleep(5)
        wait5 = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
        clickGroup = wait5.until(
            EC.element_to_be_clickable((By.XPATH, read_xpath.JoinedGroups)))
        clickGroup.click()
        sleep(5)
        # Cuộn xuống tìm tất cả thẻ
        try:
            print('access to scrollbar1')
            i = 0
            while i < 10:
                # Cuộn xuống
                browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                # Chờ một chút để trang cuộn xuống
                print("xuống cuối1")
                sleep(2)
                i += 1
        except:
            print('cannot access to scrollbar1')

        # Lấy tất cả các nhóm
        print("div to 1")
        wait = WebDriverWait(browser, 10)
        elementTo = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, read_xpath.GroupList)))
        print("div to 1 into")
        browser.implicitly_wait(10)
        element = elementTo.find_elements(By.XPATH, read_xpath.GroupLinks)
        print(f"Tong so link: {len(element)}")
        for i in element:
            href = i.get_attribute("href")
            print(f"ban oi: {href}")
        # Duyệt từng nhóm.
        ez = 0
        sleep(randint(5, 7))
        for i in range(ez,len(element)):
            if ez >2:
                try:
                        href = element[i].get_attribute("href")
                        print(f"ban oi: {href}")
                        if openFile(href):
                            # click từng link vào nhóm
                            wait6 = WebDriverWait(element[i], 30)  # Maximum wait time of 10 seconds
                            eachGroup = wait6.until(
                                    EC.element_to_be_clickable((By.XPATH, read_xpath.ClickGroup)))
                            eachGroup.click()
                            print('passsssssss1x')

                            # Check popup "Rời khỏi Trang"
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            read_xpath.LeavePagePopupVi).click()
                            except:
                                try:
                                    browser.implicitly_wait(5)
                                    close = browser.find_element(By.XPATH,
                                                                read_xpath.LeavePagePopupEn).click()
                                except:
                                    print("khong popup leavepage")
                            # dosomethings
                            sleep(randint(5, 7))
                            # Check popup "Quảng cáo"
                            try:
                                browser.implicitly_wait(5)
                                close = browser.find_element(By.XPATH,
                                                            f"read_xpath.CloseAdPopupVi").click()
                            except:
                                try:
                                    browser.implicitly_wait(5)
                                    close = browser.find_element(By.XPATH,
                                                                read_xpath.CloseAdPopupEn).click()
                                except:
                                    print("khong popup quangcao")
                                # nếu đến link thứ 3 thì bắt đầu click truy cập vào nhóm
                            try:
                                    try:
                                        #dosomethings
                                        # Cuộn trang web xuống
                                        browser.implicitly_wait(60)
                                        post = browser.find_element(By.XPATH, '//span[contains(text(), "Bạn viết gì đi...")]').click()
                                        sleep(randint(10, 15))
                                        sendText = WebDriverWait(browser, 60)
                                        #'<div class="_1p1v " id="placeholder-4mtoc" style="white-space: pre-wrap;">Tạo bài viết công khai...</div>'
                                        # Đợi phần tử hiển thị và gán nó vào biến
                                        post_content = sendText.until(EC.visibility_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')))

                                        # Sử dụng phương thức send_keys để gửi văn bản
                                        post_content.send_keys(postContent)
                                        print("Da sendkeys")
                                        sleep(randint(10, 15))
                                        wPost = WebDriverWait(browser, 60)  # Maximum wait time of 10 seconds
                                        Post = wPost.until(EC.element_to_be_clickable(
                                            (By.XPATH, '//span[text()="Đăng"]')))
                                        Post.click()
                                        print("Da nhan post")
                                        sleep(randint(5, 7))
                                    except Exception as e:
                                        print(f"Error with {e}")

                                    #Lấy Xpath Restricted POST
                                    try:
                                        browser.implicitly_wait(10)
                                        restricted = browser.find_element(By.XPATH, read_xpath.RestrictedPost)
                                        print("Restricted")
                                        # Lấy thời gian hiện tại
                                        current_datetime = datetime.now()
                                        with lock:
                                            try:
                                                log_save_database = Log_FacebookBot(account, current_datetime,"Content",
                                                                                    "POST",
                                                                                    "No", href)
                                                log_save_database.saveDB()
                                            except Exception as e:
                                                print(f"Exception: {e}")


                                        #Tắt popup Restrict
                                        try:
                                            browser.implicitly_wait(5)
                                            close = browser.find_element(By.XPATH,
                                                                         f"read_xpath.CloseAdPopupVi").click()
                                        except:
                                            try:
                                                browser.implicitly_wait(5)
                                                close = browser.find_element(By.XPATH,
                                                                             read_xpath.CloseAdPopupEn).click()
                                            except:
                                                print("khong popup restrict")
                                        # Do any else
                                        #Suspend 1 hours, do other thing before break
                                        interval_minutes = 5
                                        ack_suspension_hours = 1
                                        suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                        interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                        # Wait for the specified interval and check if 2 hours have passed
                                        elapsed_time = 0
                                        while elapsed_time < suspension_duration:
                                            #Like/comment/share 5 nhóm, 5 bài/nhóm, nghỉ 5 phút
                                            lcsrandom = randint(3, len(element)-1)

                                            # click từng link vào nhóm
                                            wait6 = WebDriverWait(element[lcsrandom], 30)  # Maximum wait time of 10 seconds
                                            eachGroup = wait6.until(
                                                EC.element_to_be_clickable(
                                                    (By.XPATH, f'(//a[@href="{element[lcsrandom].get_attribute("href")}" and @role="link"])[1]')))
                                            eachGroup.click()
                                            print('passsssssss1x')
                                            #Call like robot
                                            #robotLike(browser,element[lcsrandom], accountLike=account)


                                            print("Checking after every {} minutes...".format(interval_minutes))
                                            time.sleep(interval_duration)
                                            elapsed_time += interval_duration
                                        #Break
                                        ez -= 2

                                    except:
                                        try:
                                            browser.implicitly_wait(5)
                                            restricted = browser.find_element(By.XPATH, read_xpath.RestrictedAll)
                                            print("Restricted All")
                                            # Lấy thời gian hiện tại
                                            current_datetime = datetime.now()
                                            with lock:
                                                try:
                                                    log_save_database = Log_FacebookBot(account, current_datetime,"Content",
                                                                                        "POST",
                                                                                        "No", href)
                                                    log_save_database.saveDB()
                                                except Exception as e:
                                                    print(f"Exception: {e}")
                                            try:
                                                browser.implicitly_wait(5)
                                                close = browser.find_element(By.XPATH,
                                                                             f"read_xpath.CloseAdPopupVi").click()
                                            except Exception as e:
                                                print(f"khong popup quangcao: {e}")
                                                try:
                                                    browser.implicitly_wait(5)
                                                    close = browser.find_element(By.XPATH,
                                                                                 read_xpath.CloseAdPopupEn).click()
                                                except Exception as e:
                                                    print(f"khong popup quangcao: {e}")
                                            # Suspend 1 hours, do other thing before break
                                            # Do any else
                                            interval_minutes = 5
                                            ack_suspension_hours = 1
                                            suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                            interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                            # Wait for the specified interval and check if 2 hours have passed
                                            elapsed_time = 0
                                            while elapsed_time < suspension_duration:
                                                print("Checking after every {} minutes...".format(interval_minutes))
                                                time.sleep(interval_duration)
                                                elapsed_time += interval_duration
                                            ez -= 2
                                        except Exception as e:
                                            print(f"No Restrict: {e}")
                                            print("Da post")

                                    # Lấy thời gian hiện tại
                                    current_datetime = datetime.now()
                                    with lock:
                                        try:
                                            log_save_database = Log_FacebookBot(account, current_datetime,"Content",
                                                                                "POST",
                                                                                "Yes", href)
                                            log_save_database.saveDB()
                                        except Exception as e:
                                            print(f"Exception: {e}")
                            except Exception as e:
                                    print(f"Khong cho member post: {e}")
                            sleep(randint(10, 15))
                except Exception as e:
                        try:
                            href = element[i].get_attribute("href")
                            if openFile(href):
                                wait6 = WebDriverWait(element[i], 10)  # Maximum wait time of 10 seconds
                                eachGroup = wait6.until(
                                    EC.element_to_be_clickable((By.XPATH, read_xpath.ClickGroup)))
                                eachGroup.click()
                                try:
                                    browser.implicitly_wait(5)
                                    close = browser.find_element(By.XPATH,
                                                                read_xpath.LeavePagePopupVi).click()
                                except:
                                    try:
                                        browser.implicitly_wait(5)
                                        close = browser.find_element(By.XPATH,
                                                                    read_xpath.LeavePagePopupEn).click()
                                    except:
                                        print("khong popup leavepage")
                                # dosomethings
                                sleep(randint(5, 7))
                                # Check popup "Quảng cáo"
                                try:
                                    browser.implicitly_wait(5)
                                    close = browser.find_element(By.XPATH,
                                                                f"read_xpath.CloseAdPopupVi").click()
                                except:
                                    try:
                                        browser.implicitly_wait(5)
                                        close = browser.find_element(By.XPATH,
                                                                    read_xpath.CloseAdPopupEn).click()
                                    except:
                                        print("khong popup quangcao")
                                try:
                                    try:
                                        # dosomethings
                                        # Cuộn trang web xuống
                                        browser.implicitly_wait(60)
                                        post = browser.find_element(By.XPATH,
                                                                    '//span[contains(text(), "Bạn viết gì đi...")]').click()
                                        sleep(randint(10, 15))
                                        wsendText = WebDriverWait(browser, 60)
                                        # '<div class="_1p1v " id="placeholder-4mtoc" style="white-space: pre-wrap;">Tạo bài viết công khai...</div>'
                                        sendText = wsendText.until(EC.visibility_of_element_located((By.XPATH,
                                                                                                     '//div[@aria-label="Tạo bài viết công khai..." and contains(@class, "notranslate _5rpu")]')))
                                        sendText.send_keys(postContent)
                                        print("Da sendkeys")
                                        sleep(randint(10, 15))
                                        wPost = WebDriverWait(browser, 60)  # Maximum wait time of 10 seconds
                                        Post = wPost.until(EC.element_to_be_clickable(
                                            (By.XPATH, '//span[text()="Đăng"]')))
                                        Post.click()
                                        print("Da nhan post")
                                        sleep(randint(5, 7))
                                    except Exception as e:
                                        print(f"Error with {e}")

                                    # Lấy Xpath Restricted POST
                                    try:
                                        browser.implicitly_wait(5)
                                        restricted = browser.find_element(By.XPATH, read_xpath.RestrictedPost)
                                        print("Restricted")
                                        # Lấy thời gian hiện tại
                                        current_datetime = datetime.now()
                                        with lock:
                                            try:
                                                log_save_database = Log_FacebookBot(account, current_datetime, "Content",
                                                                                    "POST",
                                                                                    "No", href)
                                                log_save_database.saveDB()
                                            except Exception as e:
                                                print(f"Exception: {e}")

                                        # Tắt popup Restrict
                                        try:
                                            browser.implicitly_wait(5)
                                            close = browser.find_element(By.XPATH,
                                                                         f"read_xpath.CloseAdPopupVi").click()
                                        except:
                                            try:
                                                browser.implicitly_wait(5)
                                                close = browser.find_element(By.XPATH,
                                                                             read_xpath.CloseAdPopupEn).click()
                                            except:
                                                print("khong popup restrict")
                                        # Do any else
                                        # Suspend 1 hours, do other thing before break
                                        interval_minutes = 5
                                        ack_suspension_hours = 1
                                        suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                        interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                        # Wait for the specified interval and check if 2 hours have passed
                                        elapsed_time = 0
                                        while elapsed_time < suspension_duration:
                                            # Like/comment/share 5 nhóm, 5 bài/nhóm, nghỉ 5 phút
                                            lcsrandom = randint(3, len(element) - 1)

                                            # click từng link vào nhóm
                                            wait6 = WebDriverWait(element[lcsrandom], 30)  # Maximum wait time of 10 seconds
                                            eachGroup = wait6.until(
                                                EC.element_to_be_clickable(
                                                    (By.XPATH,
                                                     f'(//a[@href="{element[lcsrandom].get_attribute("href")}" and @role="link"])[1]')))
                                            eachGroup.click()
                                            print('passsssssss1x')
                                            # Call like robot
                                            # robotLike(browser,element[lcsrandom], accountLike=account)

                                            print("Checking after every {} minutes...".format(interval_minutes))
                                            time.sleep(interval_duration)
                                            elapsed_time += interval_duration
                                        # Break
                                        ez -= 2

                                    except:
                                        try:
                                            browser.implicitly_wait(5)
                                            restricted = browser.find_element(By.XPATH,
                                                                              read_xpath.RestrictedAll)
                                            print("Restricted All")
                                            # Lấy thời gian hiện tại
                                            current_datetime = datetime.now()
                                            with lock:
                                                try:
                                                    log_save_database = Log_FacebookBot(account, current_datetime,
                                                                                        "Content",
                                                                                        "POST",
                                                                                        "No", href)
                                                    log_save_database.saveDB()
                                                except Exception as e:
                                                    print(f"Exception: {e}")
                                            try:
                                                browser.implicitly_wait(5)
                                                close = browser.find_element(By.XPATH,
                                                                             f"read_xpath.CloseAdPopupVi").click()
                                            except Exception as e:
                                                print(f"khong popup quangcao: {e}")
                                                try:
                                                    browser.implicitly_wait(5)
                                                    close = browser.find_element(By.XPATH,
                                                                                 read_xpath.CloseAdPopupEn).click()
                                                except Exception as e:
                                                    print(f"khong popup quangcao: {e}")
                                            # Suspend 1 hours, do other thing before break
                                            # Do any else
                                            interval_minutes = 5
                                            ack_suspension_hours = 1
                                            suspension_duration = ack_suspension_hours * 3600  # Chuyển đổi thời gian treo thành giây
                                            interval_duration = interval_minutes * 60  # Chuyển đổi khoảng thời gian kiểm tra thành giây
                                            # Wait for the specified interval and check if 2 hours have passed
                                            elapsed_time = 0
                                            while elapsed_time < suspension_duration:
                                                print("Checking after every {} minutes...".format(interval_minutes))
                                                time.sleep(interval_duration)
                                                elapsed_time += interval_duration
                                            ez -= 2
                                        except Exception as e:
                                            print(f"No Restrict: {e}")
                                            print("Da post")

                                    # Lấy thời gian hiện tại
                                    current_datetime = datetime.now()
                                    with lock:
                                        try:
                                            log_save_database = Log_FacebookBot(account, current_datetime, "Content",
                                                                                "POST",
                                                                                "Yes", href)
                                            log_save_database.saveDB()
                                        except Exception as e:
                                            print(f"Exception: {e}")
                                except Exception as e:
                                    print(f"Khong cho member post: {e}")
                                sleep(randint(10, 15))
                        except Exception as e:
                            print(f'notpasssssssssx: {e}')
            ez += 1

def search_addGroup(browser):
    wait = WebDriverWait(browser, 10)  

    # Tìm ô tìm kiếm và nhập từ khóa
    search = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Tìm kiếm trên Facebook"]')))
    search.clear()
    search.send_keys("Hội phụ huynh")
    sleep(3)
    
    # Nhấn Enter để tìm kiếm
    actions = ActionChains(browser)
    actions.move_to_element(search).send_keys(Keys.RETURN).perform()
    sleep(5)

    # Nhấp vào "Xem tất cả" để mở danh sách nhóm
    see_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Xem tất cả"]')))
    see_all_button.click()
    sleep(5)

    joined_count = 0  # Đếm số nhóm đã tham gia
    while True:
        try:
            # Lấy danh sách tất cả các nút "Tham gia" hiện có
            join_buttons = browser.find_elements(By.XPATH, '//span[contains(text(),"Tham gia")]')

            if not join_buttons:
                print("Không còn nhóm nào để tham gia.")
                break  # Thoát vòng lặp nếu không còn nhóm

            for button in join_buttons:
                try:
                    if button.is_displayed() and button.is_enabled():
                        button.click()
                        print(f"Đã nhấp vào nút Tham gia ({joined_count + 1})")
                        joined_count += 1
                        sleep(5)  # Đợi để tránh bị phát hiện là bot

                        # Xử lý popup nếu có
                        try:
                            close_button = WebDriverWait(browser, 3).until(
                                EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Close"]'))
                            )
                            close_button.click()
                            print("Đã đóng popup")
                        except Exception:
                            pass  # Nếu không có popup thì bỏ qua

                except Exception as e:
                    print(f"Lỗi khi nhấp vào nút Tham gia: {e}")

            # Cuộn xuống để tải thêm nhóm nếu đã tham gia 5 nhóm
            if joined_count % 5 == 0:
                browser.execute_script("window.scrollBy(0, document.documentElement.scrollHeight);")
                sleep(5)

        except Exception as e:
            print(f"Lỗi trong vòng lặp chính: {e}")
            break  # Nếu có lỗi nghiêm trọng, thoát vòng lặp

    print(f"Đã tham gia tổng cộng {joined_count} nhóm.")

def runLoginPostLikeShareCommentReply(browser, link, account,postContent):
    loginlinkedin(browser, link, account)
    # post_to_facebook(browser)
    # search_addGroup(browser)
    # post2(browser, account=account,postContent=postContent)
    # autoLike(browser)
    # autoComment(browser)
    # autoReply(browser)
    # autoShare(browser)
    
def main(postContent):

    while True:
        # Thực hiện các công việc của vòng lặp ở đây
        # Tạo danh sách các luồng
        threads = []
        for account in listAccount:
            browser = webdriver.Chrome(options=options)
            thread = threading.Thread(target=runLoginPostLikeShareCommentReply, args=(browser, link, account,postContent))
            thread.start()
            threads.append(thread)
        # Đợi cho tất cả các luồng hoàn thành
        for thread in threads:
            thread.join()
        # Kiểm tra thời gian đã trôi qua
        elapsed_time = time.time() - start_time
        # Kiểm tra nếu đã đủ 24 giờ
        if elapsed_time >= loop_duration:
            break
        # Đợi một khoảng thời gian nhỏ (ví dụ: 1 giây) trước khi tiếp tục vòng lặp
        time.sleep(1)

if __name__ == '__main__':
    post_content = create_content()
    Comment = " vnexpress.net"
    main(postContent=post_content)