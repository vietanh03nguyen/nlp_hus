from src.preprocessing.simple_tokenizer import SimpleTokenizer
from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.core.dataset_loaders import load_raw_text_data


if __name__ == "__main__":
    txt1 = "Hello, world! This is a test."
    txt2 = "NLP is fascinating... isn't it?"
    txt3 = "Let's see how it handles 123 numbers and punctuation!"
    
    simple_tokenizer = SimpleTokenizer()
    regex_tokenizer = RegexTokenizer()
    
    
    print("simple tokenizer txt1:", simple_tokenizer.tokenize(txt1))
    print("simple tokenizer txt2:", simple_tokenizer.tokenize(txt2))
    print("simple tokenizer txt3:", simple_tokenizer.tokenize(txt3))
    
    print("simple tokenizer txt1:", regex_tokenizer.tokenize(txt1))
    print("simple tokenizer txt2:", regex_tokenizer.tokenize(txt2))
    print("simple tokenizer txt3:", regex_tokenizer.tokenize(txt3))
    
    path = "data/UD_English-EWT/en_ewt-ud-train.txt"
    raw_text = load_raw_text_data(path)
    sample_text = raw_text[:500]
    print("\n--- Tokenizing Sample Text from UD_English-EWT ---")
    print(f"Original Sample: {sample_text[:100]}...")
    simple_tokens = simple_tokenizer.tokenize(sample_text)
    print(f"SimpleTokenizer Output (first 20 tokens): {simple_tokens[:20]}")
    regex_tokens = regex_tokenizer.tokenize(sample_text)
    print(f"RegexTokenizer Output (first 20 tokens): {regex_tokens[:20]}")
    
    
    