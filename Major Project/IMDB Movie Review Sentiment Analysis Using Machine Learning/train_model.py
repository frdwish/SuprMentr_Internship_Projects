from pathlib import Path
import re

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = Path("/Users/frdwish/Desktop/IMDB Dataset.csv")
MODEL_DIR = BASE_DIR / "model"
MODEL_PATH = MODEL_DIR / "sentiment_model.pkl"
SAMPLE_SIZE = 10000


def clean_text(text: str) -> str:
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def load_imdb_dataset(data_path: Path = DATA_PATH, sample_size: int = SAMPLE_SIZE) -> pd.DataFrame:
    dataset = pd.read_csv(data_path)
    dataset = dataset[["review", "sentiment"]].dropna()

    if sample_size and sample_size < len(dataset):
        positive_reviews = dataset[dataset["sentiment"] == "positive"].sample(
            n=sample_size // 2, random_state=42
        )
        negative_reviews = dataset[dataset["sentiment"] == "negative"].sample(
            n=sample_size // 2, random_state=42
        )
        dataset = pd.concat([positive_reviews, negative_reviews], ignore_index=True).sample(
            frac=1, random_state=42
        )

    dataset["review"] = dataset["review"].astype(str).map(clean_text)
    return dataset


def train_and_save_model() -> dict:
    dataset = load_imdb_dataset()

    x_train, x_test, y_train, y_test = train_test_split(
        dataset["review"],
        dataset["sentiment"],
        test_size=0.25,
        random_state=42,
        stratify=dataset["sentiment"],
    )

    model = Pipeline(
        steps=[
            ("vectorizer", TfidfVectorizer(stop_words="english", max_features=15000, ngram_range=(1, 2))),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    return {
        "accuracy": accuracy_score(y_test, predictions),
        "report": classification_report(y_test, predictions, zero_division=0),
        "saved_model": str(MODEL_PATH),
        "dataset_size": len(dataset),
    }


if __name__ == "__main__":
    results = train_and_save_model()
    print(f"Model saved to: {results['saved_model']}")
    print(f"Dataset samples used: {results['dataset_size']}")
    print(f"Accuracy: {results['accuracy']:.2f}")
    print("Classification Report:")
    print(results["report"])
