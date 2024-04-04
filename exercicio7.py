#Informei como float por conta da divisão
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print(f"A soma é: {soma}")
print(f"A subtração é: {subtracao}")
print(f"A multiplicação é: {multiplicacao}")

if numero2 != 0:
    divisao = numero1 / numero2
    #Fiz uma formatação para aparecer apenas 2 após o ponto
    print("A divisão é: {:.2f}".format(divisao))
else:
    print("Não dá pra dividir por zero!!!")