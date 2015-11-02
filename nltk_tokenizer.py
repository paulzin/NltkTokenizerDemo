import nltk
from nltk.tokenize import WordPunctTokenizer

# Demo strings
sentences_string = "Bros! Big night! I'm gonna be on The Late Show with Stephen Colbert!!! " \
                   "Tonight at 11:35/10:35c on CBS. DONT MISS, WOOOOOOH"
words_string = "Dropbox's answer to Google Docs' collaborative document editing is called Paper"


def tokenize_sentences(text):
    """
    :param text:
    :return: list of sentences in text
    """
    return nltk.sent_tokenize(text)


def tokenize_words(sentence):
    """
    :param sentence:
    :return: list of words in sentence
    """
    tokenizer = WordPunctTokenizer()
    return tokenizer.tokenize(sentence)


def demo():
    print("Tokenizing sentences:")
    print(tokenize_sentences(sentences_string))
    print("\nTokenizing words:")
    print(tokenize_words(words_string))


demo()
