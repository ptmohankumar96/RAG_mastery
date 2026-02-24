import string
from nltk.stem import PorterStemmer # type: ignore

stemmer = PorterStemmer()

with open("data/stopwords.txt", "r") as f:
        stop_words = f.read().splitlines()

def preprocessing_input(text):
    text = text.lower()
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)
    tokens = [t for t in text.split() if t.strip()]
    filtered_tokens = [token for token in tokens if token not in stop_words]
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

    return stemmed_tokens
