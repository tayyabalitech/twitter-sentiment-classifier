# Twitter Sentiment Classifier

[![Python](https://img.shields.io/badge/Python-blue)](https://www.python.org) [![Flask](https://img.shields.io/badge/Flask-green)](https://flask.palletsprojects.com) [![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-orange)](https://scikit-learn.org/stable/modules/ensemble.html#random-forests)

---

## Overview

The Twitter Sentiment Classifier is a machine learning-based web application built using Python, Flask, and scikit-learn. It analyzes tweets and predicts their sentiment as Positive, Negative, or Neutral. This project leverages TF-IDF vectorization for text representation and a Random Forest Classifier for sentiment prediction.

The project is designed with clean UIUX using HTML and CSS to make sentiment analysis interactive and visually appealing.

---

## Features

 Predict Tweet Sentiment Enter any tweet to determine if it is Positive, Negative, or Neutral.
 Clean UI Beautiful, responsive interface for easy interaction.
 Pre-trained Models Includes a ready-to-use Random Forest model and TF-IDF vectorizer.
 Data Preprocessing Handles cleaning, stopword removal, and text normalization.
 Visual Feedback Displays sentiment in colored badges for clear distinction.

---

## Directory Structure

```
twitter-sentiment-classifier
│
├── models
│   ├── sentiment_rf_model.pkl       # Pre-trained Random Forest model (not included in repo due to size; see notebook to generate)
│   └── tfidf_vectorizer.pkl         # TF-IDF vectorizer
│
├── data
│   └── twitter_training.csv         # Dataset for training the model
│
├── static
│   └── style.css                    # Styling for the web app
│
├── templates
│   └── index.html                   # Main HTML template
│
├── app.py                           # Flask web application
├── notebook.ipynb                    # Jupyter notebook for training & evaluation
└── requirements.txt                  # Python dependencies
```

---

## Installation

1. Clone the repository

```bash
git clone httpsgithub.comtayyabalitechtwitter-sentiment-classifier.git
cd twitter-sentiment-classifier
```

2. Create a virtual environment (optional but recommended)

 For Linux/macOS

```bash
python -m venv venv
source venvbinactivate
```

 For Windows

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

1. Run the Flask app

```bash
python app.py
```

2. Open your browser and go to `http127.0.0.15000`.

3. Enter a tweet in the text area and click Predict Sentiment.

4. View the result displayed as a colored badge indicating Positive, Neutral, or Negative sentiment.

5. Use Clear button to reset the input.

---

## Technologies Used

- **Python 3** – Programming language used for backend and ML model  
- **Flask** – Web framework for serving the application  
- **scikit-learn** – Machine learning library for training the Random Forest model  
- **pandas** and **numpy** – Data manipulation and numerical computation  
- **NLTK** – Natural language processing (text cleaning and preprocessing)  
- **matplotlib** and **seaborn** – Data visualization  
- **HTML & CSS** – Frontend design for clean and responsive UI

---

## Preprocessing & Model

1. Text Cleaning Lowercasing, removing URLs, mentions, hashtags, punctuation, numbers, and stopwords.
2. Vectorization TF-IDF to convert text into numerical features.
3. Model Random Forest Classifier trained on labeled tweets.
4. Evaluation Accuracy, classification report, and confusion matrix.

---

## Sentiment Mapping

 Label  Sentiment 
 -----  --------- 
 0      Negative  
 1      Neutral   
 2      Positive  

Badges are styled using CSS for immediate visual feedback

 Positive Teal
 Neutral Amber
 Negative Coral Red

---

## 📧 Contact

For questions, suggestions, or collaborations, feel free to reach out


GitHub: [tayyabalitech](https://github.com/tayyabalitech)  
LinkedIn: [tayyabalitech](https://www.linkedin.com/in/tayyabalitech)  
Email: [tayyabalitechpro@gmail.com](mailto:tayyabalitechpro@gmail.com)

## Made with ❤️ by Tayyab Ali
