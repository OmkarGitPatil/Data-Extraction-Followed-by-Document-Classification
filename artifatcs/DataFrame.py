import pandas as pd
import numpy as np
import glob
import re

Directory=glob.glob(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\Text Files'+'\*.txt')
text_files_path=Directory[50:]+Directory[0:50]

text_list=[]

for k in text_files_path:
    with open(k,'r',encoding='utf-8') as file:
        content=file.read()
        text_list.append(content)

input=pd.read_excel(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\Input.xlsx')
df=pd.DataFrame({'URL_ID':input['URL_ID'][0:111],'Article':text_list})
df.to_csv(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\DataFrame\Articles.csv')
