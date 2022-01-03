### Developed by: Sadigueira ###
### Desvio Padrão e Variância de Dados Amostrais ###

from statistics import stdev 
from statistics import variance
from statistics import median
import numpy as np
import time
import matplotlib.pyplot as plt


def menu():
    print('\n')
    print('*******OPÇÕES********')
    print('1 - Iniciar Cálculos ')
    print('2 - Encerrar Programa')
    print('*********************')
    
menu()
o = int(input('Digite sua opção:')) 

while o < 1 or o > 2:
    print('Opção inválida!!!')
    time.sleep(1)
    menu()
    o = int(input('Digite a sua opção novamente:'))
         
while o == 2:
    print('Programa está sendo encerrado!!!')
    time.sleep(3)
    break  
    
while o == 1:
    
    n = 0
    n = int(input('Digite o quantidade de dados que deseja inserir:'))
    while n <= 1:
        print('Valor precisa ser maior que 1 !!!')
        time.sleep(1)
        n = int(input('Digite o quantidade de dados que deseja inserir:'))
        
    desvio = [0]
    desvio = []
    for n in range(n):
        desvio.append(float(input('Digite os valores:')))
    
    desvio_padrao = stdev(desvio)
    variancia     = variance(desvio)
    media         = np.mean(desvio)
    mediana       = median(desvio)
    Q1            = np.percentile(desvio, 25)
    Q3            = np.percentile(desvio, 75)
    Minimo        = np.min(desvio)
    Maximo        = np.max(desvio)

    print('\n')
    print('A Média dos valores é:',   round(media,6))
    print('A Variância é:',           round(variancia,6))
    print('O Desvio padrão é:',       round(desvio_padrao,6))
    print('A Mediana dos dados é:',   round(mediana,6))
    print('O Primeiro Quartil vale:', round(Q1,6))
    print('O Terceiro quartil vale:', round(Q3, 6))
    print('O Menor valor vale:',      round(Minimo,6))
    print('O Maior valor vale',       round(Maximo,6))
    
    plt.boxplot(desvio)
    plt.show()
    
    time.sleep(3)
    menu()
    
    o = int(input('Digite sua opção:'))
    
    while o < 1 or o > 2:
        print('opcao invalida!!!')
        time.sleep(1)
        menu()
        o = int(input('Digite a sua opção novamente:'))
        
    if o == 2:
        print('Programa está sendo encerrado!!!')
        time.sleep(3)
        break    
    
