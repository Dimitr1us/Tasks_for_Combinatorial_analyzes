def factorial(x):
    p=1
    for i in range(1,x+1):
        p=p*i
    return p
def f(x):
    k=x//2
    return factorial(k+2)/(factorial(k)*factorial(2))

n=int(input())
if(n%2==0):
    print("Нужно нечётное количество.")
else:
    print(f"Всего вариантов: {int(f(n))}")
