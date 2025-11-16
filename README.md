# Proyecto No. 3 - Teoría de la computación
En este proyecto se debe desarrollar una maquina de turing en el lenguaje de programación de elección, donde se pase mediante archivos .yaml el lenguaje que debe reconocer y las cadenas que debe evaluar. Estas máquinas deben ser de una sola cadena.

## Como ejecutar el código:
python main.py

## Requisitos:
- Python 3.x
- Librería PyYAML

# Lenguajes Utilizados
## Maquina reconocedora:
La máquina reconoce cadenas donde lo que está antes de # es exactamente igual a lo que está después de #

### Ejemplos que se utilizaron en la ejecución:
Aceptadas:
  - "ab#ab"
  - "aab#aab"
  - "bba#bba"

Rechazadas
  - "ab#ba"
  - "aaa#aa"
  - "ab#abbb"

## Maquina alternadora:
La máquina toma una cadena de entrada w sobre {a,b}, y construye en la misma cinta una nueva forma w#w^R, donde w^R es la reversa de w.

### Ejemplos que se utilizaron en la ejecución:
  - "aaabb"
  - "aababb"
  - "abbaba"
  - "bbbaa"
  - "ababab"
  - "baabaa"

## Vinculo al video explicativo:
[Video Demostrativo](youtube.com)