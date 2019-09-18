import string

def is_pangram(sentence):
    # Alphabet
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    
    # Lower case
    sentence = sentence.lower()
    # List of sorted letters
    sentence_sorted = sorted(sentence)
    # List of unique sorted letters
    sentence_unique_letters = list(set(sentence_sorted))
    # Strip punctuation and white space
    chars_no_punc = [letter for letter in sentence_unique_letters if letter not in string.punctuation]
    chars_no_punc_no_space = [letter for letter in chars_no_punc if letter != " "]
    chars_no_punc_no_space.sort()
    
    # The output here should be the list of unique letters, excluding spaces and punctuation
    is_pangram = alphabet == chars_no_punc_no_space
    
    return(is_pangram)
