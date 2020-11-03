from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "Das Wetter ist schoen und es ist sonnig",
    "Sonniges Wetter ist schoen",
    "Sobald das Wetter schoen ist gehen wir schwimmen"
]

vectorizer = CountVectorizer()
transformed = vectorizer.fit_transform(corpus)

print(transformed.todense())
print(vectorizer.get_feature_names())
print(vectorizer.vocabulary_)
