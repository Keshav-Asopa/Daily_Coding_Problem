'''
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ C[i] ≤ 107

Example:
Input:
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output:
4
9
'''
#DCP7
def missing_num(a,n):
    n = len(a)+1
    total = int(n*(n+1)/2)
    missing_number = int(total - sum(a))
    return missing_number

if __name__ == "__main__":
    ans = 0
    ans_list = []
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        a = list(map(int,input().split())) 
        ans = missing_num(a,n)
        ans_list.append(ans)
    for i in range(len(ans_list)):
        print(ans_list[i])
