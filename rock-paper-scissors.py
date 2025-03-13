''''
Pedra, papel ou tesoura

Jogo pra duas pessoas:

Jogador 1: Pedra, papel e tesoura

Jogador 2: Pedra, papel e tesoura

Pedra ganha da tesoura; Tesoura ganha do papel; Papel ganha da pedra;
'''

p1 = str(input("Nome do jogador 1:"))
p2 = str(input("Nome do jogador 2:"))

print(p1,", escolha: pedra, papel ou tesoura?")
p1p = str(input())
print(p2,", escolha: pedra, papel ou tesoura?")
p2p = str(input())

if (p1p=='pedra') and (p2p=='tesoura'):
  print(p1, "escolheu", p1p, "e venceu", p2, "que escolheu", p2p)
elif (p1p=='papel') and (p2p=='pedra'):
  print(p1, "escolheu", p1p, "e venceu", p2, "que escolheu", p2p)
elif (p1p=='tesoura') and (p2p=='papel'):
  print(p1, "escolheu", p1p, "e venceu", p2, "que escolheu", p2p)
elif (p1p=='pedra') and (p2p=='papel'):
  print(p2, "escolheu", p2p, "e venceu", p1, "que escolheu", p1p)
elif (p1p=='papel') and (p2p=='tesoura'):
  print(p2, "escolheu", p2p, "e venceu", p1, "que escolheu", p1p)
elif (p1p=='tesoura') and (p2p=='pedra'):
  print(p2, "escolheu", p2p, "e venceu", p1, "que escolheu", p1p)
elif (p1p=='pedra') and (p2p=='pedra'):
  print("Empate! Os dois jogadores escolheram pedra")
elif (p1p=='papel') and (p2p=='papel'):
  print("Empate! Os dois jogadores escolheram papel")
elif (p1p=='tesoura') and (p2p=='tesoura'):
  print("Empate! Os dois jogadores escolheram tesoura")
else:
  print("Partida inválida.")