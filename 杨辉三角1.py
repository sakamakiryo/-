def yanghui();
    b=[1]
    while True:
        yield b
        b = [[1]+[b(i)+b(i+1)]+[1]]
        for i in range (len(b))
n=0
for t in yanghui();
    print (t)
    n += 1
    if n == 10:
        break