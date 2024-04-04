idade = int(input("Informe a sua idade: "))

#Como não aprendemos match-case ainda, usei if elif else
if 0 <= idade <= 11:
    print("Tu é muleque!")
elif 12 <= idade <= 18:
    print("Tu é jovem dinâmico!!")
elif 19 <= idade <= 24:
    print("Tu tá lascado!!!")
elif 25 <= idade <= 40:
    print("Tu tem conta pra pagar! XD")
elif 41 <= idade <= 60:
    print("Tá veiaco heim fii?! >X)")
else:
    print("Tá com o pé na cova é?! :D")