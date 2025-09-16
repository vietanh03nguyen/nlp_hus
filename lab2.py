from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.representations.count_vectorizer import CountVectorizer

if __name__ == "__main__":
    regex_tokenizer = RegexTokenizer()
    count_vectorizer = CountVectorizer(regex_tokenizer)
    corpus = [
    "I love NLP.",
    "I love programming.",
    "NLP is a subfield of AI."
    ]
    doc_mat = count_vectorizer.fit_transform(corpus)
    print(doc_mat)
    print(count_vectorizer.vocabulary_)