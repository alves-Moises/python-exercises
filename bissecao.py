#               Metodo de Bisseccao                   

import math


def f(x):
    return x** 2 - 5
    
def main():

    # valores do intevalo
    a = int(input("Dgite o primeiro valor:"))
    b = int(input("Dgite o segundo valor:"))
    e = 0.01 
    
    i = 1 # contador
    if f((a) * f(b) < 0):
        while(math.fabs(b -a) / 2 > e):
            i += 1
            xi= (a+b) / 2
            
            if f(xi) == 0:
                print("\nA raiz é: ", xi)
                break
            else:
                if f(a) * f(xi) < 0:
                    b = xi
                else:
                    a = xi
            print(f"{f'|| valor atual: {xi}':<30} ||  Contador: {i} ")
        print("\nValor da raiz é: ", xi)

    else:
        print("\nNão há raiz nesse intervalo")

    print(f"Total de iterações: {i}")
if __name__ == "__main__":
    main()