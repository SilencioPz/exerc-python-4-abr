#Informa data e hora 
import datetime

ano_nascimento = int(input("Informe teu ano de nascimento: "))
#Função possível graças ao import acima
ano_atual = datetime.datetime.now().year

if ano_atual - ano_nascimento >= 18:
    print("Tu tá lascado meu parça!")
else:
    print("Tu és leite com pêra.")