# Sentiment Analysis Tool

## Project Description

This project implements a **Sentiment Analysis Tool** using Machine Learning. It loads labeled text data from a CSV dataset, preprocesses the text by cleaning and tokenizing it, converts the text into numerical features using **TF-IDF**, trains a **Multinomial Naive Bayes** classifier, evaluates the model using **Accuracy** and **F1 Score**, and provides an interactive Command-Line Interface (CLI) to predict the sentiment of user-entered text.

---

## Features

- Load labeled text data from a CSV dataset
- Text preprocessing (cleaning and tokenization)
- Feature extraction using TF-IDF
- Train a Machine Learning classifier
- Evaluate model performance using Accuracy and F1 Score
- Interactive Command-Line Interface (CLI)
- Predict Positive and Negative sentiments
- Easy to extend with larger datasets

---

## Project Requirements Covered

- Load labeled text data (reviews/tweets)
- Preprocess text (clean and tokenize)
- Convert text into numerical features using TF-IDF
- Train a classifier using Multinomial Naive Bayes
- Evaluate the model using Accuracy and F1 Score
- Provide a CLI for sentiment prediction

---

## Project Structure

```text
Sentiment_Analysis_Tool
│
├── dataset.csv
├── main.py
├── README.md
└── requirements.txt
```

---

## Machine Learning Pipeline

```text
dataset.csv
      │
      ▼
Load Dataset
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
CLI Prediction
```

---

## Example Execution

```text
==================================================
        SENTIMENT ANALYSIS TOOL
==================================================

Accuracy : 100.00%
F1 Score : 100.00%

Type 'exit' to quit.

Enter a review:
I love this product

Predicted Sentiment:
Positive

Type 'exit' to quit.

Enter a review:
The service was terrible

Predicted Sentiment:
Negative

Type 'exit' to quit.

Enter a review:
exit

Thank you for using the Sentiment Analysis Tool.
```

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- Machine Learning

---

## Requirements

- Python 3.10 or above
- pandas
- scikit-learn

Install the required packages using:

```bash
pip install -r requirements.txt
```

---

## Learning Outcomes

- Data preprocessing for text
- Text feature extraction using TF-IDF
- Sentiment classification using Machine Learning
- Model training and evaluation
- Measuring Accuracy and F1 Score
- Building an interactive CLI application

---

## Future Improvements

- Add support for Neutral sentiment
- Train on larger real-world datasets
- Use Logistic Regression for comparison
- Develop a GUI using Streamlit or Tkinter
- Integrate real-time sentiment analysis for social media data

---

## Author

Manan
