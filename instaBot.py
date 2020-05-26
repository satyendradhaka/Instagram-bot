from selenium import webdriver
from time import sleep
from secrets import username, password
class InstagramBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        print('bot initiated')
    
    def login(self):
        self.driver.get('https://www.instagram.com/')
        print('opened instagram webpage')
        print('waiting for page to load fully')
        sleep(5)
        print('page loaded fully')
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/button').click()
        print('going for login through fb')
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
        print('email entered')
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
        print('entered password')
        self.driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
        print('facebook login clicked waiting for instagram to open')
        sleep(30)
        print('instagram opened')
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    
    def get_unfollowers(self):
        print('going for profile page')
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div').click()
        print('waiting for profile page to open')
        sleep(5)
        print('profile page opened')
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        print('opening following list')
        followings = self._get_names()
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        print('opening followers list')
        followers = self._get_names()
        not_following_back = [user for user in followings if user not in followers]
        not_following_back.reverse()
        for name in not_following_back:
            print('searching for profile of', name)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]').click()
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(name)
            sleep(5)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()
            print('profile found of', name)
            sleep(5)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
            value=input('want to unfollow: ')
            if value.upper()=='YES':
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
                print('unfollowed', name)
            else:
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
                print('unfollow cancelled for', name)

    
    def _get_names(self):
        sleep(2)
        print('scrolling through list')
        scroll_box=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht=ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text!='']
        #hitting close button
        print('closing list')
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()

        return names
bot=InstagramBot()

bot.login()
sleep(3)
bot.get_unfollowers()