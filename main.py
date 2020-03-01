from selenium import webdriver
from time import sleep
from secrets import pw

class InstaBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/p/a")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")\
            .send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")\
            .click()
        sleep(2)        
    
    
    def likeFunc(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")\
        .click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div[1]/div/div[1]/div[3]/a/div/div[2]")\
        .click()
        sleep(3)
        self.driver.refresh()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button")\
            .click()
        self.driver.refresh()

    def loop(self):  
        for i in range(10) : 
            self.likeFunc()

abdullah = InstaBot("abdullahmafuz1@gmail.com", pw)
abdullah.loop()