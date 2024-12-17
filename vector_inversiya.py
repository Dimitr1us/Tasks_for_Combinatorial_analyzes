n=int(input("Сколько элементов в подстановке, элементы от 1 до n: "))
perestanovka=[0]*n
for i in range(n):
    perestanovka[i]=int(input(str(i+1)+" элемент: "))
vector=[0]*n
for i in range(n):
    count=0
    for j in range(i):
        if (perestanovka[j]>perestanovka[i]): count=count+1
    vector[i]=count
print(vector)