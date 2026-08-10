class Solution:
    def isPalindrome(self, n):
         rev=0
         old=n
         while n>0:
            ld=n%10
            n=n//10
            rev=rev*10+ld
         if rev==old:
            return ("is_a_palindrome")
         else:
                return ("not_A_palindrome")
n=int(input("enter a number: "))
obj=Solution()
print(obj.isPalindrome(n))
            

        