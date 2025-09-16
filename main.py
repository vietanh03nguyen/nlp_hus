from src.preprocessing.simple_tokenizer import SimpleTokenizer

if __name__ == "__main__":
    txt1 = "Hello, world! This is a test."
    txt2 = "NLP is fascinating... isn't it?"
    txt3 = "Let's see how it handles 123 numbers and punctuation!"
    
    simple_tokenizer = SimpleTokenizer()
    
    print("simple tokenizer txt1:", simple_tokenizer.tokenize(txt1))