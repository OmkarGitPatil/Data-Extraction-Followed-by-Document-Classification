import requests
from bs4 import BeautifulSoup
from autoscraper import AutoScraper
import pandas as pd


df=pd.read_excel(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\Input.xlsx')

url_list=df['URL'].to_list()
sequence=df['URL_ID'].to_list()

for i in range(0,len(url_list)):
    print(sequence[i])
    url=url_list[i]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}

    html_text=requests.get(url,headers=headers).text
    soup=BeautifulSoup(html_text,'lxml')

    title=soup.find('h1')
    text_list=soup.find_all('p')

    texts=[]
    for j in text_list:
        texts.append(j.text)


    post_content=soup.find('div', class_='td-post-content')
    bullet_list=post_content.find_all('li')

    bullet_text=[]
    for j in bullet_list:
        bullet_text.append(j.text)

    content_list=[]

    content_list.append(title.text)
    content_list.append(':')
    content_list.extend(texts)
    content_list.extend(bullet_text)
    string=' '.join(content_list)

    
    directory=f'C:\\Users\\Omkar\\Desktop\\Practice\\Datasets\\Document Classification\\Text Files\\{sequence[i]}.txt'
    with open(directory,'w',encoding='utf-8') as file:
        file.write(string)
    