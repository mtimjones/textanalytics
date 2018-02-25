import nltk
import requests
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Read the "Origin of Species"
r = requests.get("http://www.gutenberg.org/cache/epub/1228/pg1228.txt");

# Tokenize sentences from the text 
sent = sent_tokenize( r.text )

print sent[353]

words = word_tokenize( sent[353] )

tagged = pos_tag( words )

print tagged
