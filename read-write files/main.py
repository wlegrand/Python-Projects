

f = open("test.txt", "w")

for i in range(1, 100):
    a = str(i)
    f.writelines("num="+a+"\n")

f.close()

f = open("test.txt", "r")
bbb = '123'

while (True):
    line = f.readline()
    ccc = line[4:]
    ccc.strip()
    jk = len(ccc)
    if (jk > 0):
        nnn = float(ccc)
        print(nnn)
    if not line:
        break
    print(line)

f.close()
