segundos = int(input("Digite um valor inteiro em segundos: "))

horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_finais = segundos_restantes % 60

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_finais)