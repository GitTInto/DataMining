#Analyzing text for whether comments are positive or negative

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

Addr1 = './week-4/DailyComments.csv'
dataframe = pd.read_csv(Addr1)
print(dataframe)
corpus = dataframe['comments']

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print("")
print("vectorized words")
print("")
print(vectorizer.get_feature_names())
print("")
print("Identify Feature Words - Matrix View")
print("")
print(X.toarray())

df = pd.DataFrame({'text' : corpus})

#check for positive words and negative words
df['positive1'] = df.text.str.count('good')
df['positive2']= df.text.str.count('special')
df['negative'] = df.text.str.count('bad')
df['TotScore'] = df.positive1 + df.positive2 - df.negative

print("")
print(df)

Z = sum(df['TotScore'])
print("")
print("Overall Score:  ",Z)

