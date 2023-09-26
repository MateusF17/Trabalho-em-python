letra_maiuscula = input("Digite uma letra maiúscula: ")

if len(letra_maiuscula) == 1 and 'A' <= letra_maiuscula <= 'Z':
     letra_minuscula = chr(ord(letra_maiuscula) + 32)
     print("A letra minúscula correspondente é:", letra_minuscula)
else:
    print("Por favor, insira uma única letra maiúscula válida.")