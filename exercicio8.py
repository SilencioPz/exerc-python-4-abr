valor1 = float(input("Informe o primeiro valor (menor que 100): "))
valor2 = float(input("Informe o segundo valor (menor que 100): "))

#A validação é apenas com números até 99, 100 ou maiores ocorre uma mensagem
if valor1 < 100 and valor2 < 100:
    soma = valor1 + valor2
    print(f"A soma é: {soma}")
else:
    print("Não aceito maior ou igual a 100 fii! Tente de novo caceta!!! >XD")
