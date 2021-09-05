import os
import sys
import time
read=open('notify.txt','r')

#呼叫簽到
try:
    import Gamer_com
    print("巴哈成功!!")
except:
    print("巴哈呼叫失敗")
'''
try:
    import Shopee
    print("蝦皮呼叫成功")
except:
    print("蝦皮呼叫失敗")
'''
time.sleep(2)
os.system('taskkill /im chromedriver.exe /F')
os.system('taskkill /im chrome.exe /F')

#輸出結果
if os.path.getsize('notify.txt') > 0:
    try:
        print("true")
        import notify #呼叫輸出程式
        read.close
        test=open('notify.txt','w')
        test.close
    except:
        print('錯誤!!!')
    
else:
    print("nothing")
