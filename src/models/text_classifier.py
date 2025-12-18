from src.core.interfaces import Vectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class TextClassifier:
    def __init__(self, vectorizer: Vectorizer):
        self.vectorizer = vectorizer
        self._model = None
        
    def fit(self, texts, labels):
        
        X = self.vectorizer.fit_transform(texts)
        self._model = LogisticRegression(solver = 'liblinear')
        self._model.fit(X, labels)
    
    def predict(self, texts):
        X = self.vectorizer.transform(texts)
        return self._model.predict(X)
    
    def evaluate(self, y_true, y_pred):
        metrics = {"accuracy": accuracy_score(y_true, y_pred),
                   "precision": precision_score(y_true, y_pred),
                   "recall": recall_score(y_true,y_pred),
                   "f1": f1_score(y_true,y_pred)}
        return metrics
        
        
    