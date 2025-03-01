import csv
from datetime import date
import random
from time import sleep
import asyncio
from bs4 import BeautifulSoup
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
import threading
import pandas as pd
import logging
import sys
import pyodbc
import read_xpath

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument("start-maximized")
options.add_argument("--incognito")
#browser = webdriver.Chrome(options=options)
link = "https://www.linkedin.com/login/vi"
listAccount = ["alphagamingisbest@gmail.com"]
passwd = "Hoang@11204"
lock = threading.Lock()
# Thời gian bắt đầu
start_time = time.time()
# Thời gian chạy của vòng lặp (24 giờ = 86400 giây)
loop_duration = 2 * 60
# Từ khóa tìm kiếm nhóm
searchKey = "gia sư"

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

def loginlinkedin(browser, link, account):
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

def autoComment(browser, comment):
    sleep(10) #wait for authority
    browser.get("https://www.linkedin.com/groups/")
    href_links = browser.find_elements(By.XPATH, "//a[contains(@class, 'group-listing-item__title-link')]")
    links = []  # Đổi tên biến từ 'link' thành 'links' để tránh bị ghi đè

    for element in href_links:
        links.append(str(element.get_attribute('href')))  # Thêm URL của mỗi nhóm vào danh sách 'links'

    wait = WebDriverWait(browser, 30)
    if not links:
        print("you're not in any group, try to search and add some group")
        return
    else:
        sleep(5)
        # comment to post in groups
        for group in links:
            try:
                #access to group
                browser.get(group)
                sleep(5)
                
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                for i in range(5):  # Process 5 posts on the peek
                    # croll to last
                    time.sleep(5)
                    #find post list
                    posts = browser.find_elements(By.XPATH, "//div[contains(@class, 'feed-shared-update-v2__control-menu-container')]")
                    if len(posts) > 0:
                        for post in posts:
                            commentButton = post.find_element(By.XPATH, './/button[@aria-label="Bình luận"]')
                            ActionChains(browser).move_to_element(commentButton).click(commentButton).perform()
                            sleep(5)

                            commentIn = WebDriverWait(post, 10).until(EC.visibility_of_element_located((By.XPATH, './/div[contains(@class,"ql-editor")]')))
                            commentIn.send_keys(comment)
                            sleep(5)

                            submitButton = post.find_element(By.XPATH, ".//button[contains(@class, 'comments-comment-box__submit-button')]")
                            submitButton.click()
                            sleep(5)
                            print("commented ")
            except Exception as e:
                print("unable to connect to group error ", e)


def autoLike(browser):
    waitfor = WebDriverWait(browser, 10) # wait for maximum is 10 sec

    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # croll to last
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(5)
        #find post list
        post_list = waitfor.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-id, 'urn:li:activity:')]")))
        posts = post_list.find_elements(By.XPATH, "//div[contains(@data-id, 'urn:li:activity:')]")
        print(len(posts))
        # manipulate with each post
        for post in posts:
            try:
                # Cuộn bài viết vào tầm nhìn
                ActionChains(browser).move_to_element(post).perform()
                time.sleep(randint(5, 12))
                
                # Tìm nút like trong bài viết
                like_button = post.find_element(By.XPATH, ".//button[contains(@class, 'artdeco-button') and contains(@aria-label, 'Thích')]")
                
                # Kiểm tra nếu chưa like
                if 'active' not in like_button.get_attribute("class"):
                    like_button.click()
                    print("Đã like bài viết:", post.get_attribute("data-id"))
                    time.sleep(randint(5, 12))
            except Exception as e:
                print("Lỗi khi like bài viết:", str(e))

        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

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
#done
def post_to_linkedin(browser, account, postContent):
    sleep(10)
    browser.get("https://www.linkedin.com/groups/")
    href_links = browser.find_elements(By.XPATH, "//a[contains(@class, 'group-listing-item__title-link')]")
    links = []  # Đổi tên biến từ 'link' thành 'links' để tránh bị ghi đè

    for element in href_links:
        links.append(str(element.get_attribute('href')))  # Thêm URL của mỗi nhóm vào danh sách 'links'
        
    print(links)  # In ra danh sách các liên kết

    
    wait = WebDriverWait(browser, 30)
    if not links:
        print("you're not in any group, try to search and add some group")
        return
    else:
        # post to group
        for group in links:
            try:
                #access to group
                browser.get(group)
                sleep(5)

                postButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text() = 'Start a public post']")))
                postButton.click()
                sleep(5)
                #find pop up
                postPopUp = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'share-box']")))
                sleep(randint(2,5))
                print("found share box")
                #find post text
                try:
                    postInput = postPopUp.find_element(By.XPATH, "//div[contains(@class, 'ql-editor')]").send_keys(postContent)
                    sleep(randint(5, 12))# stop to avoid web's scan
                    print("sended: " + postContent)
                    #nhan nut dang bai
                    postButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'share-actions__primary-action')]")))
                    postButton.click()
                    print("posted")
                    sleep(randint(1, 5))

                    # Chờ đợi thẻ thông báo hiển thị sau khi đăng bài
                    try:
                        feedbackMessage = WebDriverWait(postPopUp, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='artdeco-inline-feedback__message']")))
                        if feedbackMessage.is_displayed():
                            # Nếu thẻ đã hiển thị, nhấn nút Hủy bỏ (hoặc thực hiện các hành động khác)
                            exitPopButton = WebDriverWait(postPopUp, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Hủy bỏ"]'))).click()
                            sleep(5)
                            print("Thẻ thông báo xuất hiện, đã hủy bỏ.")

                            #xác nhận hủy bỏ
                            confirmPopUp = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="alertdialog"]')))
                            confirmButton = confirmPopUp.find_element(By.XPATH, '//button[@data-control-name="share_draft_discard"]')
                            sleep(5)
                    except Exception as e:
                        print("Không tìm thấy thẻ thông báo: ", e)
                except:
                    print("da dang het content")
            except Exception as e:
                print("unable to connect to group error ", e)

#done
def search_addGroup(browser, searchKey):
    wait = WebDriverWait(browser, 30) # wait maximum to 30 sec if there need verified  

    search = wait.until(EC.visibility_of_element_located((By.XPATH, read_xpath.searchField)))
    search.send_keys(searchKey)
    sleep(randint(5, 7))
    # print("nhap duoc")
    
    # Nhấn Enter để tìm kiếm
    actions = ActionChains(browser)
    actions.move_to_element(search).send_keys(Keys.RETURN).perform()
    sleep(5)

    # Chờ đến khi nút nhóm nhấn được thì nhấn
    groupButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='search-reusables__filters-bar']/ul/li[4]")))
    groupButton.click()
    sleep(5)

    joined_count = 0  # Đếm số nhóm đã tham gia
    while True:
        try:
            join_buttons = browser.find_elements(By.XPATH, "//button[contains(@aria-label, 'Nối') or contains(@aria-label, 'Tham gia')]")

            if not join_buttons:
                print("No groups left to join in this page")
                #nhấn tiếp theo để tìm thêm group
                nextButton = browser.find_element(By.XPATH, '//button[@aria-label="Tiếp theo"]')
                if not nextButton and joined_count == 20:
                    print("last page")
                    break  # Exit the loop if no groups to join
                else:
                    nextButton.click()
                    sleep(5)
            else:
                for button in join_buttons:
                    try:
                        if button.is_displayed() and button.is_enabled():
                            button.click()
                            print(f"Clicked 'Join' button for group {joined_count + 1}")
                            joined_count += 1
                            if joined_count == 20: # if reach the peak of maximum adding group on linkedin
                                break
                            sleep(randint(5, 7))  # Wait to avoid being flagged as a bot

                            # Handle any pop-ups (e.g., confirmation dialogs)
                            try:
                                close_button = WebDriverWait(browser, 3).until(
                                    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Close"]'))
                                )
                                close_button.click()
                                print("Closed pop-up")
                            except Exception:
                                pass  # Ignore if there's no pop-up

                    except Exception as e:
                        print(f"Error clicking 'Join' button: {e}")

        except Exception as e:
            print(f"Error in main loop: {e}")
            break  # Exit loop on serious error


def runLoginPostLikeShareCommentReply(browser, link, account, postContent, searchKey, Comment):
    loginlinkedin(browser, link, account)

    # search_addGroup(browser, searchKey)
    # post_to_linkedin(browser, account, postContent)
    # autoLike(browser)
    autoComment(browser, Comment)
    # autoReply(browser)
    # autoShare(browser)
    
def main(postContent, Comment):

    while True:
        # Thực hiện các công việc của vòng lặp ở đây
        # Tạo danh sách các luồng
        threads = []
        for account in listAccount:
            browser = webdriver.Chrome(options=options)
            thread = threading.Thread(target=runLoginPostLikeShareCommentReply, args=(browser, link, account,postContent, searchKey, Comment))
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
    postContent = create_content()
    Comment = create_content()
    main(postContent, Comment)