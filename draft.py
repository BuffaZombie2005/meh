S = 0

def countNum(N):
    digit = N
    count=0
    addNum = 1
    while digit != 0:
        digit //= 10
        count = count + 1
    for i in range(1,count+1):
        addNum *= 10
    return addNum

N = int(input("Input N(N must bigger than 9) "))
if N<10:
    raise Exception("Sorry N must bigger than 9")


for i in range (1,N+1):
    if i<10:
        S += i*10+i
    else:
        S += i*countNum(i)+i
print(S)

