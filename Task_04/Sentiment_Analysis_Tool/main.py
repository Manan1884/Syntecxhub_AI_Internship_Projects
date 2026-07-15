import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, f1_score

data = pd.read_csv("dataset.csv")


def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    return " ".join(words)


data["text"] = data["text"].apply(preprocess)


vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(data["text"])

y = data["sentiment"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = MultinomialNB()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

f1 = f1_score(
    y_test,
    predictions,
    pos_label="Positive"
)

print("=" * 50)
print("      SENTIMENT ANALYSIS TOOL")
print("=" * 50)

print(f"\nAccuracy : {accuracy * 100:.2f}%")
print(f"F1 Score : {f1 * 100:.2f}%")

while True:

    print("\nType 'exit' to quit.")

    user_input = input("\nEnter a review: ")

    if user_input.lower() == "exit":
        print("\nThank you for using the Sentiment Analysis Tool.")
        break

    cleaned_text = preprocess(user_input)

    vector = vectorizer.transform([cleaned_text])

    prediction = model.predict(vector)[0]

    print("\nPredicted Sentiment:", prediction)