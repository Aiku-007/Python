numbers=[10,20,30,40,50]
nums=[10,20]
aiko=[10,20,30,40,50]
print(len(numbers))
#for x in numbers:#traversing a list
    #print(x)
for i in range(len(numbers)):
        print(i,numbers[i])#values with index


nums.append(30)#append(): adds at the end
print(nums)

nums.insert(4,300)#insert(): insert at specific position
print(nums)

nums.remove(20)#remove(): removes by value
print(nums)

nums.pop(1)#pop(): removes by index
print(nums)

nums.pop()#pop() without index :removes last element

#Slicing list[start:end]
print(numbers[1:4]) #VIP (start:1 and end=4 are not included)

nums[:2]
print(nums)#first three elements

#membership operator
print(20 in aiko)#checks if value exists
#if not then 
print(299 in aiko)#returns false

#List concatenation 
a=[1,2]
b=[3,4]

c=a+b
print(c)

#Repetition
nums=[0]*5
print(nums)

#useful list methods sort()
aik=[1,5,3,5]
aik.sort()#for sorting
print(aik)

aik.reverse()#reversing the list
print(aik)

#count()
aik.count(1)

#index() returns the index of asked value
a=aiko.index(20)
print(a)

#list comprehension
#squares=[]
#for i in range(5):
#        squares.append(i*i)

        #in python we can do it in easy way
squares=[i*i for i in range(5)]
print(squares)





