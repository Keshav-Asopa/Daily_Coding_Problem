'''
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
1 ≤ T ≤ 110
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Example:
Input
2
5
1 2 3 -2 5
4
-1 -2 -3 -4
Output
9
-1
'''
#DCP7
def maxSubArraySum(a,size): 
      
    max_so_far =a[0] 
    curr_max = a[0] 
      
    for i in range(1,size): 
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far,curr_max)  
    return max_so_far 

if __name__ == "__main__":
    ans = 0
    ans_list = []
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        a = list(map(int,input().split())) 
        ans = maxSubArraySum(a,n)
        ans_list.append(ans)
    for i in range(len(ans_list)):
        print(ans_list[i])
