def check(string):
    numbers=[0]*9
    for i in range(1,9):
        numbers[i] = string.count(str(i))
    if (numbers.count(2)==1 and numbers.count(3)==1): return True
    else : return False


combinations=[]
for i in range(1000000,9999999):
    string = str(i)
    if (string.count('9')==0 and string.count('0')==0):
        if (check(string)):
            combinations.append(string)
with open("output.txt","w") as f:
    for i in combinations:
        f.write(str(i)+" ")
    f.write("\n")
    f.write(str(len(combinations)))