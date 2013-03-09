from collections import Counter

names=[name.strip() for name in open('names_noisy.txt','r').readlines()]
name_counter=Counter(names)
uniques=map(lambda wordset: wordset[0],name_counter.most_common(len(name_counter)/2))
print uniques
#for unique in sorted(uniques,key= lambda word : word.lower()): print unique
