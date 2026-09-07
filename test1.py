import requests # 請求工具
from bs4 import BeautifulSoup # 解析工具
import time # 用來暫停程式
# 要爬的股票
stock = ["1101","2330"]
for i in range(len(stock)): # 迴圈依序爬股價

    # 現在處理的股票

    stockid = stock[i]

    # 網址塞入股票編號

    url = "https://tw.stock.yahoo.com/quote/"+stockid+".TW"

    # 發送請求

    r = requests.get(url)

    # 解析回應的 HTML

    soup = BeautifulSoup(r.text, 'html.parser')

    # 定位股價
    # 使用更可靠的選擇器：查找 <fin-streamer> 標籤且 data-test 屬性為 'qsp-price'
    price_element = soup.find('fin-streamer', attrs={'data-test': 'qsp-price'})

    if price_element:
        price = price_element.getText() # 獲取文本內容
    else:
        price = "N/A"
        print(f"未能找到股票 {stockid} 的股價元素。請檢查Yahoo股市頁面結構是否改變。")

    # 回報的訊息 (可自訂)
    message = f"股票 {stockid} 即時股價為 {price}"
    print(message) # 印出擷取的股價和訊息
# 定位股價

# 嘗試用更通用的 CSS 選擇器來定位股價，這些類別通常用於主股價顯示
# 注意：類別名稱中的特殊字元如括號需要用反斜線轉義
price_element = soup.select_one('span.Fz\\(32px\\).Fw\\(b\\).Lh\\(1\\).Mend\\(16px\\).D\\(f\\).Ai\\(c\\)')

if price_element:
    price = price_element.getText() # 獲取文本內容
    print(f"目前股價: {price}") # 印出擷取的股價
else:
    print("未能找到股價元素。請檢查Yahoo股市頁面結構是否改變。")
    price = "N/A"
  # 回報的訊息 (可自訂)

message = "股票 "+stockid+" 即時股價為 "+price
 # 用 telegram bot 回報股價

# bot token
token = "8647288022:AAF7zOLHWrZk8T7LKQOOjLAKHY678Pk9gKs"

# 使用者 id
chat_id = "chisu0226"

# bot 送訊息
url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

requests.get(url)

# 每次都停 3 秒
time.sleep(3)
