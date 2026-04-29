from machine import Pin
import time

# Pinos conectados aos LEDs do semáforo
led_vermelho = Pin(26, Pin.OUT)
led_amarelo  = Pin(27, Pin.OUT)
led_verde    = Pin(14, Pin.OUT)

# Duração de cada estado em milissegundos
TEMPO_VERMELHO = 3000
TEMPO_VERDE    = 2000
TEMPO_AMARELO  = 1000

# Estados possíveis do semáforo
ESTADOS = ["vermelho", "verde", "amarelo"]
estado_atual = 0

def todos_apagados():
    # Apaga todos os LEDs antes de acender o próximo
    led_vermelho.off()
    led_amarelo.off()
    led_verde.off()

def ativar_estado(estado):
    # Acende o LED correspondente ao estado atual
    todos_apagados()
    if estado == "vermelho":
        led_vermelho.on()
    elif estado == "verde":
        led_verde.on()
    elif estado == "amarelo":
        led_amarelo.on()

print("Teste")

# Inicializa o primeiro estado
ativar_estado(ESTADOS[estado_atual])
tempo_inicio = time.ticks_ms()

# Loop principal com temporização não-bloqueante
while True:
    agora = time.ticks_ms()
    duracao = [TEMPO_VERMELHO, TEMPO_VERDE, TEMPO_AMARELO][estado_atual]

    # Verifica se o tempo do estado atual já passou
    if time.ticks_diff(agora, tempo_inicio) >= duracao:
        estado_atual = (estado_atual + 1) % len(ESTADOS)
        ativar_estado(ESTADOS[estado_atual])
        tempo_inicio = time.ticks_ms()
        print("Estado:", ESTADOS[estado_atual])