#Incluindo nome a uma lista e ordenando a lista

#1. Exibindo a lista
lista=["anestesia", "index", "main", "float", "double", "string"]
print("Está é a lista: ", lista)
print(" ")
#2. Opção de incluir ou não uma palavra a lista
incluir=input("Digite a palavra que deseja incluir ou digite 0 para continuar")
#3.Condicionais para a respostas
#3.1 primera possiblidade: não incluir nova palavra e ordena as já existentes
if incluir ==0:
  lista.sort()
  print(lista)
#3.2 segunda possiblidade: incluir nova palavra na lista e ordena a lista
elif:
  lista.append(incluir)
  lista.sort()
  print(lista)
