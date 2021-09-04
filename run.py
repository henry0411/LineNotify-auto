import os
import sys
import time
read=open('notify.txt','r')

#呼叫簽到
try:    
    import Auto_run
    print("呼叫成功!!")
    #import Gamer
    
except:
    print("呼叫失敗")

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
