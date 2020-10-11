# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 20:46:35 2020

@author: Chris
"""

import os
from os import path
import numpy as np
import matplotlib.pyplot as plt
import re
import nltk
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
nltk.download('punkt')
from nltk import FreqDist

def word_cloud(text, image_ref, max_font_size, background_color, image_out):
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    
	# Read the whole text.
    text = open(path.join(d, text)).read()
	
	# remove shortwords
    #shortword = re.compile(r'^')
    #text=shortword.sub('', text)
	
	# do frequency distribution of unique words
    tokens = nltk.word_tokenize(text)
    dist=FreqDist(text)
	
    # read the mask / color image 
    Image_coloring = np.array(Image.open(path.join(d, image_ref)))
    wc = WordCloud(background_color=background_color, 
                   max_words=200000, 
                   collocations = False,
                   mask=Image_coloring, 
                   max_font_size=max_font_size, 
                   random_state=42)

    plt.figure(figsize=(96, 96))

	# generate word cloud
    wc.generate(text)

	# create coloring from image
    image_colors = ImageColorGenerator(Image_coloring)

    plt.title("Word Cloud")
    plt.imshow(wc.recolor(color_func=image_colors, random_state=1),
               interpolation="bilinear")
    plt.savefig(image_out)
    plt.show()

word_cloud('VH-After1984.txt', 'guitarBlack.jpg', 200, 'white', 'gA1984.jpeg')