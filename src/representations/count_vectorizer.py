from src.core.interfaces import Vectorizer, Tokenizer

class CountVectorizer(Vectorizer):
    def __init__(self, tokenizer: Tokenizer):
        self._tokenizer = tokenizer
        self.vocabulary_: dict[str, int] = {}
    
    def fit(self, corpus: list[str]):
        tokens_set = set()
        for doc in corpus:
            tokenized = self._tokenizer.tokenize(doc)
            for token in tokenized:
                tokens_set.add(token)
        sorted_tokens = sorted(list(tokens_set))
        
        self.vocabulary_ = {token:i for i, token in enumerate(sorted_tokens)}
        
    def transform(self, corpus: list[str]):
        vector_list = []
        for doc in corpus:
            zero_vector = [0 for i in range(len(self.vocabulary_))]
            tokenized = self._tokenizer.tokenize(doc)
            for token in tokenized:
                if token in self.vocabulary_:
                    zero_vector[tokenized.index(token)] += 1
            vector_list.append(zero_vector)
        return vector_list
    
    def fit_transform(self, corpus):
        return super().fit_transform(corpus)
            
        
        
        