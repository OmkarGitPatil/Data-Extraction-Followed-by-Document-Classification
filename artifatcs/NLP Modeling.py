import pandas as pd
import numpy as np
import glob
import re
import nltk 
from string import punctuation
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer,LancasterStemmer
import json

files_path=glob.glob(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\StopWords'+'\*.txt')

list1=[]
for i in files_path:
    with open(i,'r') as file:
        content=file.read()
        text=re.sub('[\n-]+',',',content)
        stop_words=re.findall('[\w]+',text)
        list1.extend(stop_words)

stop_words_list=[]
for j in list1:
    stop_words_list.append(j.lower())

with open(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\MasterDictionary\positive-words.txt','r') as file:
    content=file.read()
    text=re.sub('[\n]+',',',content)
    pos_words=re.findall('[+\w-]+',text)


with open(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\MasterDictionary\negative-words.txt','r') as file:
    content=file.read()
    text=re.sub('[\n]+',',',content)
    neg_words=re.findall('[\w-]+',text)

df=pd.read_csv(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\DataFrame\Articles.csv')
article=df['Article']

##    1) Tokenization
def tokenization(data):
    words=word_tokenize(data)
    return words

article_tokens=article.apply(tokenization)
# print(article_tokens)

##    2) Cleaning
def cleaning(data):
    clean_text=[i for i in data if i not in punctuation]
    return clean_text

article_clean=article_tokens.apply(cleaning)
# print(article_clean)

##    3) Normalization
def normalize(data):
    normal_text=[i.lower() for i in data]
    return normal_text

article_normal=article_clean.apply(normalize)
# print(article_normal)

##    4) Stop Words Removal
def stop_removal(data):
    stop_text=[i for i in data if i not in stop_words_list]
    return stop_text

article_domain_words=article_normal.apply(stop_removal)
# print(article_domain_words)

##    5) Join List
def string(data):
    strings=','.join(data)
    return strings

article_final=article_domain_words.apply(string)
# print(article_final)

positive_words_list=[]
negative_words_list=[]
for l in article_domain_words:
    positive_words=[m for m in l if m in pos_words]
    negative_words=[m for m in l if m in neg_words]
    pos_string=','.join(positive_words)
    neg_strings=','.join(negative_words)
    positive_words_list.append(pos_string)
    negative_words_list.append(neg_strings)

def clean_words(data):
    clean=[i for i in data if i not in punctuation]
    clean_words=','.join(clean)
    return clean_words

article_clean_words=article_tokens.apply(clean_words)

df['Positives']=positive_words_list
df['Negatives']=negative_words_list
df['Clean Words']=article_final
df['Words']=article_clean_words

df.to_csv(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\DataFrame\Articles_New.csv')