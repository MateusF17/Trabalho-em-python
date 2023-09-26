altura_degrau = float(input("Digite a altura do degrau da escada: "))
altura_objetivo = float(input("Digite a altura que você deseja alcançar: "))

degraus_necessarios = altura_objetivo / altura_degrau

print("Você precisará subir", int(degraus_necessarios), "degraus para atingir seu objetivo.")