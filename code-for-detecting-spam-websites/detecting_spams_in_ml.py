import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the spam data
spam = pd.read_csv('spam.csv')

# Split the data into training and testing sets
X_train = spam.iloc[:4000, 1] # The message content
y_train = spam.iloc[:4000, 0] # Whether it is spam or not (1 for spam, 0 for not spam)
X_test = spam.iloc[4000:, 1]
y_test = spam.iloc[4000:, 0]

# Vectorize the text data
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

# Train the model using Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Predict on the testing set and print the accuracy
X_test_vectorized = vectorizer.transform(X_test)
accuracy = model.score(X_test_vectorized, y_test)
print('Accuracy:', accuracy)
