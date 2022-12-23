from bs4 import BeautifulSoup
import requests
import json
import re

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

page = requests.get(URL)
result=json.loads(page.text)
result=dict(result)

with open('PIPpy/Sem10/Valute.json','w', encoding='utf-8') as file:
    for i in page['Valute'].items():
        file.write(str(f'{result}\n'))

page = requests.get(URL).json()

print(page)

print(f"{page['Valute']['USD']['Value']}, {page['Valute']['USD']['Name']}")
print(f"{page['Valute']['EUR']['Value']}, {page['Valute']['EUR']['Name']}")
print(f"{page['Valute']['CNY']['Value']}, {page['Valute']['CNY']['Name']}")



# filteredNews = []
# allNews = []

# soup = BeautifulSoup(page.text, "html.parser")

# print(soup)

# allNews = soup.findAll('Name', class_='Value')

# for data in allNews:
#     if data.find('Name', class_='value Previous') is not None:
#         filteredNews.append(data.text)

# for data in filteredNews:
#     print(data)

    # bot.message_handler(message.chat.id,exchange)
    # URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    # page = requests.get(URL).json()
    # if message.chat.id=='USD':
    #     bot.send_message(message.chat.id,f"{page['Valute']['USD']['Value']}, {page['Valute']['USD']['Name']}")
    # elif message.chat.id=='EUR':   
    #     bot.send_message(message.chat.id,f"{page['Valute']['EUR']['Value']}, {page['Valute']['EUR']['Name']}")
    # elif message.chat.id=='CNY':
    #     bot.send_message(message.chat.id,f"{page['Valute']['CNY']['Value']}, {page['Valute']['CNY']['Name']}")