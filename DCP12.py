'''
Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow. Each testcases contains two lines of input. The first line denotes the size of the array N. The second lines contains the elements of the array A separated by spaces.

Output: 
For each testcase, print the sorted array.
'''
#DCP12
def sorting(a,n):
    a.sort()
    return a
import re
if __name__ == "__main__":
    ans = 0
    ans_list = []
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        a = list(map(int,input().split())) 
        ans = sorting(a,n)
        ans_list.append(ans)
    for i in range(len(ans_list)):
        ans_list[i] = str(ans_list[i])
        ans_list[i] = re.sub('[^0-9]', '', ans_list[i])
        ans_list[i] = ' '.join(ans_list[i]) 
        print(ans_list[i])
