import os

read=open('notify.txt','r')

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
