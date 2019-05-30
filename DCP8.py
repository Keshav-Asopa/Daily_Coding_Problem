'''
finding the first positive integer 
'''
#DCP 8
def first_positive_integer(a,n):
	for i in range(1,len(test)+1,1):
	    if i not in test:
        	print('first missing positive integer is {}'.format(i))
        	break

if __name__ == "__main__":
	ans = 0
    	ans_list = []
    	test_cases = int(input())
    	for i in range(test_cases):
        	n = int(input())
        	a = list(map(int,input().split())) 
        	ans = first_positive_integer(a,n)
        	ans_list.append(ans)
    	for i in range(len(ans_list)):
        	print(ans_list[i])
