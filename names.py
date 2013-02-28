import nltk
import os
book_1 = open(os.path.join("dataset","book_1.txt"),'r').read()
sentences=nltk.sent_tokenize(book_1)
sentences=[nltk.word_tokenize(sent) for sent in sentences]
sentences=[nltk.pos_tag(sent) for sent in sentences]
chunked=[nltk.ne_chunk(sent) for sent in sentences]
for chunk in chunked:
	if hasattr(chunk,'node'):		
		if chunk.node == 'PERSON':
			name=' '.join(leave[0] for leave in chunk.leaves())
			print name
	else:
		print "Nope"
