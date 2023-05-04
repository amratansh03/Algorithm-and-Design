def gcd1(a,b):
  if a == b:
    return a
  elif a>b:
        a=a-b
        if b%a ==0:
            return a
  elif a<b :
        b=b-a
        if a%b == 0:
            return b

a = int(input("enter number1: "))
b = int(input("enter number2: "))
print(gcd1(a,b))