# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 08:20:58 2019

@author: Chris
"""

import os
import re
import nltk
from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt

path = "C:\\Users\\Chris\\Desktop"
 
os.chdir(path)

words = open("CARES.txt" , 'r')
text = words.read()
words.close()

shortword = re.compile(r'\W*\b\w{1,3}\b')
text=shortword.sub('', text)
nltk.download('punkt')
from nltk import FreqDist
tokens = nltk.word_tokenize(text)
dist=FreqDist(tokens)

stopwords = set(STOPWORDS)

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=126000,
        max_font_size=40, #Was 40
        scale=3,
        random_state=1 # chosen at random by flipping a coin; it was heads
    ).generate(str(data))

    fig = plt.figure(1, figsize=(24, 24))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.savefig('BasicWordCloud.png')
    plt.show()
    
if __name__ == '__main__':
     
    show_wordcloud(text)
