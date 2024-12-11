import os
os.system("clear")

# Solicitando dados do usuário.

lista_nomes = []

while True:
    nome = input("Digite seu nome: ")

    if nome == "sair":
        break
    else:
        lista_nomes.append(nome)

 # Exibindo dados.
for nome in lista_nomes:
    print(nome)

