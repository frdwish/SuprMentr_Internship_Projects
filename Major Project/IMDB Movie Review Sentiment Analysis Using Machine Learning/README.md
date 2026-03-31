# Sentiment Analysis Tool

This project predicts whether a sentence or short review is **positive** or **negative** using a machine learning model.

## Why this project is good for an internship

- Easy to understand and explain
- Uses real NLP and machine learning concepts
- Has a clean live demo through a simple web app
- Can be extended later with a larger dataset

## Tech Stack

- Python
- pandas
- scikit-learn
- Streamlit
- joblib

## Project Structure

```text
sentiment-analysis-tool/
├── app.py
├── train_model.py
├── requirements.txt
├── data/
│   └── sentiment_data.csv
└── model/
    └── sentiment_model.pkl
```

## How to Run

1. Open a terminal in the project folder.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Train the model:

```bash
python train_model.py
```

4. Start the app:

```bash
streamlit run app.py
```

## How it Works

1. The dataset contains labeled text examples.
2. `TfidfVectorizer` converts text into numeric features.
3. `LogisticRegression` learns patterns from the labeled examples.
4. The trained model predicts whether new input text is positive or negative.

## Suggested Presentation Flow

1. Introduce the problem: understanding sentiment from text
2. Show the dataset format: text and label
3. Explain preprocessing and vectorization
4. Explain the machine learning model
5. Run the Streamlit app live and test a few example sentences

## Viva Questions You May Get

### What is sentiment analysis?

It is the process of identifying whether a text expresses a positive, negative, or neutral opinion.

### Why did you use TF-IDF?

TF-IDF converts text into numbers by measuring how important a word is in a sentence compared to the whole dataset.

### Why did you choose Logistic Regression?

It is simple, fast, and works well for basic text classification tasks.

### What are the limitations of this project?

- The dataset is small
- The model may not understand sarcasm or complex language
- Accuracy can improve with more real-world training data

## Future Improvements

- Add a neutral class
- Use a larger public dataset
- Try advanced models such as Naive Bayes or BERT
- Save prediction history in the app
