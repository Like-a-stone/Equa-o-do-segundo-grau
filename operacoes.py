#O programa é destinado a realizar qualquer uma das quatros operações matemáticas

#Entrada do tipo de operação
sinal=input("Digite aqui a operação que deseja. Ex(+, -, /, *):  ")
print(" ")
#Entrada dos números para operação
num1=int(input("Digite o primeiro número para operação: "))
print(" ")
num2=int(input("Digite o segundo número para operação: "))

#Condicionais if,or. Usando simbolos e nomes
if (sinal=="+" or sinal =="soma"):
  print(" ")
  print(num1, "+", num2, "=", num1+num2)

elif (sinal == "-" or sinal== "subtração" or sinal== "subtracao"):
  print(" ")
  print(num1,"-",num2,"=", num1-num2)

elif (sinal =="*" or sinal=="multiplicação" or sinal=="multiplicacao"):
  print(" ")
  print(num1,"*",num2,"=",num1*num2)
  
elif (sinal=="/" or sinal=="divisão" or sinal=="divisao"):
  print(" ")
  print(num1,"/",num2,"=",num1/num2)
  
else:
  print("operador inválido, execulte o progama novamente")
print(" ")
print("Fim do progama")  
