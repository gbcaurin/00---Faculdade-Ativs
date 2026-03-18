#Descobrir se a pessoa pode doar sangue, para isso ela deve ter entre 18 e 67 anos
while True:
    age = int(input("Quantos anos voce tem?: "))
    if age >= 18 and age <=67:
        print("VOce pode doar sangue")
    else:
        print("Voce nao pode doar sangue")