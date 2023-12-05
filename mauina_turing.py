#maquina_turing.py
class TuringMachine:
  def __init__(self, tape):
      self.tape = list(tape)
      self.head = 0
      self.state = 'q0'

  def transition(self, symbol):
      if self.state == 'q0':
          if symbol == '0':
              self.tape[self.head] = '1'
              self.head += 1
          elif symbol == '1':
              self.tape[self.head] = '0'
              self.head += 1
          elif symbol == '_':
              self.state = 'q_accept'
          else:
              self.state = 'q_reject'
      elif self.state == 'q_accept':
          pass  # Máquina en estado de aceptación, no realiza más transiciones
      else:
          self.state = 'q_reject'  # En caso de que se encuentre un símbolo inesperado

  def run(self):
      while self.state not in ['q_accept', 'q_reject']:
          symbol = self.tape[self.head] if self.head < len(self.tape) else '_'
          self.transition(symbol)

  def display_tape(self):
      return "".join(self.tape[:-1])  # Excluye el último símbolo (espacio en blanco) al mostrar la cinta


def ejecutar_maquina_turing(input_string):
  input_tape = '0' + input_string + '_'
  tm = TuringMachine(input_tape)
  tm.run()
  resultado = tm.display_tape()

  if tm.state == 'q_accept':
      return f"Resultado: {resultado}\nOperación completada."
  else:
      return "La máquina de Turing entró en un estado de rechazo."

if __name__ == "__main__":
  input_string = input("Ingrese una cadena binaria: ")
  print(ejecutar_maquina_turing(input_string))
