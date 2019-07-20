salario = float(input('Digite seu salário atual '))
aumento = 15
salarioAtualizado = (salario + ((salario * aumento) / 100))
print('Seu salário era : {}, com o aumento de : {}%, ficou : {}'.format(salario, aumento, salarioAtualizado))