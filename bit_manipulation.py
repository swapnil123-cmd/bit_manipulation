num1=10
num2=4
print("num1 & num2 are: ", num1 & num2)
print("num1 | num2 are: ", num1 | num2)
print("num1 ^ num2 are: ", num1 ^num2)
print("num1 << num2 are: ", num1<<num2)
print("num1 >> num2 are: ", num1>>num2)
print("not num1", ~num1)

# odd even bitwise
def isEvenOdd(n):
  if (n^1==n+1):
    return True
  else:
    return False
  
number=int(input("Enter a number: "))
if isEvenOdd(number): #by default checks for true
  print(number, " is even")
else:
  print(number, " is odd")
  
#checking for the numebr of bits 
def numberofBits(n):#5
  count=0
  while(n): #101 #010 #001 #000(loop stops)
    count += 1 #1 #2 #3
    n >>=1 #010 #001 #000 
  return count

n=int(input("Enter a number: "))
print("Number of bits: ", numberofBits(n))
