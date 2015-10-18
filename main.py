import nltk
from nltk.tokenize import WordPunctTokenizer

# Tokenizing sentences
sentences_string = "Bros! Big night! I'm gonna be on The Late Show with Stephen Colbert!!! " \
                   "Tonight at 11:35/10:35c on CBS. DONT MISS, WOOOOOOH"
sentence_tokens = nltk.sent_tokenize(sentences_string)
for sentence in sentence_tokens:
    print(sentence)
print()

# Tokenizing words
words_string = "Dropbox's answer to Google Docs' collaborative document editing is called Paper"
word_tokens = nltk.word_tokenize(words_string)
for word in word_tokens:
    print(word)
print()


words_with_contraction = "I can't do that"
word_tokens = nltk.word_tokenize(words_with_contraction)
for word in word_tokens:
    print(word)
print()

tokenizer = WordPunctTokenizer()
tokens = tokenizer.tokenize(words_with_contraction)
for word in tokens:
    print(word)
