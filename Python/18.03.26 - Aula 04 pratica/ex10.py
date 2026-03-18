#Calculo do fatorial de um numero inteiro
n = int(input("Digite um numero inteiro: "))
saven = n
i = n
if n == 0:
 print(f"0! é 1")
else:
 while i > 1:
  fat = n * (i - 1)
  i -= 1 
  n = fat
  print(f"{saven}! é {fat}")
