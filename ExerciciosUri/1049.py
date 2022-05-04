x = input().lower()
y = input().lower()
z = input().lower()

if x == 'vertebrado' and y == 'ave' and z == 'carnivoro':
    print('Aguia')
elif x == 'vertebrado' and y == 'ave' and z == 'onivoro':
    print('Pomba')
elif x == 'vertebrado' and y == 'mamifero' and z == 'onivoro':
    print('Homem')
elif x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro':
    print('Vaca')
elif x == 'invertebrado' and y == 'inseto' and z == 'hematofogo':
    print('Pulga')
elif x == 'invertebrado' and y == 'inseto' and z == 'herbivoro':
    print('Lagarta')
elif x == 'invertebrado' and y == 'anelideo' and z == 'hematofogo':
    print('Sanguessuga')
elif x == 'invertebrado' and y == 'anelideo' and z == 'onivoro':
    print('Minhoca')
else:
    print('Digitou algo errado, digite tudo sem acentos')