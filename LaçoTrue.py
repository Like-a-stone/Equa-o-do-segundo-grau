#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

while True:
  name=input("Digite seu nome: ")
  age=int(input("Digite sua idade:"))
  salary=float(input("Digite seu sálario: "))
  gender=input("Digite seu sexo (m,f)")
  status=input("Estado civil (s,c,v,d): ")
  if len(name)<=3:
    print("Nome não aceito!")
  if age >150:
    print("Idade não aceita! ")
  if salary<=0:
    print("sálario incoerente!")
  if gender != "m" and gender !="f":
    print("Gênero não aceito Sigma Rule Bitc*")
  if status != "s" and status != "c" and status != "v" and status != "d":
    print("Estado civil não aceito!")
  else:
    break
print("Successful")    
                
            
     
  
