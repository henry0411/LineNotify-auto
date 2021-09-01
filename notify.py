from bs4 import BeautifulSoup
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

token=config['notify']['token'] #notify的token放在這
toke=open('notify.txt','r')#讀取的檔案

response = requests.get("https://www.udemy.com/course/codegym-python/")
soup = BeautifulSoup(response.text, "html.parser")

#price = soup.find("span", {"class": "price-text__current"}).getText()[7:]  #取得文字中的價格部分
#price=1
#if int(price) < 500:  #將爬取的價格字串轉型為整數
headers = {
"Authorization": "Bearer " + token,
"Content-Type": "application/x-www-form-urlencoded"
   } 

params = { "message" : '\n' + toke.read()}
 
r = requests.post("https://notify-api.line.me/api/notify",
                  headers=headers, params=params)
print(r.status_code)  #200

