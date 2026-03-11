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

#10 pula pois eh igual o 4


#Ler dois numeros e descobrir se eles estão na origem, no eixo X, no eixo Y ou em qual quadrante estão.  11
#x = float(input("Digite um número X: "))
#y = float(input("Digite outro número Y: "))
#if x == 0 and y == 0:
    #print("Os números estão na origem.(0,0)")
#if x == 0 and y != 0:
    #print("Os números estão no eixo Y.")
#if x != 0 and y == 0:
    #print("Os números estão no eixo X.")
#if x > 0 and y > 0:
    #print("Os números estão no primeiro quadrante.")
#if x < 0 and y < 0:
    #print("Os números estão no terceiro quadrante.")
#if x < 0 and y > 0:
    #print("Os números estão no segundo quadrante.")
#if x > 0 and y < 0:
    #print("Os números estão no quarto quadrante.")


#Descobrir se os numeros formam um triangulo, se sim, descobrir qual tipo de triangulo.  12
#a = int(input("Digite um número inteiro: "))
#b = int(input("Digite outro número inteiro: "))
#c = int(input("Digite mais um número inteiro: ")) 
#if a < c+b and b < a+c and c < a+b:
  #if a == b and b == c and a == c:
    #print("Os números formam um triângulo equilátero.")
  #if a == b and a != c or a == c and a != b or b == c and b != a:
    #print("Os números formam um triângulo isósceles.")
  #if a != b and a != c and b != c:
    #print("Os números formam um triângulo escaleno.")
#else:
  #if a >= b+c:
    #print(f"O número {a} é maior ou igual à soma de {b} e {c}, portanto não formam um triângulo.")
  #if b >= a+c:
    #print(f"O número {b} é maior ou igual à soma de {a} e {c}, portanto não formam um triângulo.")
  #if c >= a+b:
    #print(f"O número {c} é maior ou igual à soma de {a} e {b}, portanto não formam um triângulo.")


#Ler os coeficientes de uma equação do segundo grau e calcular as raízes.  13
#a = int(input("Digite o valor de A: "))
#b = int(input("Digite o valor de B: "))
#c = int(input("Digite o valor de C: "))
##delta = (b ** 2) - (4 * a * c)
#if delta < 0 or a == 0:
    #print("A equação não possui raízes reais.")
#else:
    #b_plus = (-b + (delta ** 0.5)) / (2 * a)
    #b_minus = (-b - (delta ** 0.5)) / (2 * a)
    #print(f"As raízes da equação são: {b_plus} e {b_minus}.")


a, b, c, d, e, f = map(int, input("Digite os coeficientes da equação (A, B, C, D, E, F): ").split())
if (a * e) - (b * d) != 0:
    x = ((c * e) - (b * f)) / ((a * e) - (b * d))
    y = ((a * f) - (c * d)) / ((a * e) - (b * d))
    print(f"As soluções da equação são: x = {x:.2f} e y = {y:.2f}.")
else:
    print("A equação não possui soluções.")

    


  
