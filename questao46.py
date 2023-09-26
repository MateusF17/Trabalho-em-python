numero_lido = int(input("Digite um número inteiro de três dígitos (entre 100 e 999): "))

if 100 <= numero_lido <= 999:
    centenas = numero_lido // 100
    dezenas = (numero_lido % 100) // 10
    unidades = numero_lido % 10
    numero_gerado = unidades * 100 + dezenas * 10 + centenas
    print("Número Gerado:", numero_gerado)
else:
    print("Por favor, insira um número de três dígitos válido.")