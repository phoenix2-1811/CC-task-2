from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from selenium import webdriver

from selenium.webdriver.chrome.service import Service


from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By


from webdriver_manager.chrome import ChromeDriverManager

import json

class scrapingApi(APIView):
    def get(self,request):
        
        website='https://www.nvidia.com/en-in/geforce/buy/'
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install())) # Optional argument, if not specified will search path.
        driver.get(website);
        graphic_cards=driver.find_elements(By.XPATH,'//div[@class="nv-container container responsivegrid"]/div/div')
        graphic_cards.pop()
        graphic_cards.pop()
        graphic_cards.pop()
        graphic_cards.pop()
        gc_dict={}
        

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
        
        driver.quit()
        response =  Response(
            data= gc_dict,
            status=status.HTTP_200_OK
            )
        response["Access-Control-Allow-Origin"] = "*"
        return response