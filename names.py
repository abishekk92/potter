import nltk
import os
book_1 = open(os.path.join("dataset","book_1.txt"),'r').read()
sentences=nltk.sent_tokenize(book_1)
sentences=[nltk.word_tokenize(sent) for sent in sentences]
sentences=[nltk.pos_tag(sent) for sent in sentences]
print sentences
