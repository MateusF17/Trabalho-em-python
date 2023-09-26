valor_hora = float(input("Digite o valor da hora de trabalho (em reais): "))

horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

valor_pago = valor_hora * horas_trabalhadas

valor_pago_com_adicional = valor_pago * 1.10

print("O valor a ser pago ao funcionário é:", valor_pago_com_adicional, "reais")