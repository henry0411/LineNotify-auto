import time
import os
try:
    import Gamer_com
    
    print("巴哈已開啟")
except:
    print("巴哈開啟失敗")
time.sleep(2)
os.system('taskkill /im chromedriver.exe /F')
os.system('taskkill /im chrome.exe /F')