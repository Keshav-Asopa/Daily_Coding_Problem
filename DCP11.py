'''
Given two arrays X and Y of positive integers, find number of pairs such that xy > yx (raised to power of) where x is an element from X and y is an element from Y.

Input:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test consists of three lines. The first line of each test case consists of two space separated M and N denoting size of arrays X and Y respectively. The second line of each test case contains M space separated integers denoting the elements of array X. The third line of each test case contains N space separated integers denoting elements of array Y.

Output:
Corresponding to each test case, print in a new line, the number of pairs such that xy > yx.

Constraints:
1 ≤ T ≤ 100
1 ≤ M, N ≤ 105
1 ≤ X[i], Y[i] ≤ 103

Example:
Input
1
3 2
2 1 6
1 5

Output
3
'''
#DCP11
def comopare_power(a,b,m,n):
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if pow(a[i],b[j])>pow(b[j],a[i]):
                count += 1
    return count

if __name__ == "__main__":
    ans = 0
    ans_list = []
    test_cases = int(input())
    for i in range(test_cases):
        n , m = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        ans = comopare_power(a,b,m,n)
        ans_list.append(ans)
    for i in range(test_cases): 
        print(ans_list[i], end = " ")
