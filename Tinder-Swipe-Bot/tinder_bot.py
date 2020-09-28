from selenium import webdriver
from time import sleep
from secrets import username, password
class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://tinder.com')
        print('opened tinder webpage')
        sleep(5)
        try:
            print('going for direct popup')
            fb_btn=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn.click()
            if len(self.driver.window_handles)==1:
                self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button').click()
                self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button').click()
                self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button').click()
                self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button').click()
            print('popup complete')
        except Exception:
            print('going for more option')
            more_option_btn=self.driver.find_element_by_xpath("//button[contains(text(), 'More options')]")
            more_option_btn.click()
            fb_btn=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn.click()

        print('waiting for popup to open')
        while(len(self.driver.window_handles)==1):
            sleep(1)
        print('fb login popup opened, switching to popup')
        #switch to pop window
        base_window=self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        print("entered email")
        password_in= self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)
        print("entered password")
        login_btn=self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        print("waiting for tinder to login")
        while len(self.driver.window_handles)==2:
            sleep(1)
        self.driver.switch_to.window(base_window)
        print('logged into tinder')
        sleep(10)
        try:
            allow_location_btn= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            allow_location_btn.click()
            allow_location_btn= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            allow_location_btn.click()
        except:
            allow_location_btn=0
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
    def dislike(self):
        dislike_btn=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()
    def autoswipe(self):
        count_like=0
        count_dislike=0
        from random import random
        while True:
            sleep(3)
            try:
                rand = random()
                if rand< 0.75:
                    self.like()
                    count_like+=1
                    print('right swiped', count_like)
                else:
                    self.dislike()
                    count_dislike+=1
                    print('left swiped', count_dislike)
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()
    
    def close_popup(self):
        popup  = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()
        print('removed popup')
    def close_match(self):
        match_popup= self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
        print('removed match popup')
    
bot= TinderBot()
bot.login()
sleep(10)
bot.autoswipe()