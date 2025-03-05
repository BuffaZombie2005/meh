S = 0

N = int(input("Input N(N must bigger than 9) "))
if N<10:
    raise Exception("Sorry number must bigger than 9")
for i in range (1,N+1):
    S += i*10+i
print(S)
