comprimento_terreno = float(input("Digite o comprimento do terreno (metros): "))
largura_terreno = float(input("Digite a largura do terreno (metros): "))

preco_metro_tela = float(input("Digite o preço do metro de tela (por metro): "))

perimetro_terreno = 2 * (comprimento_terreno + largura_terreno)

custo_cercar_terreno = perimetro_terreno * preco_metro_tela

print("O custo para cercar o terreno com tela é de R$", custo_cercar_terreno)