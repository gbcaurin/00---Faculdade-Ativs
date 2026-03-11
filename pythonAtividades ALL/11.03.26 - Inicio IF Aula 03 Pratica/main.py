#Descobrir se o numero é par ou impar.  1
#num = int(input("Digite um número inteiro: "))
#if num % 2 == 0:
    #print("O número é par.")
#else:
    #print("O número é ímpar.")


#Descobrir se é multiplo de 5.  2
#num = int(input("Digite um número inteiro para descubrir se é multiplo de 5: "))
#if num % 5 == 0:
  #print("O número é múltiplo de 5.")
#else:
  #print("O número não é múltiplo de 5.")


#Receber dois numeros, se forem iguais, some, se for diferente multiplique.  3
#a = int(input("Digite um número inteiro: "))
#b = int(input("Digite outro número inteiro: "))
#if a == b:
  #c = a+b
  #print("A soma dos números é:", c)
#else:
  #d = a*b
  #print("A multiplicação dos números é:", d)


#Calcular o reajuste de acordo com o salario.  4
#sal = float(input("Digite o valor do seu salário: "))
#if sal >= 500:
  #if sal >= 1000:
    #reaj2 = sal * 0.05
    #reaj1000 = sal + reaj2
    #print("O valor do salário com reajuste adicional é:", reaj1000)
  #else:
     #reaj = sal * 0.10
     #reaj500 = sal + reaj
     #print("O valor do salário com reajuste é:", reaj500)
#else:
  #reaj3 = sal * 0.15
  #reaj1 = sal + reaj3
  #print("O valor do salário com reajuste é:", reaj1)


#Verificar se é divisivel.  5
#num1 = int(input("Digite um número inteiro: "))
#num2 = int(input("Digite outro número inteiro: "))
#if num1 % num2 == 0:
  #print("O primeiro número é divisível pelo segundo.")
#else:
  #print("O primeiro número não é divisível pelo segundo.")


#Se o produto for mais caro que 100 tem desconto de 10%, se nao, matem o mesmo preço.  6
#prod = float(input("Digite o valor do produto: "))
#if prod > 100:
  #desc = prod * 0.10
  #valor = prod - desc
  #print("O valor do produto com desconto é:", valor)
#else:
  #print("O valor do produto é:", prod)


#Se a senha for 2026 entra se não nao entra.  7
#passw = int(input("Digite sua senha de numeros inteiros: "))
#if passw == 2026:
  #print("Logado")
#else:
  #print("Senha incorreta")


#Pegar o salario bruto e o valor do emprestimo, se o valor do emprestimo for 30% do salario, recusar. Se nao aceitar. Se for cliente a mais de 2 anos, aceitar com bonus.   8
#sal = float(input("Digite o valor do seu salário: "))
#emp = float(input("Digite o valor do seu empréstimo: "))
#temp = int(input("Digite a quanto tempo voce presta serviço a empresa (em anos): "))
#salemp = sal * 0.3
#if emp < salemp:
  #if temp > 2:
    #print("Aprovado com bonus")
  #else:
    #print("Empréstimo aprovado")
#else:
  #print("Empréstimo não aprovado")


#Ler a idade de lutador, se for menor que 18, Categ juvenil. Se for maior de 18 e com peso menor que 80, Peso Médio. Se for maior de 18 e peso maior que 80, Peso Pesado.   9
#age = int(input("Digite sua idade: "))
#if age < 18:
  #print("Categoria Juvenil")
#else:
  #peso = int(input("Digite seu peso em KGs: "))
  #if peso <= 80:
    #print("Peso Médio")
  #else:
    #print("Peso Pesado")