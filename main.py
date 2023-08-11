import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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


    # def follow(self):
    # 
    #     print("I I will follow you")


    # def find_follower(self):
    #     # - just for now
    #     self.driver.get("https://www.instagram.com/elonrmuskk/")
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, '//button[contains(text(), "Decline optional cookies")]').click()
    #     time.sleep(3)
    #
    #     search_box = self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
    #     search_box.send_keys(SIMILAR_ACCOUNT)
    #     search_box.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
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


# insta_bot.login()
insta_bot.follow()
insta_bot.find_follower()