from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import getopt
import time
import sys
import os


username = ""
password = ""
number_of_pages = 5
targeted_username = ["blackpink", "soyaa", "pink", "soo", "yaaa"]
save_info = False
allow_notification = False


def usage():
    print("LIKE IG POST AUTOMATICALLY")
    print()
    print("Usage: ig_like_post.py -u your_ig_username -p your_ig_password")
    print("-u           --username            - username of your instagram account")
    print("-p           --password            - password of your account")
    print(
        '-t           --targeted_username   - name of user that you want to track and like, make sure usernames inside "" and no whitespace in ""'
    )
    print("-n           --number_of_pages     - number of pages you want to like")
    print("-s           --save-info           - do you want to save your cookies")
    print(
        "-a           --allow_notification  - do you want to allow browser to send you notification"
    )
    print()
    print()
    print("Examples:")
    print("ig_like_post.py -username your_ig_username -p your_ig_password")
    print(
        'ig_like_post.py -username your_ig_username -p your_ig_password -user "blackpink,jisoo,rosie" -n 5'
    )
    print(
        "ig_like_post.py -username your_ig_username -p your_ig_password -save-info -get-noti"
    )


def init():
    global username
    global password
    global targeted_username
    global number_of_pages
    global save_info
    global allow_notification

    if not len(sys.argv[1:]) > 1:
        usage()

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "u:p:t:n:sa",
            [
                "username",
                "password",
                "targeted_username",
                "number_of_pages",
                "save_info",
                "allow_notification",
            ],
        )
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-u", "--username"):
            username = a
        elif o in ("-p", "--password"):
            password = a
        elif o in ("-t", "--targeted_username"):
            targeted_username = a.split(",")
        elif o in ("-n", "--number_of_pages"):
            number_of_pages = int(a)
        elif o in ("-s", "--save_info"):
            save_info = True
        elif o in ("-a", "--allow_notification"):
            allow_notification = True
        else:
            assert False, "Unhandled Option"
    bot(username, password, targeted_username, save_info, allow_notification)


class bot:
    def __init__(
        self, username, password, targeted_username, save_info, allow_notification
    ):
        self.username = username
        self.password = password
        self.users = targeted_username
        self.save_info = save_info
        self.allow_notification = allow_notification
        self.base_url = "https://www.instagram.com/"
        self.bot = webdriver.Chrome("/usr/bin/chromedriver")
        self.login()

    def login(self):
        self.bot.get(self.base_url)
        time.sleep(5)

        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, "username"))
        )
        enter_username.send_keys(self.username)

        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, "password"))
        )
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        print("end login")
        time.sleep(5)

        if not self.save_info:
            print("Do not save info")
            do_not_save_info = self.bot.find_element(By.CLASS_NAME, "_acao")
            do_not_save_info.click()
            time.sleep(5)

        if not self.allow_notification:
            print("Do not show notification")
            do_not_show_notification = self.bot.find_element(By.CLASS_NAME, "_a9_1")
            do_not_show_notification.click()
            time.sleep(3)
        # self.like_post()
        self.search_targeted_user()

    def search_targeted_user(self):
        time.sleep(2)
        WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located(
                (By.CLASS_NAME, "_aacw ._aap6._aap7._aap8 a")
            )
        )
        first_all_tags = self.bot.find_elements(
            By.CLASS_NAME, "_aacw ._aap6._aap7._aap8 a"
        )
        for i in first_all_tags:
            for j in self.users:
                if j in i.text:
                    index = first_all_tags.index(i)
                    print(i.text)
                    print(index)
                    WebDriverWait(self.bot, 20).until(
                        expected_conditions.presence_of_element_located(
                            (By.CLASS_NAME, "_aamw ._abl-")
                        )
                    )
                    like_button = self.bot.find_elements(By.CLASS_NAME, "_aamw ._abl-")
                    like_button[index].click()

        for i in range(5):
            self.bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            WebDriverWait(self.bot, 20).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "_aacx ._aap6._aap7._aap8 a")
                )
            )
            all_tags = self.bot.find_elements(
                By.CLASS_NAME, "_aacx ._aap6._aap7._aap8 a"
            )
            for i in all_tags:
                for j in self.users:
                    if j in i.text:
                        index = all_tags.index(i)
                        print(i.text)
                        print(index)
                        like_button = WebDriverWait(self.bot, 20).until(
                            expected_conditions.presence_of_element_located(
                                (By.CLASS_NAME, "_aamw ._abl-")
                            )
                        )
                        like_button[index].click()
        # time.sleep(3)
        input()

    def like_post(self):
        first_all_tags = self.bot.find_elements(
            By.CLASS_NAME, "_aacw ._aap6._aap7._aap8 a"
        )
        for i in first_all_tags:
            for j in self.users:
                if j in i.text:
                    print(i.text)
                    self.bot.find_elements(By.CLASS_NAME, "_aamw ._abl-").click()
                else:
                    counter += 1
        input()


init()
