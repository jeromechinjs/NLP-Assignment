#import library
import nltk
import pandas as pd    # redundant if run the above codes
import random

data = pd.read_csv('/content/Dataset/headphone_datn.csv')
nltk.download('state_union')
nltk.download('stopwords')

#download and read nltk library and csv file
data = pd.read_csv('/content/Dataset/headphone_datn.csv')
nltk.download('state_union')
nltk.download('stopwords')

# to check the total amout of data, and check any null value contained
data.head()
total = data.count()
print(total)

words = [w for w in nltk.corpus.state_union.words() if w.isalpha()] # list out all the individual words
stopwords = nltk.corpus.stopwords.words("english")
words = [w for w in words if w.lower() not in stopwords] # change all the capital letter to small letter

# tbc......