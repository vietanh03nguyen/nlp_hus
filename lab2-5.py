from src.preprocessing.simple_tokenizer import SimpleTokenizer
from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.core.dataset_loaders import load_raw_text_data
from src.representations.count_vectorizer import CountVectorizer

if __name__ == "__main__":
    regex_tokenizer = RegexTokenizer()
    simple_tokenizer = SimpleTokenizer()
    count_vectorizer = CountVectorizer(simple_tokenizer)
    
    path = "data/c4_30k/c4-train.00000-of-01024-30K.json"
    
    corpus = load_raw_text_data(path)
    
    sample_corpus = corpus[1:100000]
    
    doc_mat = count_vectorizer.fit_transform(sample_corpus)
    # print("doc1 = ",doc_mat[0])
    # print("doc2 = ",doc_mat[1])
    # print("doc3 = ",doc_mat[2])
    # print(sample_corpus)
    

    print(len(count_vectorizer.vocabulary_))
    print(count_vectorizer.vocabulary_)