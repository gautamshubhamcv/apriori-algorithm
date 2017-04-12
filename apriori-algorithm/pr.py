
all = []
with open('chess.dat') as f:
	for line in f:
		ha = line.split(" ")
		all.append(ha)

# print(len(all))

I1='I1'
I2='I2'
I3 = 'I3'
I4 = 'I4'
I5 = 'I5'
l1 = [I1, I2, I5]; l2=[I2, I4]
l3= [I2, I3];l4=[I1, I2, I4];l5=[I1, I3];l6=[I2, I3];l7=[I1, I3];l8=[I1, I2, I3, I5];l9=[I1, I2, I3]

list1 = [l1,l2,l3,l4,l5,l6,l7,l8,l9]


	#Generating Frequent Itemset from given dataset & min support 
def frSet(itemset,minSup):
	tab = {}
	frequent={}
	for items in itemset:
		for item in items:
			if item in tab:
				# Set = {item}
				tab[item] += 1
			else:
				tab[item] = 1
	for key,value in tab.items():
		if (value/len(itemset)>=minSup):
			a = frozenset({key})
			frequent[a] = value/len(itemset)
#	sorted_x = sorted(frequent.items(), key=operator.itemgetter(1))		 				
	return frequent
# print(frSet(all,3000/3196).items())


	     
#counts the frequency of items in itemset
def count(l,itemset):
	i = 0
	for items in itemset:
		if l.issubset(items):
			i = i+1
	return i

# print(count(frozenset({5}),[[2,4],[5,6],[5]]))
	     
def join(Set,length):
	output = set()
	for i in Set:
		for j in Set:
			if len(i.union(j))==length:
				output.add(i.union(j))
	return output

# print join()
# List = [[1],[2],[3],[4]]
# Set = set(map(frozenset, List))
# print(Set)
# print(join(Set,2))

def anyone(Set,ItemSet,minsup):
	b = False
	for items in Set:
		if (count(items,ItemSet)/len(ItemSet)>=minsup):
			b = True
			break
	return b

# print(anyone({frozenset({'56','40','34','36'}),frozenset({'56','40','34','36','45'})},all,2000))


def frequentItems(ItemSet,minsup):
	frItems = frSet(ItemSet,minsup)
	# print(frItems.items())
	fSet = set()
	for key,value in frItems.items():
		# a = frozenset([key]);
		# a.add(key);
		fSet.add(key)
	# print(fSet)
	length = 1;
	while anyone(fSet,ItemSet,minsup):
		length = length+1;
		fSet = join(fSet,length)
		tempSet = set()
		# print(fSet)
		for x in fSet:
			if (count(x,ItemSet)/len(ItemSet)>=minsup):
				frItems[x] = count(x,ItemSet)/len(ItemSet)
				tempSet.add(x)
		fSet = tempSet
		# print(fSet)
	# print(frItems.items())
	return frItems
	        
# frequentItems(all,.92)

def list_powerset(lst):
    # the power set of the empty set has one element, the empty set
	result = [[]]
	for x in lst:
		result.extend([subset + [x] for subset in result])
	return result
 
# print(list_powerset({1,2}))
 
def subsets(s):
	List = list_powerset(s)
	# print(type(List))
	# print(List)
	List.remove([])
	# List.remove(s)
	# print(List)
	return set(map(frozenset, List))

# print(subsets(frozenset({1,2})))

def ass_rules(Set,ItemSet,minconf):
	tupleSet=set()
	for x in subsets(Set):
		tuple = ()
		if (count(Set,ItemSet)/count(x,ItemSet)>=minconf):
			tuple = tuple+(x,Set.difference(x),count(Set,ItemSet)/count(x,ItemSet))
			tupleSet.add(tuple)
	tupleSet.remove((Set,frozenset(),1.0))
	return tupleSet

# print(ass_rules(frozenset({'I1','I2','I4'}),list,0.5))

def main(ItemSet,minsup,minconf):
	frItems = frequentItems(ItemSet,minsup)
	i = 1
	print("S.No","Items","Support",sep='   ')
	for key,value in frItems.items():
		print(i,list(key),value,sep=('  '))
		i = i+1
	# print(frItems.items())
	print()
	j = 1
	print("S.No","Item1","Item2","Confidence",sep='   ')
	for key,value in frItems.items():
		if (len(key)!=1):
			z = ass_rules(key,ItemSet,minconf)
			for x,y,w in z:
				print(j,list(x),list(y),w,sep=('   '))
				j=j+1

# main(list1,0.2,0.5)
main(all,0.95,0.7)






# fSet = {frozenset({'I1'}),frozenset({'I2'}),frozenset({'I3'})}
# print(anyone(fSet,list,8))
# print(join(fSet,2))
