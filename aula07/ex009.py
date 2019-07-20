preco = float(input('Digite o preço do produto '))
desconto = 5
valor = (preco - ((preco * 5) / 100))
print('Com o desconto de : {}%, 100 produto que estava com o valor : {}, ficou com o valor : {}'.format(desconto, preco, valor))