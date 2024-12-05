horaInicio = float(input("Hora inicial: "))
horaFim = float(input("Hora final: "))

if horaInicio < horaFim:
    duracao = horaFim - horaInicio
else:
    duracao = 24 - horaInicio + horaFim

print(f"O jogo durou: {duracao:.2f} hora(s)")