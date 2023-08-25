#adding a value in a list
list1=['apple','banana','cherry']
print(list1)
list1.append('orange')
print(list1)

#remove from a list
list2=[1,2,3,4,5]
list2.remove(3)
print(list2)

#inserting a value at the second position in a list
list3=['red','green','blue']
list3.insert(1,'yellow')
print(list3)

#occurance of a value in list
list4=['a','b','c','a','d']
item=list4.count('a')
print(item)

#to remove and return from the list
list5=[10,20,30,40,50]
item=list5.pop(4)
print(item)


#ascending order
list6=[4,1,7,3,9]
list6.sort()
print(list6)

#finding the index of a given list
list7=['New York', 'Los Angeles', 'Chicago','Houston']
item=list7.index('Chicago')
print(item)

#replaceing a value

list8=['dog', 'cat', 'elephant', 'lion']
list8[2]='tiger'
print(list8)


#counting a value

list9=[5, 2, 8, 2, 1]
item=list9.count(2)
print(item)

#removing and returning
list10=['apple', 'banana', 'cherry']
list10.reverse()
item=list10.pop()

print(item)
