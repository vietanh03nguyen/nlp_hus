from sklearn.model_selection import train_test_split
from src.models.text_classifier import TextClassifier
from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.representations.count_vectorizer import CountVectorizer

#Define dataset
texts = [
"This movie is fantastic and I love it!",
"I hate this film, it's terrible.",
"The acting was superb, a truly great experience.",
"What a waste of time, absolutely boring.",
"Highly recommend this, a masterpiece.",
"Could not finish watching, so bad."
]
labels = [1, 0, 1, 0, 1, 0] # 1 for positive, 0 for negative

#Split train-test
x_train,x_test,y_train,y_test = train_test_split(texts, labels, test_size=0.2)

#Instantiate RegexTokenizer and CountVectorizer instead of TfidfVectorizer
tokenizer = RegexTokenizer()
vectorizer = CountVectorizer(tokenizer)

#Instantiate TextClassifier with vectorizer
textClassifier = TextClassifier(vectorizer)

#Train the classifier
textClassifier.fit(x_train, y_train)

#Make predictions
y_pred = textClassifier.predict(x_test)
y_true = y_test

#Evaluate
print(textClassifier.evaluate(y_true, y_pred))


