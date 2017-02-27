#куда сохраняем
'''
    import sys, os 
    os.getcwd() #узнать, какая сейчас директория
    os.chdir('C:\\......')
    
'''
import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

A=[] 
df=pd.DataFrame(A,columns=['id_Q', 'id_vk', 'followed']) 

import datetime
begin = str(datetime.datetime.now())

range_from = 1
range_to = 4000
for i in range(range_from, range_to + 1): 
    theQ = str('https://thequestion.ru/account/') 
    theQ = theQ + str(i) 
    theQ = requests.get(theQ) 
    # print(theQ.text) 
    
    
    page = BeautifulSoup(theQ.text, 'html.parser') 
    link_vk = page.find('a', {'class': 'profile__header-social-icon font-icon theq_social_vk_fill'}).get('href')  
    theQ_with_name = page.find('meta', {'property': 'og:url'}).get('content') 
    theQ_with_name = theQ_with_name + str('?filter=followed') 
    theQ_with_name = requests.get(theQ_with_name) 
    theQ_with_name = BeautifulSoup(theQ_with_name.text, 'html.parser') 
    followed = theQ_with_name.find_all('div', {'class': 'list-questions__header-center'})   
    if followed is None: 
        followed = "NA"
    else: 
        followed = "1"
        
    df.loc[len(df)]=[str(i), link_vk, followed]
    
    if i % 1000 == 0: #сохраняем через каждую тысячу
        df.to_csv('dataset_' + str(range_from) + '-' + str(i) +'.csv')
        
df.to_csv('dataset_' + str(range_from) + '-' + str(range_to) +'.csv')  #сохранится в директорию
end = str(datetime.datetime.now()) 









