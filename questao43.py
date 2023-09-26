valor_total = float(input("Digite o valor total da venda: "))

valor_com_desconto = valor_total * 0.90

valor_parcela = valor_total / 3

comissao_vista = valor_com_desconto * 0.05

comissao_parcelada = valor_total * 0.05

print("Total a pagar com desconto de 10%:", valor_com_desconto)
print("Valor de cada parcela (3× sem juros):", valor_parcela)
print("Comissão do vendedor (venda à vista):", comissao_vista)
print("Comissão do vendedor (venda parcelada):", comissao_parcelada)
