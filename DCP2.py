'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

#DCP 2
# Python3 program for A Product Array Puzzle 
def productArray(arr, n): 
  
    i, temp = 1, 1
  
    # Allocate memory for the product array  
    prod = [1 for i in range(n)] 
  
    # Initialize the product array as 1  
  
    # In this loop, temp variable contains product of 
    # elements on left side excluding arr[i]  
    for i in range(n): 
        prod[i] = temp 
        temp *= arr[i]
        print(temp)
    print(prod)
          
    # Initialize temp to 1 for product on right side  
    temp = 1
  
    # In this loop, temp variable contains product of 
    # elements on right side excluding arr[i]  
    for i in range(n - 1, -1, -1): #(start, stop, step)
        prod[i] *= temp 
        temp *= arr[i]
        print(temp)
    print(prod)
  
    # Print the constructed prod array  
    for i in range(n): 
        print(prod[i], end = " ") 
  
    return
  
# Driver Code 
arr = [10, 3, 5, 6, 2] 
n = len(arr) 
print("The product array is: n") 
productArray(arr, n) 
