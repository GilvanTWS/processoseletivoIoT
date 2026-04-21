from machine import Pin
import time

# Definição dos pinos dos LEDs
led_vermelho = Pin(26, Pin.OUT)
led_amarelo  = Pin(27, Pin.OUT)
led_verde    = Pin(14, Pin.OUT)

def todos_apagados():
    led_vermelho.off()
    led_amarelo.off()
    led_verde.off()

def estado_vermelho():
    todos_apagados()
    led_vermelho.on()
    time.sleep(5)

def estado_verde():
    todos_apagados()
    led_verde.on()
    time.sleep(4)

def estado_amarelo():
    todos_apagados()
    led_amarelo.on()
    time.sleep(2)

print("Teste")

while True:
    estado_vermelho()
    estado_verde()
    estado_amarelo()