from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = [
    "buy cheap offer now",
    "limited time offer",
    "buy medicines online",
    "let's have lunch tomorrow",
    "project meeting schedule",
    "can we buy groceries"
]

labels = ["spam", "spam", "spam", "ham", "ham", "ham"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

nb = MultinomialNB()
nb.fit(X, labels)

test_emails = [
    "buy cheap offer now",
    "today I have meeting"
]

X_test = vectorizer.transform(test_emails)
predictions = nb.predict(X_test)

for email, pred in zip(test_emails, predictions):
    print(f"Email: '{email}'  -> Prediction: {pred}")
