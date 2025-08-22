from flask import Flask, render_template, request
import pickle
import re
import string

app = Flask(__name__)

# Load saved TF-IDF vectorizer
with open("models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load trained sentiment analysis model
with open("models/sentiment_rf_model.pkl", "rb") as f:
    model = pickle.load(f)

# Function to clean input text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)          # Remove links
    text = re.sub(r"@\w+", "", text)             # Remove mentions
    text = re.sub(r"#\w+", "", text)             # Remove hashtags
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)  # Remove punctuation
    text = re.sub(r"\d+", "", text)              # Remove numbers
    return text

# Mapping predicted labels to text
label_map = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}

# Main route
@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    user_input = ""
    if request.method == "POST":
        user_input = request.form["tweet"]      # Get input
        cleaned = clean_text(user_input)        # Clean text
        vec = vectorizer.transform([cleaned])   # Vectorize
        prediction = model.predict(vec)[0]      # Predict sentiment
        sentiment = label_map[prediction]       # Map to label
    return render_template("index.html", sentiment=sentiment, user_input=user_input)

# Run app
if __name__ == "__main__":
    app.run(debug=True)
