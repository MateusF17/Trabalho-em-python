numero = input("Digite um número inteiro de 4 dígitos (entre 1000 e 9999): ")

if len(numero) == 4 and numero.isdigit():
    for digito in numero:
        print(digito)
else:
    print("Por favor, insira um número de 4 dígitos válido.")
    