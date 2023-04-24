def cal_fat(x):
    fatorial = 1 # valor inicial 

    # calculando o fatorial de x
    for i in range(x):
        fatorial *= (i + 1)

    return fatorial

def main():
    valid = False  # variavel de controle

    # validacao de input inteiro
    while not valid:
        try:
            n = int(input("Digite um valor:"))
        except ValueError:
            print("Digite um valor inteiro!")
        else:
            # verificando se digitou um valor maior que zero
            if(n <= 0):
                print("Valor inválido")
            else:
                valid =True


    # variaveis que vamos usar dentro do for
    h = 0
    temp = int()

    # aplicação da formula
    for i in range(n):
        cont = i + 1   # contador

        # variaveis para calculo
        numerador = cont
        denominador =  (n - cont + 1) ** cal_fat(cont)


        if n == cont:   # ultimo termo, denomiador == 1
            denominador = 1
        
        # primeiro elemento
        if cont == 1:
            h = 1 / n

        # se for elemento de numero par, subtrai
        elif cont % 2 == 0: 
            h -= numerador / denominador

        # senão, soma
        else:
            h += numerador / denominador

    print(f"resultado: {h}")

#============= INICIO =============
if __name__ == "__main__":
    main()