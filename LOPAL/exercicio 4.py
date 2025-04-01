#-*- coding: UTF-8 -*-
print('olá usuario, irei calcular o seu aumento')
salário = float(input('qual é o seu sálario?: '))
salário2 = float(input('qual a porcentagem que você deseja de aumento?: '))
porcentagem = salário*salário2/100
soma = salário + porcentagem
print('o aumento será: ', porcentagem)
print('a soma será: ', soma)

