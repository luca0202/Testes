# 2) Verificar se um número pertence à sequência de Fibonacci
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
if is_fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} NÃO pertence à sequência de Fibonacci.")