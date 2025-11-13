
#Implement Naive Bayes classifier in python using scikit learn to classify emails as spam or non spam based on their content.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Example emails
emails = [
    "win a free lottery",
    "free google subscription",
    "let's meet tomorrow",
    "project meeting schedule"
]

# Step 2: Labels → 1 = spam, 0 = not spam
Labels = [1, 1, 0, 0]

# Step 3: Convert words to numbers
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(emails)

# Step 4: Train the model
model = MultinomialNB()
model.fit(x, Labels)

# Step 5: Test with new email
test_email = ["free lottery for you"]
test_x = vectorizer.transform(test_email)

# Step 6: Predict
result = model.predict(test_x)

print("Prediction:", "Spam" if result[0] == 1 else "Not Spam")
