valor_apostador1 = float(input("Digite o valor investido pelo primeiro apostador: "))
valor_apostador2 = float(input("Digite o valor investido pelo segundo apostador: "))
valor_apostador3 = float(input("Digite o valor investido pelo terceiro apostador: "))

valor_premio = float(input("Digite o valor total do prêmio: "))

total_investido = valor_apostador1 + valor_apostador2 + valor_apostador3
proporcao_apostador1 = valor_apostador1 / total_investido
proporcao_apostador2 = valor_apostador2 / total_investido
proporcao_apostador3 = valor_apostador3 / total_investido

ganho_apostador1 = proporcao_apostador1 * valor_premio
ganho_apostador2 = proporcao_apostador2 * valor_premio
ganho_apostador3 = proporcao_apostador3 * valor_premio

print("O primeiro apostador ganharia:", ganho_apostador1)
print("O segundo apostador ganharia:", ganho_apostador2)
print("O terceiro apostador ganharia:", ganho_apostador3)