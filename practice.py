#1. Write a python program to remove the duplicate in given list.
 #               a = [2,3,4,2,3,4,5,7]
 #               output: [2,3,4,5,7]
a = [2,3,4,2,3,4,5,7]
res = []
for i in a:
    if i not in res:
        res.append(i)
print(res)

#2. Write a program that takes array of numbers as input, 
# among the numbers in array, print the numbers which forms a prime number by 
# adding one to it. Print such numbers in the given array separated b spaces.
 #             Testcase1	:  [ 7, 4, 7, 23, 10, 6]
  #             Output     	:  4 10 6
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(arr):
    # Filter numbers where (num + 1) is prime
    result = [str(x) for x in arr if is_prime(x + 1)]
    print(" ".join(result))

# Example usage
test= [7, 4, 7, 23, 10, 6]
solve(test) # Output: 4 10 6

#3. Write python program 
 #             a   = " aaabbaaccdd"
  #           output: "a5b2c2d2”
a = " aaabbaaccdd"

def counting_characters(s):
    # Create a list of unique characters excluding spaces, maintaining order
    unique_chars = []
    for char in s:
        if char != " " and char not in unique_chars:
            unique_chars.append(char)
    
    # Build the result string by counting occurrences in the original string
    result = ""
    for char in unique_chars:
        c = s.count(char)
        result += f"{char}{c}" 
    print(f'"{result}"')
counting_characters(a)
