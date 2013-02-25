from pattern.vector import Corpus
import os,sys; sys.path.insert(0,os.path.join("..",".."))

corpus=Corpus.build(os.path.join("dataset","*.txt"), name=lambda path: os.path.basename(path)[:6])
book_1=corpus.document(name="book_1")
print book_1.keywords(top=50)

