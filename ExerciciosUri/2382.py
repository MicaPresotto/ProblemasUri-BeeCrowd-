l,a,p,r = [float(x) for x in input().split()]
for i in range(0,1):
    if not (0 <= l <= 1000 and 0 <=  a<= 1000 and 0 <=  p <= 1000 and 0 <= r <= 1000):
        print('Numero grande')
        break
    else:
        if l*l + a*a + p*p > 4*r*r:
            print('N')
        else:
            print('S')
        

