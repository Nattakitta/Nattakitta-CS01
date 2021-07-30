Num = int(input(' Enter Your Loop ='))
NumTotal = []
for i in range (Num) :
    data = int(input(' Enter Your Data ='))
    NumTotal += [data]
    A = min(NumTotal) , max(NumTotal)
print(A)
