def yanghui():
    b=[1]
    while True:
        yield b
        b = [sum(i) for i in zip([0] + b,b + [0])]
n = 0
for t in yanghui():
    print(t)
    n += 1
    if n == 10:
        break
