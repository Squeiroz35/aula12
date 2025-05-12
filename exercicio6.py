soma=0
for x in range(1,6):
    numero=int(input("digite um numero:"))
    soma= soma+numero
media= soma/5
if media>=7:
    print("aprovado!")
elif media<7:
    print("Recuperação!")
elif media<4:
    print("final!")
else:
    print("reprovou!")