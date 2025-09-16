from src.preprocessing.simple_tokenizer import SimpleTokenizer
from src.preprocessing.regex_tokenizer import RegexTokenizer

if __name__ == "__main__":
    txt1 = "Hello, world! This is a test."
    txt2 = "NLP is fascinating... isn't it?"
    txt3 = "Let's see how it handles 123 numbers and punctuation!"
    
    simple_tokenizer = SimpleTokenizer()
    regex_tokenizer = RegexTokenizer()
    
    
    print("simple tokenizer txt1:", simple_tokenizer.tokenize(txt1))
    print("simple tokenizer txt1:", simple_tokenizer.tokenize(txt2))
    print("simple tokenizer txt1:", simple_tokenizer.tokenize(txt3))
    
    print("simple tokenizer txt1:", regex_tokenizer.tokenize(txt1))
    print("simple tokenizer txt1:", regex_tokenizer.tokenize(txt2))
    print("simple tokenizer txt1:", regex_tokenizer.tokenize(txt3))