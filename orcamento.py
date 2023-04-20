def calculaMaodeObra(pedreiro, eletricista, tec_ar, pintor):
    # mao de obra -> calculado peela soma da diária de cada profissional envolvido

    # valor da diaria de cada profissional
    dia_pedreiro = 11.0
    dia_eletrcista = 13
    dia_tec_ar = 15.0
    dia_pintor = 12
    dia_ajudante = 5

    # valor total de cada profissional em singular
    total_pedreiro = pedreiro * dia_pedreiro
    total_eletricista = eletricista * dia_eletrcista
    total_tec_ar = tec_ar * dia_tec_ar
    total_pintor = pintor * dia_pintor

    total_ajudante = pedreiro + eletricista + tec_ar + pintor # cada profissional precisa de um ajdante
    valor_total_ajudante = total_ajudante * dia_ajudante      # calculo o custo toal de ajudante

    # imprime informacoes sobre o valor da mão de obra de cada profissional
    print("=" * 20)
    print("Valor total de cada profssional:")
    print(f"Total do pedreiro: R${float(total_pedreiro)}")
    print(f"Total do eletricista: R${float(total_eletricista)}")
    print(f"Total do tecnico em ar: R${float(total_tec_ar)}")
    print(f"Total do pintor: R${float(total_pintor)}")
    print(f"total do ajudante: R${float(total_ajudante)}")
    print("=" * 20)

    # somatorio total
    total = total_pedreiro + total_eletricista + total_tec_ar + total_pintor + valor_total_ajudante

    return total #retorna o valor total do custo
    

def calculaTipoResidencia(tipo_residencia, area):
    # valores:
    casa =  40  # R$40,00/m
    apt = 50    # R$50,00/n

    # calcula de acoro com o tipo de residencia
    if(tipo_residencia == "c"):
        obra_bruta = area * casa
    else:
        obra_bruta = area * apt

    return obra_bruta #retorna o valor total


def main():


    #  pega o valor da area em m³
    valid = False  # variavel de controle
    while not valid:
        #recebe o valor e valida o tipo inteiro
        try:
            area = float(input("DIgite o valor a área:"))
        except ValueError:
            print("Digite um valor válido!")
        else:
            valid = True  #muda valor da variável de controle caso o valor de entrada seja inteiro ou decimal econtinua o programa


    valid = False # variavel de controle
    while not valid:
        construcao = input("Digite o tipo de construcao: \n\"A\" para apartamento\n\"C\" para casa:\n").lower()
        if ((construcao != "a") and (construcao != "c")):
            print("Responsta inválida. Digite apenas uma letra correspondente!")
        else:
            valid = True
        
    # ================ Pega horas para cada profssional =======================
    pedreiro = int(input("Digite o total de horas para o pedreiro:"))
    eletricista = int(input("Digite o total de horas para o eletricista:"))
    tec_ar = int(input("Digite o total de horas para o tecnico em ar condicionado:"))
    pintor = int(input("Digite o total de horas para o pintor:"))
    
    # calcula mao de obra
    mao_de_obra = calculaMaodeObra(pedreiro, eletricista, tec_ar, pintor)
    
    #calcula obra bruta
    obra_bruta = calculaTipoResidencia(construcao, area)


    
    

    valor_orcamento = mao_de_obra + obra_bruta


    print("\n\n\n")
    print("Relatório:")
    print(f"Total de horas com pedreiro: {pedreiro}")
    print(f"Total de horas com eletricista: {eletricista}")
    print(f"Total de horas com técnico em ar: {tec_ar}")
    print(f"Total de horas com pintor: {pintor}")
    print("=" * 20)
    print(f"TOTAL: R${valor_orcamento}")

if __name__ == "__main__":
    main()