class TPS:
    def __init__(self, caminho):
        self.matriz_distancia  = self._carregar_matriz(caminho)
        
    def calcular_distancia(self, ponto_a, ponto_b):
        return self.matriz_distancia[ponto_a][ponto_b]
        
    def _carregar_matriz(self, caminho):
        matriz_aux = []
        try:
            with open(caminho, 'r') as arquivo:
                for linha in arquivo:
                    linha_limpa = linha.strip()
                    
                    if not linha_limpa:
                        continue
                    
                    valores = [float(x) for x in linha_limpa.replace(',', ' ').split()]
                    matriz_aux.append(valores)
                    
                return matriz_aux
        except FileNotFoundError:
            print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
            return []
    
    def exibir(self):
        for linha in self.matriz_distancia:
            print(linha)