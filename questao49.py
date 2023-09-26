hora_inicio = int(input("Digite a hora de início (0-23): "))
minuto_inicio = int(input("Digite o minuto de início (0-59): "))
segundo_inicio = int(input("Digite o segundo de início (0-59): "))

duracao_segundos = int(input("Digite a duração em segundos: "))

segundo_termino = segundo_inicio + duracao_segundos
minuto_termino = minuto_inicio + segundo_termino // 60
hora_termino = hora_inicio + minuto_termino // 60

segundo_termino %= 60
minuto_termino %= 60
hora_termino %= 24

print("Horário de término da experiência:")
print("Hora:", hora_termino)
print("Minuto:", minuto_termino)
print("Segundo:", segundo_termino)