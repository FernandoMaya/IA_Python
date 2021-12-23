import math
import random

def palabra():
    n=8 # de consonante vocal. pares
    con='abcdefghijklmnñopqrstuvwxyz'
    L=[]
    #Cambiar los for
    for i in range(1,201):
        p=''
        for j in range(n):
            p+=''.join(random.choice(con))
        a = str(p.count("a"))
        num = ('%0.3d' % i)
        L.append(num + a + p)
    L_upper = [x.upper() for x in L]
    L_upper.sort(reverse=True)
    # print (L_upper)
    print ('\n\n\n\n')
    print (L_upper)

palabra()
        

