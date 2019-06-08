'''
String Rotation
Problem Description
Rotate a given String in specified direction by specified magnitude.

After each rotation make a note of first character of the rotated String, After all rotation are performed the accumulated first character as noted previously will form another string, say FIRSTCHARSTRING.

Check If FIRSTCHARSTRING is an Anagram of any substring of the Original string.

If yes print "YES" otherwise "NO".

Constraints
1 <= Length of original string <= 30

1<= q <= 10

Input Format
The first line contains the original string s. The second line contains a single integer q. The ith of the next q lines contains character d[i] denoting direction and integer r[i] denoting the magnitude.

Output
YES or NO

Test Case

Explanation
Example 1

Input

carrace 3 L 2 R 2 L 3

Output

NO

Explanation After applying all the rotations the FIRSTCHARSTRING string will be "rcr" which is not anagram of any sub string of original string "carrace".
'''
def rotate(word,d,r,q): 
    S = ""
    for i in range(q):
        new_string = ""
        if d[i] == 'L':
    # slice string in two parts for left and right 
            Lfirst = word[0 : int(r[i])] 
            Lsecond = word[int(r[i]):] 
    # now concatenate two parts together
            new_string = Lsecond + Lfirst 
            S += new_string[0]
        else:
    # slice string in two parts for left and right 
            Rfirst = word[0 : len(word)-int(r[i])] 
            Rsecond = word[len(word)-int(r[i]): ]
    # now concatenate two parts together
            new_string = Rsecond + Rfirst
            S += new_string[0]
    return S
            
def anagram(fcs):
    if (word.find(fcs) != -1):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__": 
    word = input()
    q = int(input())
    d=[]
    r=[]
    for i in range(q):
        m,n = input().split()
        d.append(m)
        r.append(n)
    FIRSTCHARSTRING = ""
    FIRSTCHARSTRING = rotate(word,d,r,q)
    anagram(FIRSTCHARSTRING)
