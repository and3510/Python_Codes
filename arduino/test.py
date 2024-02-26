import pyfirmata
import time

# Define a porta serial
port = '/dev/ttyACM0'

# Conecta ao Arduino
board = pyfirmata.Arduino(port)

# Define o pino do LED
led_pin = board.get_pin('d:8:o')
buzz_pin = board.get_pin('d:7:o')

while True:
  # Liga o LED
  led_pin.write(1)
  buzz_pin.write(1)
  time.sleep(1)
  print("Ola")

  # Desliga o LED
  led_pin.write(0)
  buzz_pin.write(0)
  time.sleep(1)
  print("Mundo!")
