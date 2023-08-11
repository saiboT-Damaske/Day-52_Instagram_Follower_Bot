import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

import time

SIMILAR_ACCOUNT = "elonrmuskk"
USERNAME = ""
PASSWORD = ""

OPTIONS = Options()
OPTIONS.add_experimental_option("detach", True)


class InstaFollower:

    def __init__(self):
        self.driver = selenium.webdriver.Chrome(options=OPTIONS)
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://instagram.com")
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//button[contains(text(), "Decline optional cookies")]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//span[contains(text(), "Log in with Facebook")]/..').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[contains(text(), "Decline optional cookies")]').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'email').send_keys(USERNAME)
        self.driver.find_element(By.ID, 'pass').send_keys(PASSWORD)
        self.driver.find_element(By.ID, 'pass').send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(By.XPATH, '//button[contains(text(), "followers")]')
        followers.click()

        time.sleep(2)
        # modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        modal = self.driver.find_element(By.XPATH, '//span[contains(text(), "Meta")]')
        for i in range(1):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup)
            # element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()



insta_bot = InstaFollower()

insta_bot.login()

insta_bot.find_followers()

insta_bot.follow()
