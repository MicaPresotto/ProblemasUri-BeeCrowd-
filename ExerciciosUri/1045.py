a,b,c = [float(x) for x in input().split()]

if c > a:
    x = c
    c = a
    a = x
elif b > a:
    x = b
    b = a
    a = x

if a >= (b+c):
    print('Nao forma triangulo')
else:
    if a**2 == b**2 + c**2:
        print('Triangulo retangulo')
    elif a**2 > (b**2 + c**2):
        print('Triangulo obtusangulo')
    elif a**2 < (b**2 + c**2):
        print('Triangulo Acutangulo')
    
    if a == b == c:
        print('Triangulo equilatero')
    elif a == b or c == b or c == a:
        print('Triangulo isoceles')
