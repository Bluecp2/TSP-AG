import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import product
import statistics
import os

from src.AG import AG
from src.TSP import TSP

class Experimento:
    def __init__(self, caminho_instancia, n_execucoes=20, n_geracoes=20):
        self.tsp = TSP(caminho_instancia)
        self.n_execucoes = n_execucoes
        self.n_geracoes = n_geracoes
        
        # Fatores definidos no roteiro
        self.fatores = {
            'populacao' : [50, 100],
            'taxa_cruzamento' : [0.8, 0.9],
            'taxa_mutacao' : [0.01, 0.05],
            'operador' : ['OX', 'PMX']
        }
        
        self.dados_tabela = [] 
        self.dados_brutos_boxplot = []
        self.convergencia_global = {}
        self.melhor_absoluto = None
        
    def rodar(self):
        combinacoes = list(product(*self.fatores.values()))
        coluna_fatores = list(self.fatores.keys())
        
        print(f"Iniciando Teste Fatorial: 16 configs x {self.n_execucoes} execuções.")
        
        for i, valores in enumerate(combinacoes):
            config = dict(zip(coluna_fatores, valores))
            id_config = f"C{i+1}"
            print(f"Configuração {id_config}: {config}")
            
            fitness_por_execucao = []
            matriz_convergencia = np.zeros((self.n_execucoes, self.n_geracoes))
            
            for rodada in range(self.n_execucoes):
                ga = AG(
                    tamanho_pop=config['populacao'],
                    taxa_cruzamento=config['taxa_cruzamento'],
                    taxa_mutacao=config['taxa_mutacao'],
                    operador=config['operador'],
                    tsp_instancia=self.tsp
                )
                
                for gen in range(self.n_geracoes):
                    ga.evolucao()
                    melhor_da_gen = min(ga.populacao, key=lambda ind: ind.fitness)
                    matriz_convergencia[rodada, gen] = melhor_da_gen.fitness
                    
                    # Salva o recorde absoluto de todo o experimento
                    if self.melhor_absoluto is None or melhor_da_gen.fitness < self.melhor_absoluto.fitness:
                        from src.Individuo import Individuo
                        self.melhor_absoluto = Individuo(melhor_da_gen.rota[:], self.tsp)
                
                # Coleta resultado final da rodada
                melhor_final = matriz_convergencia[rodada, -1]
                fitness_por_execucao.append(melhor_final)
                
                self.dados_brutos_boxplot.append({
                    'Config': id_config,
                    'Fitness': melhor_final,
                    'Operador': config['operador']
                })
            
            self.convergencia_global[id_config] = np.mean(matriz_convergencia, axis=0)
            
            self.dados_tabela.append({
                'ID': id_config,
                'Operador': config['operador'],
                'Pop': config['populacao'],
                'TX_C': config['taxa_cruzamento'],
                'TX_M': config['taxa_mutacao'],
                'Melhor': min(fitness_por_execucao),
                'Pior': max(fitness_por_execucao),
                'Média': statistics.mean(fitness_por_execucao),
                'Mediana': statistics.median(fitness_por_execucao),
                'Desvio Padrão': statistics.stdev(fitness_por_execucao)
            })

        df_tabela = pd.DataFrame(self.dados_tabela)
        df_tabela.to_csv("resultados_fatorial_completo.csv", index=False, sep=';')
        return df_tabela
    
    def gerar_graficos(self):
        df_box = pd.DataFrame(self.dados_brutos_boxplot)

        plt.figure(figsize=(12, 6))
        sns.boxplot(x='Config', y='Fitness', hue='Operador', data=df_box)
        plt.title("Boxplot: Dispersão por Configuração")
        plt.savefig("boxplot_final.png")
        plt.show()

        plt.figure(figsize=(12, 6))
        sns.barplot(x='Config', y='Fitness', data=df_box, capsize=.1)
        plt.title("Média e Desvio Padrão por Configuração")
        plt.savefig("barras_media.png")
        plt.show()

        plt.figure(figsize=(12, 6))
        for id_config, valores in self.convergencia_global.items():
            plt.plot(valores, label=id_config)
        plt.title("Evolução da Convergência (Média das 20 execuções)")
        plt.xlabel("Geração")
        plt.ylabel("Melhor Fitness")
        plt.legend(loc='upper right', ncol=2)
        plt.savefig("convergencia_final.png")
        plt.show()