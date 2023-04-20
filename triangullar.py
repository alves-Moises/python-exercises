
valid = False  # variavel de controle
while not valid:
    #recebe o valor e valida o tipo inteiro
    try:
        valor = int(input("DIgite o valor de K:"))
    except ValueError:
        print("Digite um valor inteiro!")
    else:
        if(valor <= 1):
            print("Digite um valor maior que 1!\n")
        else:
            valid = True  #muda valor da variável de controle caso o valor de entrada seja um número inteiro

valid = False  #variavel de controle
while not valid:
    # pergunta e valida triangulo par ou impar
    triangulo = input("Digite \"i\" para Triângulo impar ou \"p\" para triangulo par: ").lower()

    if((triangulo != "i") and (triangulo != "p")):   
        print("Resposta inválida!\n")
    else:
        valid = True
    
if(triangulo == "i"):
    n = 1
else:
    n = 2


produto = 1
# calcular e apresentar os valores na tela
for i in range(valor):
    produto *= n
    n += 2
    print(f"{i + 1}ª valor: {produto}")

