S = 0

N = int(input("Input N(N must bigger than 9) "))
if N<10:
    raise Exception("Sorry N must bigger than 9")
for i in range (1,N+1):
    if i<10:
        S += i*10+i
    else:
        S += i*100+i
print(S)
