def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b - 1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = multiply(a, b)
print(result)