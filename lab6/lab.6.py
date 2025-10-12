from lab6dek import count_recursions
@count_recursions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(200))

print("Кількість рекурсивних викликів:", factorial.calls)
