'''
Given two sorted arrays P[] and Q[] in non-decreasing order with size X and Y. The task is to merge the two sorted arrays into one sorted array (in non-decreasing order).

Note: Expected time complexity is O((X+Y) log(X+Y)). DO NOT use extra space.

Input:
First line contains an integer T, denoting the number of test cases. First line of each test case contains two space separated integers X and Y, denoting the size of the two sorted arrays. Second line of each test case contains X space separated integers, denoting the first sorted array P. Third line of each test case contains Y space separated integers, denoting the second array Q.

Output:
For each test case, print (X + Y) space separated integer representing the merged array.

'''
#DCP9
import re
def merge_sorting(a,b,m,n):
    for i in range(len(b)):
        a.append(b[i])
    a.sort()
    for i in a:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    ans = 0
    ans_list = []
    test_cases = int(input())
    for i in range(test_cases):
        n , m = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        merge_sorting(a,b,m,n)


