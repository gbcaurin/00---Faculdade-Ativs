#Digitar numeros inteiros e apresentar a quantidade de numeros impares e a soma dos numeros pares
ip = 0
ii = 0
while True:
  n = int(input("Digite um número inteiro(0 para sair): "))
  if n == 0:
    break
  if n % 2 == 0:
    ip += n
  else:
    ii+= 1
  
print(f"Foram digitados {ii} números ímpares.")
print(f"A soma dos números pares é {ip}.")
