from selenium import webdriver
import time


print("""
Welcome to Instagram Bot 

1) follow
2) like
3) comment

""")

choice = input("Enter your choice: ")
follow_control = 0
like_control = 0
comment_control = 0
count = 1

if choice == "1":
    name = input("Enter Instagram Username: ")
    follow_control = 1
elif choice == "2":
    link = input("Enter Instagram Link: ")
    like_control = 1
elif choice == "3":
    link = input("Enter Instagram Link: ")
    comment = input("Enter Instagram Comment: ")
    comment_control = 1

settings = webdriver.FirefoxOptions()
settings.headless = True
path = "gecko driver path"
browser = webdriver.Firefox(options=settings, executable_path=path)

while True:
    browser.get("https://www.instagram.com/")
    time.sleep(5)

    username = browser.find_element_by_xpath("username area xpath")
    password = browser.find_element_by_xpath("password area xpath")
    username.send_keys("<Username>{}".format(str(count)))
    password.send_keys("<Password>")
    time.sleep(2)
    browser.find_element_by_xpath("login button xpath").click()
    time.sleep(2)

    if follow_control == 1:
        browser.get("https://www.instagram.com/{}".format(name))
        time.sleep(2)
        browser.find_element_by_xpath("follow button xpath").click()
    if like_control == 1:
        browser.get(link)
        time.sleep(2)
        browser.find_element_by_xpath("like button xpath").click()
    if comment_control == 1:
        browser.get(link)
        time.sleep(2)
        browser.find_element_by_xpath("comment button xpath").click()
        time.sleep(1)
        browser.find_element_by_xpath("write comment button xpath").send_keys(comment)
        time.sleep(1)
        browser.find_element_by_xpath("share comment button xpath").send_keys(comment)

    time.sleep(2)
    browser.get("https://www.instagram.com/{}{}".format(username.text, count))
    time.sleep(3)
    browser.find_element_by_xpath("settings button xpath").click()
    time.sleep(1)
    browser.find_element_by_xpath("logout button xpath").click()
    time.sleep(1)
    count = count + 1
    if count == 5:
        break
browser.close()














