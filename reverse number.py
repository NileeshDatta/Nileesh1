'''write a programto find rev of given number

'''
n=int(input("Enter"))

rev=0
while n!=0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
print(rev)
    
