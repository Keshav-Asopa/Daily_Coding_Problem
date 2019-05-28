'''
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1".

Constraints:
1 <= T <= 100
3 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
4
1 5 3 2
3
3 2 7
Output:
2
-1

'''
#code
def find_triplet(A):
    count = 0 
    A.sort()
    S = set(A)
    def sums(a,b):
        sum1 = a+b
        return sum1
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if sums(A[i],A[j]) in S:
                count += 1
    if count == 0:
        count = -1
    return count

import math

if __name__ == "__main__":
    ans = 0
    ans_list = []
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        a = list(map(int,input().split())) 
        ans = find_triplet(a)
        ans_list.append(ans)
    for i in range(len(ans_list)):
        print(ans_list[i])
