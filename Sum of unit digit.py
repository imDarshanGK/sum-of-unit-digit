#Program to find sum of unit digit in a given number
n=int(input("Enter a number:"))
s=0
while n!=0:
    ud=n%10
    s=s+ud
    n=n//10
print("Sum=",s)
