import nltk
import requests
import random
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Read the "Origin of Species"
r = requests.get("http://www.gutenberg.org/cache/epub/1228/pg1228.txt");

# Tokenize sentences from the text 
sents = sent_tokenize( r.text )

sent = sents[ random.randint(0,len(sents)) ]

print sent

words = word_tokenize( sent )

tagged = pos_tag( words )

print tagged
