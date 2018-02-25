import nltk
import requests
from nltk import FreqDist
from nltk.book import *
from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))

fd = FreqDist(text7)

mc = fd.most_common(20)

words = [w for w in mc]

print words
