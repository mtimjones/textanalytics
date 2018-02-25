import nltk
import requests
from nltk.tokenize import RegexpTokenizer

# Read the "Origin of Species"
r = requests.get("http://www.gutenberg.org/cache/epub/1228/pg1228.txt");

# Tokenize the text from the request
tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize( r.text )
unique_words = set( words )

# Find the 20 longest words
long_words = [ w for w in unique_words if len(w) > 16 ]

for i in long_words:
	print i
