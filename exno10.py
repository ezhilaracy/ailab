# AI Code Error Classifier using Naive Bayes 
 
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.naive_bayes import MultinomialNB 
from sklearn.model_selection import train_test_split 
 
# Step 1: Sample dataset (error message -> category) 
data = { 
    "text": [ 
        "SyntaxError: invalid syntax", 
        "IndentationError: unexpected indent", 
        "SyntaxError: unexpected EOF while parsing", 
        "ZeroDivisionError: division by zero", 
        "IndexError: list index out of range", 
        "NameError: name 'x' is not defined", 
        "TypeError: unsupported operand type", 
        "Output does not match expected result", 
        "Loop runs infinite times, wrong condition used", 
        "Wrong output due to incorrect formula used" 
    ], 
    "label": [ 
        "Syntax Error", "Syntax Error", "Syntax Error", 
        "Runtime Error", "Runtime Error", "Runtime Error", "Runtime Error", 
        "Logical Error", "Logical Error", "Logical Error" 
    ] 
} 
 
X_text = data["text"] 
y = data["label"] 
 
# Step 2: Convert text to feature vectors 
vectorizer = CountVectorizer() 
X = vectorizer.fit_transform(X_text) 
 
# Step 3: Train-test split 
X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size=0.3, random_state=42 
) 
 
# Step 4: Train Naive Bayes model 
model = MultinomialNB() 
model.fit(X_train, y_train) 
# Step 5: Test with a new error message 
def classify_error(error_message): 
vec = vectorizer.transform([error_message]) 
prediction = model.predict(vec) 
return prediction[0] 
# Step 6: Sample predictions 
test_errors = [ 
"SyntaxError: missing colon", 
"TypeError: cannot add str and int", 
"Output is incorrect due to wrong loop condition" 
] 
for err in test_errors: 
print(f"Error: '{err}'  -->  Predicted Category: {classify_error(err)}")
# Model accuracy on test split 
accuracy = model.score(X_test, y_test) 
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")