import nltk
import os

output_file=open('names_noise.txt','w')
for i in xrange(1,8):
	book_name="book_%s.txt" %(str(i))
	book=open(os.path.join('dataset',"book_%s.txt" % (str(i)))).read()
	for sentences in nltk.sent_tokenize(book):
		for chunked in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentences))):
			if hasattr(chunked,'node'):
				if chunked.node == 'PERSON':
					name=' '.join(leaf[0] for leaf in chunked.leaves())
					output_file.write(name+"\n")
				
