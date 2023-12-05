#automata_pila.py
class Estado:
  Q0, Q1, Q2 = range(3)

class Simbolo:
  A, B, Z = 'a', 'b', 'Z'

class PilaAutomata:
  def __init__(self):
      self.pila = [Simbolo.Z]

  def apilar(self, simbolo):
      self.pila.append(simbolo)

  def desapilar(self):
      return self.pila.pop()

def automata_pila_ab(input_string):
  pos = 0
  actual = Estado.Q0
  pila_automata = PilaAutomata()

  while pos < len(input_string):
      simbolo = input_string[pos]

      if actual == Estado.Q0:
          if simbolo == Simbolo.A:
              pila_automata.apilar(Simbolo.A)
              actual = Estado.Q1
          elif simbolo == Simbolo.B:
              pila_automata.apilar(Simbolo.B)
              actual = Estado.Q2
          else:
              break  # Rechazar si no comienza con 'a' o 'b'

      elif actual == Estado.Q1:
          if simbolo == Simbolo.A:
              pila_automata.apilar(Simbolo.A)
          elif simbolo == Simbolo.B:
              pila_automata.desapilar()
              actual = Estado.Q2
          else:
              break  # Rechazar si se encuentra un símbolo que no es 'a' o 'b'

      elif actual == Estado.Q2:
          if simbolo == Simbolo.B:
              pila_automata.apilar(Simbolo.B)
          elif simbolo == Simbolo.A:
              pila_automata.desapilar()
              actual = Estado.Q1
          else:
              break  # Rechazar si se encuentra un símbolo que no es 'a' o 'b'

      pos += 1

  if actual in [Estado.Q1, Estado.Q2] and len(pila_automata.pila) == 1 and pila_automata.pila[0] == Simbolo.Z:
      return True  # Aceptar si se llega al final de la cadena y la pila está vacía excepto por Z
  else:
      return False  # Rechazar en otros casos
