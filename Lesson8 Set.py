sample_list=[1,1,2,2,3,3]
sample_set=set(sample_list)
print(sample_set)
#Sets are not indexable
#print(sample_set[2])
if 4 in sample_set:
    print("Yes")
else:
    print("No")

myset=set([])
myset.add(3)
myset.add(4)
myset.add(4)
myset.add(2)
myset.add(1)
print(myset)

myset.remove(2)
#throws an error if element is not present, otherwise no error
print(myset)
myset.discard(5) #does not throw an error even if element is not present
print(myset)

#union
a={1,2,3,4,5}
b={5,6,7,8,9}
print(a.union(b))
print(a|b)

#Intersection
print(a.intersection(b))
print(a&b)

#difference

print(a.difference(b))
print(a-b)

#symmetric difference
print(a.symmetric_difference(b))
print(a^b)