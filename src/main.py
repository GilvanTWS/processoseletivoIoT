from machine import Pin
import time

# Pinos conectados aos LEDs do semáforo
led_vermelho = Pin(26, Pin.OUT)
led_amarelo  = Pin(27, Pin.OUT)
led_verde    = Pin(14, Pin.OUT)

def todos_apagados():
    # Garante que todos os LEDs estejam desligados antes de acender o próximo
    led_vermelho.off()
    led_amarelo.off()
    led_verde.off()

def estado_vermelho():
    todos_apagados()
    led_vermelho.on()
    time.sleep(5)  # Sinal vermelho dura 5 segundos

def estado_verde():
    todos_apagados()
    led_verde.on()
    time.sleep(4)  # Sinal verde dura 4 segundos

def estado_amarelo():
    todos_apagados()
    led_amarelo.on()
    time.sleep(2)  # Sinal amarelo dura 2 segundos — atenção, vai fechar!

# Mensagem inicial para confirmar que o sistema subiu corretamente
print("Teste")

# Loop principal: ciclo contínuo do semáforo
while True:
    estado_vermelho()
    estado_verde()
    estado_amarelo()