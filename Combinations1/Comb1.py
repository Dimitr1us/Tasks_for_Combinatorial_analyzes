combinations=[]
for i in range(10000,99999):
    string = str(i)
    if (string.count('9')==0 and string.count('0')==0):
        combinations.append(string)
with open("output.txt","w") as f:
    for i in combinations:
        f.write(str(i)+" ")
    f.write("\n")
    f.write(str(len(combinations)))