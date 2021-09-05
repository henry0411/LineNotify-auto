# -*- coding: utf-8 -*-
import time 
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

config = configparser.ConfigParser()
config.read('gamer.ini')
myusername = config['gamer-com']['gamername']#登錄賬號
mypassword = config['gamer-com']['gamerpasswd']#登錄密碼

driver = webdriver.Chrome() #模擬瀏覽器打開網站
driver.get("https://user.gamer.com.tw/login.php")
#driver.maximize_window() #將視窗最大化

try:
    #driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/span/a[1]').click()#定位語句去源碼中找
    #time.sleep(2)#延時載入
        
    #找到登錄框，輸入賬號密碼
    driver.find_element_by_xpath("//*[@id='uidh']").send_keys(myusername)
    driver.find_element_by_xpath("//*[@type='password']").send_keys(mypassword)
    time.sleep(2)        
        
    #模擬點擊登錄
    driver.find_element_by_xpath("//*[@type='submit']").click()
    time.sleep(5)

    driver.get("https://user.gamer.com.tw/login.php")
    time.sleep(2)
    #模擬登陸後點擊簽到界面
    #driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/a").click()
    #time.sleep(2)
        
    #模擬點擊簽到
    driver.find_element_by_xpath("//*[@id='signin-btn']").click()
    time.sleep(2)

    print("簽到成功")
        
except:
    print("簽到失敗")
    notify = open("notify.txt","a")
    notify.write("巴哈姆特簽到失敗，請手動簽到\ngamer.com.tw\n")
    notify.close()

try:
        #領取雙倍八幣
        driver.find_element_by_xpath("//*[@class='popoup-ctrl-btn']").click()
        time.sleep(3)

        driver.find_element_by_xpath("//*[@class='rewardResumebutton']").click()
        time.sleep(30000)
except:    
    print("雙倍巴幣領取失敗")

driver.quit#退出去動