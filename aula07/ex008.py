altura = float(input('Digite altura da parede '))
largura = float(input('Digite largura da parede '))
area = altura * largura
tinta = 2
qtdTinta = area / tinta
print('Area {}, vo2.5cê precisa de {} tinta(s) para pintar essa parede'.format(area, qtdTinta))