import nltk
import requests
import random
from nltk.tokenize import word_tokenize

def CreateTuples( words ):
   tuples = []

   for i in range( len(words)-1 ):
      tuples.append( (words[i], words[i+1]) )

   return tuples

# Iterate the bigrams and construct a sentence until a '.' is encountered.
def EmitSentence( cfd ):
   word = u'I'
   sentence = []
   sentence.append(word)

   while word != '.':
      options = []
      for gram in cfd[word]:
         for result in range(cfd[word][gram]):
            options.append(gram)

      word = options[int((len(options))*random.random())]
      sentence.append( word )

   print sentence


# Read the "Origin of Species"
r = requests.get("http://www.gutenberg.org/cache/epub/1228/pg1228.txt");

# Tokenize words from the text 
tokens = word_tokenize( r.text )

# Create the bigram word tuples
tuples = CreateTuples( tokens )

# Create a conditional frequency distribution based upon the tuples
cfd = nltk.ConditionalFreqDist( tuples )

# Emit a random sentence based upon the corpus
EmitSentence( cfd )
