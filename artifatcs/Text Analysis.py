import numpy as np
import pandas as pd
import re

## Calling rough .csv file from DataFrame folder to compute variables

df=pd.read_csv(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\DataFrame\Articles_New.csv')  


Positive_Score=[]
Negative_Score=[]
for i in range(0,len(df)):
    if type(df['Positives'][i:i+1][i])==float:
        Positive_Score.append(0)
    else:
        p_score=len(df['Positives'][i:i+1][i].split(','))
        Positive_Score.append(p_score)

    if type(df['Negatives'][i:i+1][i])==float:
        Negative_Score.append(0)
    else:
        n_score=len(df['Negatives'][i:i+1][i].split(','))
        Negative_Score.append(n_score)


df['Positive_Score']=Positive_Score
df['Negative_Score']=Negative_Score


Polarity_Score=[]
Subjectivity_Score=[]

for j in range(0,len(df)):
    pola=(df['Positive_Score'][j:j+1][j]-df['Negative_Score'][j:j+1][j])/((df['Positive_Score'][j:j+1][j]+df['Negative_Score'][j:j+1][j])+0.000001)
    Polarity_Score.append(pola)

    subj=(df['Positive_Score'][j:j+1][j]+df['Negative_Score'][j:j+1][j])/((len(df['Clean Words'][j:j+1][j].split(',')))+0.000001)
    Subjectivity_Score.append(subj)

df['Polarity_Score']=Polarity_Score
df['Subjectivity_Score']=Subjectivity_Score


Average_Sentence_Length=[]
for k in range(0,len(df)):
    length=len(df['Words'][k:k+1][k].split(','))/len(df['Article'][k:k+1][k].split('.'))
    Average_Sentence_Length.append(length)

df['Average_Sentence_Length']=Average_Sentence_Length

Complex_Word_Count=[]
Percentage_of_Complex_Words=[]
Syllable_Count_Per_Word=[]
for l in range(0,len(df)):

    complex=[]
    start=0
    syllable_count=[]

    for k in df['Words'][l:l+1][l].split(','):
        count=0
        syllable=[]
        vowels=['a','e','i','o','u']
        list1=list(k)

        for m in list1:
            if (m in vowels) and (k[len(k):len(k)-3:-1] not in ['se','de']):
                syllable.append(list1.count(m))

                if m=='a':
                    count=count+1
                elif m=='e':
                    count=count+1
                elif m=='i':
                    count=count+1
                elif m=='o':
                    count=count+1
                elif m=='u':
                    count=count+1

                while (list1.count(m)):
                    list1.remove(m)

        if count > 2:
            start+=1
            complex.append(start)
        
        syllable_count.extend(syllable)

    if start < 1:
        complex.append(0)
    
    comlex_words_ratio=len(complex)/len(df['Words'][l:l+1][l].split(','))
    Percentage_of_Complex_Words.append(comlex_words_ratio)
    Complex_Word_Count.append(len(complex))
    Syllable_Count_Per_Word.append(np.round(sum(syllable_count)/len(df['Words'][l:l+1][l].split(','))))

df['Percentage_of_Complex_Words'] =Percentage_of_Complex_Words

df['Fog_Index']=0.4*(df['Average_Sentence_Length']+df['Percentage_of_Complex_Words'])

df['Complex_Word_Count']=Complex_Word_Count


Word_Count=[]
for n in range(0,len(df)):
    Word_Count.append(len(df['Clean Words'][n:n+1][n].split(',')))

df['Word_Count']=Word_Count
df['Syllable_Count_Per_Word']=Syllable_Count_Per_Word


Personal_Pronoun=[]
for o in range(0,len(df)):
    list2=df['Words'][o:o+1][o].split(',')
    add=0
    for p in list2:
        if p in ['I','we','us','my','ours']:
            count=list2.count(p)
            while (list2.count(p)):
                list2.remove(p)
            add=count+add
    Personal_Pronoun.append(add)

df['Personal_Pronoun']=Personal_Pronoun

Average_Word_Length=[]
for q in range(0,len(df)):
    count=0
    for r in df['Article'][q:q+1][q]:
        if r not in [',','.',' ','"','?','!']:
            count+=1
    Average_Word_Length.append(count/len(df['Words'][q:q+1][q].split(',')))

df['Average_Word_Length']=Average_Word_Length

df_input=pd.read_excel(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\Input.xlsx')

df.insert(2,'URL',df_input['URL'])
df.drop(['Unnamed: 0','Article','Positives','Negatives','Clean Words','Words','URL_ID'],axis=1,inplace=True)
df.insert(1,'URL_ID',df_input['URL_ID'])
df.to_csv(r'C:\Users\Omkar\Desktop\Practice\Datasets\Document Classification\Solution\Output Solution.csv',index=False)