x,y,z = [int(x) for x in input().split()]

for i in range(0,1):
    if not 1 <= x <= 1000 and  1 <= y <= 1000 and 1 <= z <= 1000:
        print('Número grande')
        break
    if x*z <= y:
        print('S')
    else:
        print('N')
    
    