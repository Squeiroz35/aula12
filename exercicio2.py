from random import randint
numerosecreto=randint(0,100)
adivinha = 0
while adivinha != numerosecreto:
    adivinha = int(input("digite um numero:"))

    if adivinha < numerosecreto:
        print("numero menor que o certo")
    elif adivinha > numerosecreto:
        print("numero maior que o certo")
    else:
        print("voce acertou!!!")
