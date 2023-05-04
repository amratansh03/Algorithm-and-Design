def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("enter number1: "))
b = int(input("enter number2: "))
print(gcd(a,b))