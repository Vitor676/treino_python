# Função para calcular o salário com aumento
def calcular_salario_com_aumento(salario_atual, porcentagem_aumento):
    return salario_atual + (salario_atual * (porcentagem_aumento / 100))

# Função para validar a entrada do usuário


def validar_entrada(valor):
    return valor > 0

# Função principal


def main():
    try:
        # Solicitar entrada do usuário
        salario_atual = float(input("Por favor, informe seu salário atual: "))
        porcentagem_aumento = float(
            input("Digite a porcentagem do aumento que deseja aplicar: "))

        # Validar entradas
        if validar_entrada(salario_atual) and validar_entrada(porcentagem_aumento):
            # Calcular o salário final
            salario_final = calcular_salario_com_aumento(
                salario_atual, porcentagem_aumento)

            # Exibir o resultado
            print(
                f"Ótima notícia! Seu novo salário, após o aumento, será: R$ {salario_final:.2f}")
        else:
            print("Insira valores válidos.")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")


# Executar o programa
if __name__ == "__main__":
    main()
