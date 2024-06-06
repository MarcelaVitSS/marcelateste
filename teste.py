qntd = int(input("Insira uma quantidade: "))
lista = []
inf = 234567890

for n in range(qntd):
    nome = input("Insira um nome: ")
    nome = nome.capitalize()
    if nome in lista:
        for i in range(inf):
           if nome in lista:
              print("Insira um nome diferente: ")
              nome = input("Insira um nome que não tenha sido mencionado")
              nome = nome.capitalize()
           else: 
              lista.append(nome)
              break
    else: 
       lista.append(nome)
print(lista)