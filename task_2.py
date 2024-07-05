from selenium import webdriver

from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

# from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By

# import codecs

# import re

# from fastapi import FastAPI

from webdriver_manager.chrome import ChromeDriverManager

import json

# graphic_card_name=[]
# graphic_card_price=[]

website='https://www.nvidia.com/en-in/geforce/buy/'
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install())) # Optional argument, if not specified will search path.
driver.get(website);
graphic_cards=driver.find_elements(By.XPATH,'//div[@class="nv-container container responsivegrid"]/div/div')
graphic_cards.pop()
graphic_cards.pop()
graphic_cards.pop()
graphic_cards.pop()
gc_dict={}
# try:
#     graphic_cards[2].find_element(By.CLASS_NAME,'startingprice').text 
# except:
#     print('false')

for graphic_card in graphic_cards:
    key=graphic_card.find_element(By.XPATH,'./div/div/div/div/h3').text

    try:
        value=""
        price=graphic_card.find_element(By.CLASS_NAME,'startingprice').text
        for i in price:
            if i.isdigit():
                value=value+i
        new_value=int(value)
    except:
        new_value="N/A"
    gc_dict[key]=new_value

# print(gc_dict)
# print(graphic_card_price)
# json_object = json.dumps(gc_dict, indent = 4)
# print(json_object)

# app=FastAPI()
# @app.get("/")
# async def hello():
#     return json_object

driver.quit()
