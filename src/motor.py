from typing import list
from src.Individuo import Individuo
import random

class motor:
    
    def __init__(self, tamanho_pop, taxa_cruzamento, taxa_mutacao, operador):
        self.tamanho_pop = tamanho_pop
        self.taxa_cruzamento = taxa_cruzamento
        self.taxa_mutacao = taxa_mutacao
        self.operador = operador
    
    def torneio(self, populacao, k=3):
        competidores = random.sample(populacao, k)
        vencedor = min(competidores, key=lambda ind: ind.fitness)
        
        return vencedor
    
            