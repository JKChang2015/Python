# stemming
# Created by JKChang
# 2019-08-01, 10:29
# Tag:
# Description: test text stemming process
import time

from nltk.stem import WordNetLemmatizer

start_time = time.time()
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('newborns'))
print(time.time() - start_time)

s = time.time()
print(lemmatizer.lemmatize("bottles"))
print(time.time() - s)

# print(lemmatizer.lemmatize('children'))
# print(lemmatizer.lemmatize("bottles"))
# print(lemmatizer.lemmatize("DDS"))
