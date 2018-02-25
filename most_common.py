import nltk
import requests
from nltk import FreqDist
from nltk.book import *

fd = FreqDist(text7)

mc = fd.most_common(5)

print mc
