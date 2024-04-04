numero = int(input("Informe um número: "))

'''
Módulo é a divisão do número e o resto é o que foi dividido. Por exemplo: 2 % 2 terá módulo zero. Se 3 % 2 terá módulo 1 e assim sucessivamente.
'''
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")