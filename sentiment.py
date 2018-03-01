import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys

def IdentifySentiment( sentence ):

   sia = SentimentIntensityAnalyzer()
   ps = sia.polarity_scores( sentence )

   for i in ps:
      print('{0}: {1}, '.format(i, ps[i]))


IdentifySentiment( sys.argv[1] )
