numero = int(input('Digite um número '))
count = 1;
print('A tabuada de {} '.format(numero))
while (count < 10) :
    tabuada = numero * count
    print('{} X {} é : {}'.format(numero, count, tabuada))
    count += 1