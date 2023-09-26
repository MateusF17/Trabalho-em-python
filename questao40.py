valor_diario = 30.00

dias_trabalhados = int(input("Digite o número de dias trabalhados: "))

valor_bruto = dias_trabalhados * valor_diario

imposto_renda = 0.08 * valor_bruto

valor_liquido = valor_bruto - imposto_renda

print("A quantia líquida a ser paga é:", valor_liquido)