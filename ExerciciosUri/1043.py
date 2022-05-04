a,b,c = [float(x) for x in input().split()]
if (b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b):
    print('Perimetro: ', a+b+c)
else:
    print('Area', (a+b)*c/2)
