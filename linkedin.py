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
import threading
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
link = "https://www.linkedin.com/login"
account = "htvhtv1239@gmail.com"
passwd = "Hoang@11204"
lock = threading.Lock()
# Thời gian bắt đầu
start_time = time.time()
# Thời gian chạy của vòng lặp (24 giờ = 86400 giây)
loop_duration = 2 * 60
# Từ khóa tìm kiếm nhóm
searchKey = "Artificial"

# create some quotes to comment or post if u want
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

def autoLikeComment(browser, comment):
    waitfor = WebDriverWait(browser, 10) # wait for maximum is 10 sec

    last_height = browser.execute_script("return document.body.scrollHeight")
    
    for i in range(3):
        # croll to last
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(5)
        #find post list
        try:
            post_list = waitfor.until(EC.visibility_of_element_located((By.XPATH, read_xpath.FiniteScroll)))
            posts = post_list.find_elements(By.XPATH, read_xpath.Post)
            print(len(posts))
            
            if len(posts) == 0:
                print("group has no post")
            else:
                # manipulate with each post
                length = len(posts) if len(posts) < 5 else 5
                
                for i in range(length):
                    post = posts[i]
                    try:
                        # Cuộn bài viết vào tầm nhìn
                        ActionChains(browser).move_to_element(post).perform()
                        time.sleep(randint(5, 12))
                        
                        # Tìm nút like trong bài viết
                        like_button = post.find_element(By.XPATH, read_xpath.LikeButton)
                        
                        # Click vào nút like
                        like_button.click()
                        print("Đã like bài viết:", post.get_attribute("data-id"))
                        time.sleep(randint(5, 12))
                        
                        # Tìm nút bình luận trong bài viết
                        commentButton = post.find_element(By.XPATH, read_xpath.CommentButton)
                        ActionChains(browser).move_to_element(commentButton).click(commentButton).perform()
                        sleep(5)
                        # Nhập nội dung bình luận
                        commentIn = WebDriverWait(post, 10).until(EC.visibility_of_element_located((By.XPATH, '')))
                        commentIn.send_keys(comment)
                        sleep(5)
                        # Nhấn nút gửi bình luận
                        submitButton = post.find_element(By.XPATH, read_xpath.SendCommentButton)
                        submitButton.click()
                        sleep(5)
                        print("commented ")
                        # try:
                        #     lastScroll = browser.find_element(By.XPATH, ".//button[contains(@class, 'scaffold-finite-scroll__load-button')]")
                        #     if lastScroll:
                        #         lastScroll.click()
                        #         time.sleep(randint(5, 12))
                        #     else:
                        #         pass
                        # except:
                        #     pass
                    except Exception as e:
                        print("Lỗi khi like bài viết:", str(e))
        except Exception as e:
            print("unable to find post list", e)
            break
        
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

#done
def post_to_linkedin(browser, account, postContent):
    sleep(10)
    browser.get("https://www.linkedin.com/groups/")
    href_links = browser.find_elements(By.XPATH, read_xpath.GroupList)
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

                postButton = wait.until(EC.element_to_be_clickable((By.XPATH, read_xpath.PostButton)))
                postButton.click()
                sleep(5)
                #find pop up
                postPopUp = wait.until(EC.element_to_be_clickable((By.XPATH, read_xpath.PostPopUp)))
                sleep(randint(2,5))
                print("found share box")
                #find post text
                try:
                    postInput = postPopUp.find_element(By.XPATH, "").send_keys(postContent)
                    sleep(randint(5, 12))# stop to avoid web's scan
                    print("sended: " + postContent)
                    #nhan nut dang bai
                    postButton = wait.until(EC.element_to_be_clickable((By.XPATH, read_xpath.PostSubmitButton)))
                    postButton.click()
                    print("posted")
                    sleep(randint(1, 5))

                    # Chờ đợi thẻ thông báo hiển thị sau khi đăng bài
                    try:
                        feedbackMessage = WebDriverWait(postPopUp, 10).until(EC.presence_of_element_located((By.XPATH, read_xpath.FeedBack)))
                        if feedbackMessage.is_displayed():
                            # Nếu thẻ đã hiển thị, nhấn nút Hủy bỏ (hoặc thực hiện các hành động khác)
                            exitPopButton = WebDriverWait(postPopUp, 10).until(EC.element_to_be_clickable((By.XPATH, ''))).click()
                            sleep(5)
                            print("Thẻ thông báo xuất hiện, đã hủy bỏ.")

                            #xác nhận hủy bỏ
                            confirmPopUp = wait.until(EC.element_to_be_clickable((By.XPATH, '')))
                            confirmButton = confirmPopUp.find_element(By.XPATH, read_xpath.ConfirmButton)
                            confirmButton.click()
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
    
    # Nhấn Enter để tìm kiếm
    actions = ActionChains(browser)
    actions.move_to_element(search).send_keys(Keys.RETURN).perform()
    sleep(5)

    # Chờ đến khi nút nhóm nhấn được thì nhấn
    groupButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Groups' and contains(@class, 'artdeco-pill artdeco-pill--slate')]")))
    groupButton.click()
    sleep(5)

    joined_count = 0  # Đếm số nhóm đã tham gia
    while True:
        try:
            join_buttons = browser.find_elements(By.XPATH, "//button[contains(@aria-label, 'Nối') or contains(@aria-label, 'Join')]")
            
            if not join_buttons:
                print("No groups left to join in this page")
                #nhấn tiếp theo để tìm thêm group
                try:
                    sleep(2)
                    
                    nextButton = browser.find_element(By.XPATH, '//button[@aria-label="Next"]')
                    ActionChains(browser).move_to_element(nextButton).click(nextButton).perform()
                    sleep(5)
                    
                    if not nextButton and joined_count == 20:
                        print("last page")
                        break  # Exit the loop if no groups to join
                    else:
                        nextButton.click()
                        sleep(5)
                except Exception as e:
                    print(f"Error clicking 'Next' button: {e}")
            else:
                for button in join_buttons:
                    try:
                        sleep(2)
                        
                        if button.is_displayed() and button.is_enabled():
                            span = button.find_element(By.TAG_NAME, "span")
                            button_text_before = span.text
                            sleep(2)
                            if button_text_before == "Tham gia" or button_text_before == "Join":
                                actions = ActionChains(browser)
                                actions.move_to_element(button).perform()
                                button.click()

                                # if button_text_after == "Tham gia" or button_text_after == "Join":
                                #     print("reach the maximum group")
                                #     browser.quit()
                                #     break
                            print(f"Clicked 'Join' button for group {joined_count + 1}")
                            joined_count += 1
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

def swapGroup(browser, comment):
    browser.get("https://www.linkedin.com/groups/")
    href_links = browser.find_elements(By.XPATH, read_xpath.GroupList)
    links = []  # Đổi tên biến từ 'link' thành 'links' để tránh bị ghi đè

    for element in href_links:
        links.append(str(element.get_attribute('href')))  # Thêm URL của mỗi nhóm vào danh sách 'links'
        
    print(links)  # In ra danh sách các liên kết
    
    wait = WebDriverWait(browser, 30)
    
    if not links:
        print("you are not in any group please search and add some gr")
    else:
        for link in links:
            browser.get(link)
            sleep(10)
            print("access to group", link)
            
            autoLikeComment(browser, comment)
            sleep(5)
            
                

def runLoginPostLikeShareCommentReply(browser, link, account, postContent, searchKey, Comment):
    loginlinkedin(browser, link, account)

    # search_addGroup(browser, searchKey)
    # post_to_linkedin(browser, account, postContent)
    swapGroup(browser, Comment)
    # autoComment(browser, Comment)
    # autoReply(browser)
    # autoShare(browser)
    
def main(postContent, Comment): 
    browser = webdriver.Chrome(options=options)
    runLoginPostLikeShareCommentReply(browser, link, account,postContent, searchKey, Comment)

if __name__ == '__main__':
    postContent = create_content()
    Comment = "Thanks for sharing this post"
    main(postContent, Comment)