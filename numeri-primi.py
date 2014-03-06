#numeri primi
import datetime
from math import sqrt
g = 0
lista_primi = [2,]
print ("define prime numbers from 1")
b = int(float(input ('to')))
#time start
inizio = datetime.datetime.now()

for x in range(3,b,2) :
    rad = int( sqrt ( x ))
    divisori = 0
    y = lista_primi[g]
    while y < rad + 1:
        resto = x % y     
        if resto == 0:
            divisori = 1
            break
        elif resto!=0:
            g = g + 1
            y = lista_primi[g]
    if divisori == 0: 
        lista_primi.append(x)
        g = 1
    else:
        g = 1
        
fine = datetime.datetime.now()
differenza = fine - inizio
print(differenza)
# time end
for p in lista_primi:
    print (p)
print ('end')
