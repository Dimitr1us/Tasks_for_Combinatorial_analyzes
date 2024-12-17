n=int(input("Сколько элементов в подстановке, элементы от 1 до n: "))
print('Введите поочередно значения вектора')
vector=[0]*n
for i in range(n):
    vector[i]=int(input(str(i+1)+" элемент: "))
spisok=[0]*n
for i in range(0,n):
    spisok[i]=i+1
podstanovka=[]
for i in range(n-1,-1,-1):
    count=len(spisok)
    podstanovka.insert(0,spisok[count-1-vector[i]])
    spisok.remove(spisok[count-1-vector[i]])
print(podstanovka)