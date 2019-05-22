'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
# Python program to find if there are 
# two elements wtih given sum 
  
# function to check for the given sum 
# in the array 
def printPairs(arr, arr_size, sum): 
      
    # Create an empty hash set 
    s = set() 
      
    for i in range(0,arr_size): 
        temp = sum-arr[i] 
        if (temp>=0 and temp in s): 
            print ("Pair with the given sum is", arr[i], "and", temp) 
        s.add(arr[i]) 
  
# driver program to check the above function 
A = [1,4,45,6,10,8] 
n = 16
printPairs(A, len(A), n) 
