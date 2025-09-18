#Peça ao usuário a nota de produtividade (0–10) e a nota de comportamento (0–10).
#Calcule a média.
#Classifique o funcionário:
#Média ≥ 9 → "Excelente desempenho"
# 9≤  Média 7 <  → "Bom desempenho"
#5 ≤ Média < 7 → "Desempenho regular"
#Média < 5 → "Precisa melhorar"

#aqui o programa pega as informações das notas
Nota_1 = float(input("Digite sua nota de Produtividade de 0 a 10: "))
Nota_2 = float(input ("Digite sua nota de Comportamento de 0 a 10: "))

#aqui o programa faz o calculo
media = (Nota_1 + Nota_2) / 2 

#aqui classifica o funcionario
if media >= 9: 
    print("Excelente Desempenho")
elif media >=7 and media < 9 :
    print("Bom desempenho") 
elif media >= 5 and media < 7:
    print("Desempenho regular")
else:
    print("precisa melhorar")

print (f"Sua nota é: {media}" )