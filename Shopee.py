# -*- coding: utf-8 -*-
import time 
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

config = configparser.ConfigParser()
config.read('shopee.ini')
myusername = config['shopee-com']['shopeename']#登錄賬號
mypassword = config['shopee-com']['shopeepasswd']#登錄密碼


driver = webdriver.Chrome() #模擬瀏覽器打開網站
driver.get("https://user.gamer.com.tw/login.php")
time.sleep(1)
driver.get("https://shopee.tw/")
time.sleep(2)
driver.get("https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2F")
time.sleep(5)
#driver.maximize_window() #將視窗最大化

try:
    #driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/span/a[1]').click()#定位語句去源碼中找
    
    #driver.find_element_by_xpath("//*[@class='navbar__link navbar__link--account navbar__link--tappable navbar__link--hoverable navbar__link-text navbar__link-text--medium']").click()

    #找到登錄框，輸入賬號密碼
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/from/div/div[2]/div[1]/div[1]').send_keys("myusername")
    time.sleep(5)
    driver.find_element_by_xpath("//*[@name='password']").send_keys("mypassword")
    time.sleep(20)

    #模擬點擊登錄
    driver.find_element_by_xpath("//*[@class='_1ruZ5a _3Nrkgj _3kANJY _1IRuK_ hh2rFL _3_offS']").click()
    time.sleep(2)
    0
    #跳轉到簽到畫面
    driver.get("https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2Fshopee-coins")
    time.sleep(2)
    #模擬登陸後點擊簽到界面
    #driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/a").click()
    #time.sleep(2)
    
    #模擬點擊簽到
    driver.find_element_by_xpath("//*[@class='pcmall-coinsrewardpage_327hN9']").click()
    time.sleep(2)
    
    print("簽到成功")
    
except:
    print("簽到失敗")
    notify = open("notify.txt","a")
    notify.write("蝦皮簽到失敗，請手動簽到\nhttps://shopee.tw/shopee-coins\n")
    notify.close()

#driver.quit#退出去動