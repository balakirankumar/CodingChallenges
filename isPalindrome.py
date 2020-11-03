
import sys
def isPalindrome(s):
    z=''
    for i in s:
        if i.isalpha():
            z+=i
    return z == z[::-1]

print(isPalindrome(sys.argv[1]))



import re

def is_Palindrome(s):
    forward="".join(re.findall(r'[a-z]+',s.lower()))
    backward=forward[::-1]
    return forward == backward
