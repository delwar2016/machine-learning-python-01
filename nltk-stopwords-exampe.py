from  nltk.corpus import stopwords
stop = set(stopwords.words('english'))
sentence = "this is a foo bar sentence"
print [i for i in sentence.lower().split() if i not in stop]