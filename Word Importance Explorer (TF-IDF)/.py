from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "AI is transforming the world",
    "Machine learning is part of AI",
    "Python is used in AI",
    "Data science uses ML",
    "AI helps automation"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

features = vectorizer.get_feature_names_out()

for i, row in enumerate(X.toarray()):
    print(f"\nDoc {i+1}:")
    words = sorted(zip(features, row), key=lambda x: x[1], reverse=True)
    for w, s in words[:3]:
        print(w, round(s, 2))