from collections import Counter
import re
names=[name.strip() for name in open('names_noisy.txt','r').readlines()]
name_counter=Counter(names)
uniques=sorted(map(lambda wordset: re.sub(r'Mr.',' ',wordset[0]),name_counter.most_common(len(name_counter)/2)),key=lambda word: len(word))
index=0
def normalize(uniques,index):
	pattern=re.compile(uniques[index])
	try:
		if index != len(uniques)-1:
			to_remove=filter(pattern.match,uniques)
			map(lambda key : uniques.remove(key),to_remove[1::])
			return normalize(uniques,index+1)
		else :
			return uniques
	except:
		pass
print normalize(uniques,index)

#for unique in sorted(uniques,key= lambda word : word.lower()): print unique
