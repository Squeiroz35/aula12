nomesgerados=[]
nomesA=[]
for x in range(1,6):
    nome=input("digite um nome:")
    if nome[0]== "a" or nome[0] == "A":
        nomesA.append(nome)
    nomesgerados.append(nome)
print(nomesA)


