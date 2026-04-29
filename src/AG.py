from typing import list
from src.Individuo import Individuo
import random

class AG:
    
    def __init__(self, tamanho_pop, taxa_cruzamento, taxa_mutacao, operador):
        self.tamanho_pop = tamanho_pop
        self.taxa_cruzamento = taxa_cruzamento
        self.taxa_mutacao = taxa_mutacao
        self.operador = operador
    
    def torneio(self, populacao, k=3):
        competidores = random.sample(populacao, k)
        vencedor = min(competidores, key=lambda ind: ind.fitness)
        
        return vencedor
    
    def sorteia_corte(self, tamanho_rota):
        pontos = random.sample(range(tamanho_rota), 2)
        pontos.sort()
        return pontos[0], pontos[1]
        
    def OX(self, pai1, pai2, tamanho_rota):
        inicio, fim = self.sorteia_corte(tamanho_rota)
        filho = [-1] * tamanho_rota #cria o vetor filho
        
        filho[inicio:fim + 1] = pai1[inicio:fim + 1] #faz a copia do segmento sorteado
        segmento_herdado = set(filho[inicio:fim + 1])
        
        posicao_filho = (fim + 1) % tamanho_rota #implementa a logica circular
        posicao_pai2 = (fim + 1) % tamanho_rota

        while -1 in filho:
            cidade = pai2[posicao_pai2] #salva em cidade  a cidade do indice que esta no pa12
            
            if cidade not in segmento_herdado: #verifica se nao e repetido
                filho[posicao_filho] = cidade
                posicao_filho = (posicao_filho + 1) % tamanho_rota #avança o indice
            
            (posicao_pai2 + 1) % tamanho_rota #avança sempre para testar novos indices
        
        return filho