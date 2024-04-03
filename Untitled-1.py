# This is a python program to calculate the fibonacci sequence. Create the fibonacci sequence using a generator.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fib(i), end=" ")
    print("vroom vroom")