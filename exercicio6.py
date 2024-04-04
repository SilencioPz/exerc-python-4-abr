valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

#Validação simples para descobrir se é maior, menor ou igual
if valor1 > valor2:
    print(f"O maior valor foi {valor1}.")
elif valor2 > valor1:
    print(f"O maior valor foi {valor2}.")
else:
    print("Os dois valores são iguais.")