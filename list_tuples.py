#Method: append()
#EASY QUESTIONS
#What happens to the length of a list after calling the append() method?

#it will increase by 1 as a new element is added to the end of the list.
l =[1,3,"uma",2]
print(len(l)) # 4
l.append(4)
print(len(l)) # 5
#Where is the new element placed when you use list.append(x)?
#new element is placed at the end (last) of the list.

#Write a simple line of code to add the string 'apple' to a list named 'fruits'.
fruits = ['banana', 'orange']
fruits.append('apple')
print(fruits)  # Output: ['banana', 'orange', 'apple']

#MEDIUM QUESTIONS
#If you append a list [10, 20] to an existing list [1, 2],
#  what is the total number of elements in thefinal list?
l = [1, 2]
l.append([10, 20])
print(l)  # [1, 2, [10, 20]]
print(len(l))  #3
total number of elements in the final list is 3 because the entire list [10, 20] is
added as a single element to the original list.

#Explain the difference in result between list.append([5, 6]) and list + [5, 6].
append([5, 6]) # adds one nested list
[1, 2, [5, 6]]
list + [5, 6] → creates a new list with elements merged
[1, 2, 5, 6]

'''Method: extend()
EASY QUESTIONS'''
#Does the extend() method add elements individually or as a single nested object?
It adds elements individually. When you use extend(), it takes each element from the 
iterable you provide and adds it to the end of the list as separate elements, 
rather than adding the entire iterable as a single nested object.
#What type of argument (e.g., integer, iterable) does the extend() method expect?
iterable (like list, tuple, set, etc.)

#How do you merge list B into list A using extend()?
extend() method is used to merge list B into list A. You can do this by 
calling the extend() method on list A and passing list B as an argument.
A = [1, 2, 3]
B = [4, 5, 6]
A.extend(B)
print(A)  # Output: [1, 2, 3, 4, 5, 6]


#MEDIUM QUESTIONS
#Predict the output: my_list = [1, 2]; my_list.extend('34'); print(my_list).
[1,2,'3','4'] --> string is iterable → characters added one by one
#What is the difference between extend() and the += operator for lists, if any?
a.extend(b) --> modifies list a in place by adding elements of b
a += b --> Add elements individually

'''Method: insert()
EASY QUESTIONS
How many arguments does the insert() method take?'''
Two arguments: index and element to be inserted.

#If you want to add an element at the very beginning of a list, what index 
# should you use in insert()?
use index 0 to add an element at the very beginning of a list with insert().
insert(0,"uma") # will add "uma" at the beginning of the list

#Does insert() replace the existing element at the given index or shift it?
shifts it to right and inserts the new element at the specified index.
l = [1, 2, 3]
l.insert(1, 'x')
print(l)  # Output: [1, 'x', 2, 3] 

#MEDIUM QUESTIONS
#What happens if you use a negative index, like list.insert(-1, 'x'), on a list of 3 items?
using -ve index will insert the element before the last element of the list but
it will not replace the existing element at that index.
lst = [1, 2, 3]
lst.insert(-1, 'x')
print(lst)  # Output: [1, 2, 'x', 3]

#In terms of performance, why is insert(0, x) considered slower than append(x)
# for large lists?
insert(0, x) is slower than append(x) for large lists because insert(0, x)
 requires shifting all existing elements in the list one position to the
right to make space for the new element at the beginning. 
This operation has a time complexity of O(n), where n is the number of 
elements in the list. On the other hand, append(x) simply adds the new element 
at the end of the list without needing to shift any existing elements, resulting 
in a time complexity of O(1). Therefore, as the size of the list increases, the 
performance difference becomes more significant, making insert(0, x) less 
efficient than append(x).

append(x) → O(1) (adds at end, no shifting)
insert(0, x) → O(n) (shifts all elements)

➡️ For large lists, shifting every element makes it slower.