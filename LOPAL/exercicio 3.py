#-*- coding: UTF-8 -*-
print('digite sua quantidade de dias, horas, minutos e segundos e vou calcular o total em segundos')
dias = int(input('digite a quantidade de dias: '))
horas = int(input('digite a quantidade de horas: '))
minutos = int(input('digite a quantidade de minutos: '))
segundos = int(input('digite a quantidade de segundos: '))
resultado = (dias*86.400) + (horas*3.600) + (minutos*60) + (segundos)
print('o seu valor em segundos será: ', resultado)
