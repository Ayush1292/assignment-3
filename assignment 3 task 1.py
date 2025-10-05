#Calculate Factorial Using a Function

a = int(input("Enter a number: "))

def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

result = factorial(a)
print("factorial of", a, "is", result)




