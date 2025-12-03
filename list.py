# fruits = ["orange", "mango", "banana", "malimao", "bamia"]
# print(fruits)


# #adding ane element
# fruits.insert(0, "chenza") 
# print(fruits)


# #removing the second element 
# fruits.pop(1)
# print(fruits)



#sort
numbers = [4,3,2,1,0]

#numbers.sort()
#print(numbers)
#print(numbers[4])

# num = input("enter ur number: ")
# numbers.append(num)
# print(numbers)

# numb = input("enter the number on the third: ")
# numbers.insert(2,numb)
# print(numbers)
numb = numbers[1]
numbers.remove(3)  #deletes by value, if string it could be the name z
print (numbers, "the deleted number is", numb)


#pop used to retain the deleted value})

removed_number = numbers.pop(2)
print(f"{numbers} the removed number is {removed_number}")

#deleting with delete
del numbers[0] # deletes with specified index
print(numbers)