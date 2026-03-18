n = int(input("Digite a quantidade de numeros inteiros que voce deseja digitar: "))

while n < 10:
 n = int(input("Digite um numero inteiro maior ou igual a 10: "))

x = int(input("Digite um numero inteiro: "))

max = x
min = x
i = 1

while i < n:
  x = int(input("Digite um numero inteiro: "))

  if x > max:
    max = x

  if x < min:
    min = x

  i += 1 
print(f"O maior numero foi {max} e o menor numero foi {min}")
    