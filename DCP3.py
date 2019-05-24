'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''

#DCP 3
test = [3,4,-1,1]
for i in range(1,len(test)+1,1):
    if i not in test:
        print('first missing positive integer is {}'.format(i))
        break
