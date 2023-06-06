# 24.Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
import random

def roll_die():
    return random.randint(1, 6)

results = [0] * 6

for _ in range(100):
    roll = roll_die()
    results[roll - 1] += 1

for i in range(6):
    print(f"Valor {i+1}: {results[i]} vezes")
