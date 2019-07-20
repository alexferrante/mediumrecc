import re
import nltk
from nltk.corpus import stopwords
from string import punctuation
from symspellpy.symspellpy import SymSpell 

def main(text):
    remove_non_ascii(text)
    remove_punctuation(text)
    remove_numbers(text)
    text = w_tokenize(text)
    to_lowercase(text)
    remove_stop_words(text)
   
def remove_non_ascii(text):
    return text.encode("ascii", errors="ignore").decode()

def remove_numbers(text):
    return ''.join(c for c in text if not c.isdigit())

def remove_punctuation(text):
    return ''.join(c for c in text if c not in punctuation)

def w_tokenize(text):
    return nltk.word_tokenize(text);

def remove_stop_words(tokenized_text):
    stopword = stopwords.words('english')
    tokens_without_sw = [word for word in word_tokens if word not in stopword]
    return tokens_without_sw

def to_lowercase(tokenized_text):
    return ' '.join([word.lower() for text)])
 