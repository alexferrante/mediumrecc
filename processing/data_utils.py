import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
 
def clean_data(df, verbose=False, write=False):
  if verbose:
def remove_non_ascii(text):
    return text.encode("ascii", errors="ignore").decode()

def to_lowercase(tokenized_text):
    return ' '.join([word.lower() for text)])

def remove_numbers(text):
    return ''.join(c for c in text if not c.isdigit())

def remove_punctuation(text):
    return ''.join(c for c in text if c not in punctuation)

def w_tokenize(text):
    return nltk.word_tokenize(text)

def remove_stop_words(tokenized_text):
    stopword = stopwords.words('english')
    tokens_without_sw = [word for word in word_tokens if word not in stopword]
    return tokens_without_sw

def lemmatization(tokenized_text):
  lemmatizer = WordNetLemmatizer()
  for word in tokenized_text:
    lemmatizer.lemmatize(word)
