# Verificar se os batimentos cardiacos por minuto se encontram na faixa dequada. Para isso
# voce deve solicitar que o usuario informe o seu numero de batimentos por minuto (BPM) e a IDADE
# A partir disso o script deve verificar e exibir uma mensagem informando se os batimentos do
# usuario encontram-se dentro da faixa adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada,
# de acordo com o site Tua Saude


# IDADE BPM
# Ate 2 anos 120 a 140
# De 8 anos ate 17 anos 80 a 100
# Adulto sedentario 70 a 80
# Idosos 50 a 60



print("VERIFICADOR DE BATIMENTOS POR MINUTO\n")

batimentos = int(input("Digite seu numero de batimentos por segundo (BPM): "))
idade = int(input("Digite a sua idade: "))

if idade <= 2:
    if batimentos >= 120:
        if batimentos <= 140:
            print("Batimentos dentro da faixa adequada para a idade! ")
        else:
            print("Batimentos acima da faixa adequada para a idade! ")
    else:
        print("Batimentos abaixo da faixa adequada para a idade!")


elif idade >= 8:
    if batimentos >= 80:
        if batimentos <= 100:
            print(" Batimentos dentro da faixa adequada para a idade! ")
        else:
            print("Batimentos acima da faixa adequada para a idade! ")
    else:
        print("Batimentos abaixo da faixa adequada para a idade! ")
       

elif idade >= 18:
    if batimentos >= 70:
        if batimentos <= 80:
            print("Batimentos dentro da faixa adequada para a idade!")
        else:
            print("Batimentos acima da faixa adequada para a idade!")
    else:
        print("Batimentos abaixo da faixa adequada para a idade!")

elif idade >= 60:
    if batimentos >= 50:
        if batimentos <= 60:
            print("Batimentos dentro da faixa adequada para a idade!")
        else:
            print("Batimentos acima da faixa adequada para a idade!")
    else:
        print("Batimentos abaixo da faixa adequada para a idade!")


else:
    print("A idade informada eh invalida ")






