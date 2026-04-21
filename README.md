# Semáforo com ESP32 – Intensivo Maker | IoT

## 👤 Identificação do Candidato

- **Nome completo:** Gilvan Alves Pastor Junior
- **GitHub:** GilvanTWS

---

## 1️⃣ Visão Geral da Solução

O projeto simula um semáforo de trânsito utilizando um microcontrolador ESP32 e três LEDs (vermelho, amarelo e verde). O sistema alterna automaticamente entre os estados do semáforo em um ciclo contínuo, respeitando tempos realistas para cada sinal.

---

## 2️⃣ Arquitetura do Sistema Embarcado

O programa segue um fluxo simples e direto:

- Ao iniciar, os três LEDs são configurados como saída digital
- O loop principal chama as funções de cada estado em sequência: vermelho → verde → amarelo → (repete)
- Cada função apaga todos os LEDs antes de acender o correspondente, evitando sobreposição de sinais
- O controle de tempo é feito com `time.sleep()`, simulando a duração real de cada fase do semáforo

  ## 3️⃣ Componentes Utilizados na Simulação

| Componente | ID | Função |
|---|---|---|
| ESP32 DevKit C v4 | esp | Microcontrolador principal |
| LED vermelho | led1 | Indica sinal de parada |
| LED amarelo | led2 | Indica sinal de atenção |
| LED verde | led3 | Indica sinal de passagem |
| Resistor 220Ω | r1, r2, r3 | Proteção dos LEDs contra sobrecorrente |
