import nltk
import requests
import random
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# Read the "Origin of Species"
r = requests.get("http://www.gutenberg.org/cache/epub/1228/pg1228.txt");

# Tokenize sentences from the text 
sent = sent_tokenize( r.text )

print len( sent )
print sent[random.randint(0,len(sent))]

# Tokenize words from the text
words = word_tokenize( r.text )

print len( words )
print words[ random.randint(0,len(words)) ]
