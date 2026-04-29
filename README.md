# Semáforo com ESP32 – Intensivo Maker | IoT

## 👤 Identificação do Candidato

- **Nome completo:** Gilvan Alves Pastor Junior

---

## 1️⃣ Visão Geral da Solução

O projeto simula um semáforo de trânsito utilizando um microcontrolador ESP32 e três LEDs (vermelho, amarelo e verde). O sistema alterna automaticamente entre os estados do semáforo em um ciclo contínuo, utilizando uma máquina de estados com temporização não-bloqueante — ou seja, o microcontrolador nunca fica travado esperando, podendo responder a outros eventos enquanto controla o semáforo.

---

## 2️⃣ Arquitetura do Sistema Embarcado

O programa é estruturado como uma **máquina de estados finitos** com três estados: `vermelho`, `verde` e `amarelo`. A transição entre estados é controlada por temporização não-bloqueante usando `time.ticks_ms()`.

**Fluxo principal:**

1. Os pinos dos LEDs são configurados como saída digital
2. O primeiro estado (`vermelho`) é ativado e o tempo de início é registrado
3. No loop principal, o tempo atual é comparado com o tempo de início usando `time.ticks_diff()`
4. Quando o tempo do estado atual expira, o sistema avança para o próximo estado automaticamente
5. O ciclo se repete indefinidamente: vermelho → verde → amarelo → vermelho...

**Por que temporização não-bloqueante?**
O uso de `time.sleep()` trava completamente o processador durante a espera. Com `ticks_ms()`, o loop continua rodando e o sistema pode ser expandido para reagir a botões ou sensores sem perder o controle do semáforo.

---

## 3️⃣ Componentes Utilizados na Simulação

| Componente | ID | Pino | Função |
|---|---|---|---|
| ESP32 DevKit C v4 | esp | — | Microcontrolador principal |
| LED vermelho | led_vermelho | GPIO 26 | Indica sinal de parada |
| LED amarelo | led_amarelo | GPIO 27 | Indica sinal de atenção |
| LED verde | led_verde | GPIO 14 | Indica sinal de passagem |
| Resistor 220Ω | r1, r2, r3 | — | Proteção dos LEDs contra sobrecorrente |

---

## 4️⃣ Decisões Técnicas Relevantes

- **Máquina de estados:** cada estado do semáforo é representado por uma string em uma lista (`ESTADOS`), e o índice atual avança ciclicamente com operador módulo (`% len(ESTADOS)`), tornando fácil adicionar novos estados
- **Temporização não-bloqueante:** `time.ticks_diff()` calcula a diferença de tempo de forma segura, evitando problemas de overflow do contador interno do MicroPython
- **Constantes de tempo:** os valores `TEMPO_VERMELHO`, `TEMPO_VERDE` e `TEMPO_AMARELO` são definidos no topo do arquivo, facilitando ajustes sem alterar a lógica
- **Função `todos_apagados()`:** centraliza o desligamento dos LEDs antes de cada transição, garantindo que nunca dois LEDs fiquem acesos simultaneamente
- **IDs descritivos no circuito:** os componentes no `diagram.json` usam nomes como `led_vermelho` em vez de `led1`, tornando o circuito mais legível e alinhado com o código

---

## 5️⃣ Resultados Obtidos

O sistema funciona corretamente na simulação do Wokwi. O ciclo do semáforo alterna entre os três estados de forma contínua e sem travamentos. O pipeline do GitHub Actions executa a simulação e valida a saída com sucesso, confirmando o funcionamento do projeto no ambiente de CI.

A cada transição de estado, o sistema imprime no monitor serial o estado atual, permitindo acompanhar o fluxo em tempo real.

---

## 6️⃣ Comentários Adicionais

**Dificuldades encontradas:** o principal desafio foi entender a diferença entre temporização bloqueante e não-bloqueante, e como estruturar o código em torno de uma máquina de estados ao invés de um fluxo linear com `sleep`.

**Limitações:** o timeout de 10 segundos do ambiente de CI limita a duração da simulação, o que exigiu ajustar os tempos de cada estado para que o pipeline consiga validar o projeto dentro do prazo.

**Melhorias futuras:** com mais tempo, seria interessante adicionar um botão de pedestre que força o sinal vermelho ao ser pressionado, e um display LCD mostrando o tempo restante de cada fase — ambas as funcionalidades seriam naturalmente suportadas pela arquitetura de máquina de estados já implementada.