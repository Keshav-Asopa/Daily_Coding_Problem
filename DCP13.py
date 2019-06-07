'''
Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array. Equilibrium position in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Input:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. First line of each test case contains an integer N denoting the size of the array. Then in the next line are N space separated values of the array A.

Output:
For each test case in a new  line print the position at which the elements are at equilibrium if no equilibrium point exists print -1.
'''

def equilibrium(a,n):
    s = 0
    e = len(a)
    f = 0
    if e == 1:
        return e
    for i in range(1,len(a)):
        if sum(a[s:i]) == sum(a[i+1:e]):
            f = 1
            return i+1
    if f == 0:
        return -1
        
if __name__ == "__main__":
    ans = 0
    ans_list = []
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        a = list(map(int,input().split())) 
        ans = equilibrium(a,n)
        ans_list.append(ans)
    for i in range(test_cases): 
        print(ans_list[i], end = " ")
