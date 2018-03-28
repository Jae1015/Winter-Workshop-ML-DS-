import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

data = pd.read_csv('@SrBachchan.csv')
a = data.length
b = data.no_hashtags
c = data.no_men
d = data.likes
e = data.retweets
f = data.sentiment_polarity
h = data.time

foo = 1500
bar = 1500

foo1 = 28 + 4*np.random.randn(foo)
bar1 = 24 + 4*np.random.randn(bar)

plt.hist([foo1, bar1], stacked =False, color=['r','b'])
#Stacked: Refers to the presence of the two features getting plotted one over the other or sidewise.
plt.show()
