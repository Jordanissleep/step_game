from textblob import Textblob
with open('myText.txt', 'r') as f:
    text = f.read()
blob= TextBlob(text)
sentiment = blob.sentiment.polarity # -1
print (sentiment)