"""#s = {}         # ❌ This creates an empty dictionary
s = set()      # ✅ This creates an empty set"""

s = {1, 'Prakash', 3.5, (1,2,3), }

#print(1 in s)
 
 #Update--

s.add(5)

s.update({9,8})


# Delete--

s.discard(8)

val=s.pop()
print(s, val)


st1={8,4,5,2,3}

st2={9,1,4,6,7}



st2.intersection_update(st1)

print(st1)

print(st2)

#Remove all duplicates from the list using set.

lst=[2,3,4,8,7,2,3]
print(list(set(lst)))


#Find common elements between two lists.

lst=[2,3,4,8,7,]
lst2=[9,5,2,3,6]
com_ele=list(set(lst).intersection(set(lst2)))
print(com_ele)


#Check if two sets are disjoint.

st1={2,3,4,8,7}
st2={9,5,2,3,6}
print(st1.isdisjoint(st2))


#Create a set of even numbers from 1 to 10
set1={x for x in range(1,11)}
print(set1)