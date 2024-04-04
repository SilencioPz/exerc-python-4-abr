'''
Deixei float por ser notas, sempre tem décimos por algum professor
'''
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"A média do aluno é {media:.2f}. Está aprovado.")
else:
    print(f"A média do aluno é {media:.2f}. Está reprovado.")