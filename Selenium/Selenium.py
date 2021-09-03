# -*- coding: utf-8 -*-
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#myusername = "XXX"#登錄賬號
#mypassword = "XXX"#登錄密碼

driver = webdriver.Chrome() #模擬瀏覽器打開網站
driver.get("https://www.ctguqmx.com")
#driver.maximize_window() #將視窗最大化

try:
    driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/span/a[1]').click()#定位語句去源碼中找
    time.sleep(2)#延時載入
    
    #找到登錄框，輸入賬號密碼
    driver.find_element_by_xpath("//*[@id='aw-login-user-name']").send_keys("myusername")
    driver.find_element_by_xpath("//*[@id='aw-login-user-password']").send_keys("mypassword")
        
    
    #模擬點擊登錄
    driver.find_element_by_xpath("//*[@id='login_submit']").click()
    time.sleep(2)
    
    #模擬登陸後點擊簽到界面
    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/a").click()
    time.sleep(2)
    
    #模擬點擊簽到
    driver.find_element_by_xpath("//*[@id='qd_button']").click()
    time.sleep(2)
    
    print("簽到成功")
    
except:
        print("簽到失敗")

driver.quit#退出去動