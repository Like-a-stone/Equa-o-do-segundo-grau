#EQUAÇÂO DO SEGUNDO GRAU QUESTAO 2
a= int(input("Digite A: "))
b= int(input("Digite B: "))
c= int(input("Digite C: "))
delta= b**2-4*a*c
if delta <=0:
  print("Delta é igual a",delta,"portanto, não há bhaskara")
 else:
 raiz_delta = delta**(1/2)
  print("para o x uma linha teremos: ", (-b+raiz_delta)/2*a)
  
 print("para o x duas linhas teremos: ", (-b-raiz_delta)/2*a)
