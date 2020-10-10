# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 08:04:26 2019

@author: Chris
"""
import os
from os import path
import numpy as np
import matplotlib.pyplot as plt
import re
import nltk
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from wordcloud import WordCloud, ImageColorGenerator

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'nirvana.txt')).read()

shortword = re.compile(r'^')
#shortword = re.compile(r'\W*\b\w{1,2}\b')

text=shortword.sub('', text)
nltk.download('punkt')
from nltk import FreqDist
tokens = nltk.word_tokenize(text)
dist=FreqDist(tokens)

# read the mask / color image 
Image_coloring = np.array(Image.open(path.join(d, "Nirvana4.jpg")))
#stopwords = ['finger']
wc = WordCloud(background_color="white", 
               max_words=200000, 
               collocations = False,
               mask=Image_coloring, 
               max_font_size=100, 
               random_state=42)

#wc = WordCloud(background_color="white", max_words=126000, mask=Image_coloring,
#               stopwords=stopwords, max_font_size=1500, random_state=1)

plt.figure(figsize=(96, 96))#plt.figure(1, figsize=(96, 96))

# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(Image_coloring)

plt.title("Word Cloud")
plt.imshow(wc.recolor(color_func=image_colors, random_state=1),
           interpolation="bilinear")
plt.savefig('NirvanaTest.jpeg')
plt.show()





import nltk
from nltk.util import ngrams

def word_grams(words, min=3, max=4):
    s = []
    for n in range(min, max):
        for ngram in ngrams(words, n):
            s.append(' '.join(str(i) for i in ngram))
    return s

print(word_grams(text.split(' ')))





