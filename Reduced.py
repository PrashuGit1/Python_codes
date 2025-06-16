import functools

#use of the mathmatics opeartions

"""numbers = [1, 2, 3, 4]
product=functools.reduce(lambda x,y:x*y,numbers)
print(product)"""

#use of the concrit string

"""lst=['Python', 'is', 'osm']
result=functools.reduce(lambda x,y: x+' '+y,lst)
print(result)"""

# Use of the Flatten a list of lists

lists = [[1, 2], [3, 4], [5, 6]]
result=functools.reduce(lambda x,y : x+y, lists)

print(type(result),result)
