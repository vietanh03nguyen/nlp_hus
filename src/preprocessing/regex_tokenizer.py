from src.core.interfaces import Tokenizer
import re

class RegexTokenizer(Tokenizer):
    def tokenize(self, text):
        return re.findall("\w+|[^\w\s]", text) 