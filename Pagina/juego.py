import random

# Esta función toma una lista de cartas y devuelve el valor total
# del juego del Siete y Medio.
def obtener_total(cartas):
  total = 0
  for carta in cartas:
    if carta == "A":
      total += 1
    elif carta in ["J", "Q", "K"]:
      total += 0.5
    else:
      total += int(carta)
  return total

# Esta función toma una lista de cartas y decide si el jugador ha ganado o perdido
def determinar_ganador(cartas):
  total = obtener_total(cartas)
  if total > 7.5:
    return "Perdiste"
  elif total == 7.5:
    return "Empate"
  else:
    return "Ganaste"

# Esta función simula el juego del Siete y Medio. El jugador comienza con una lista vacía de cartas
# y luego elige si quiere seguir pidiendo más cartas o si quiere plantarse. Si el total de sus cartas
# excede 7.5, entonces pierde automáticamente.
def jugar():
  cartas = []
  while True:
    decision = input("¿Quieres seguir pidiendo cartas o te plantas? (s/p) ")
    if decision == "s":
      carta = random.choice(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
      print(f"Pides a la banca: {carta}")
      cartas.append(carta)
      total = obtener_total(cartas)
      print(f"Total: {total}")
      if total > 7.5:
        print("Perdiste")
        break
    elif decision == "p":
      break
  
  resultado = determinar_ganador(cartas)
  print(resultado)

# Iniciamos el juego
jugar()
