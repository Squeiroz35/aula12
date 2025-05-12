frase=input("digite uma frase:")
contador=0
for x in range (len(frase)):
    if frase[x]=="a" or frase[x]=="A":
        contador+=1
print(contador)