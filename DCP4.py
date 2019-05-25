'''
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5
'''

#DCP 5

def check(n,k,s):
    sum1 = 0
    count = 0
    i = 0
    j = 0
    while(i < n):
        sum1 += s[i]
        if sum1 > k:
            count += 1
            sum1 = 0
            i = count
            j = i
        elif sum1 ==  k:
            i += 1
            j += 1
            return j, i
        else:
            i+=1

if __name__ == "__main__":
    list1 = []
    ans_list = []
    test_cases = int(input())
    for i in range(test_cases):
        n,k= map(int,input().split())
        s = list(map(int,input().split())) 
        list1 = check(n,k,s)
        ans_list.append(list1)
    for i in range(test_cases):
        print("{} {}".format(ans_list[i][0],ans_list[i][1]))
 
