import os
from src.Experimento import Experimento

def main(): 
    caminho_instancia = os.path.join("data", "/home/gabriel/Documentos/GitHub/TSP-AG/dados/att48_d.txt")
    
    num_execucoes = 50
    num_geracoes = 200
    
    print("="*120)
    print(f"ALGORITMO GENÉTICO - TESTE FATORIAL TSP")
    print(f"Instância: {caminho_instancia}")
    print(f"Planejamento: 16 configurações x {num_execucoes} execuções")
    print("="*120)
    
    exp = Experimento(
        caminho_instancia=caminho_instancia, 
        n_execucoes=num_execucoes, 
        n_geracoes=num_geracoes
    )
    
    tabela_final = exp.rodar()
    exp.gerar_graficos()
    
    caminho_instancia = os.path.join("data", "/home/gabriel/Documentos/GitHub/TSP-AG/dados/fri26_d.txt")
    print("="*120)
    print(f"ALGORITMO GENÉTICO - TESTE FATORIAL TSP")
    print(f"Instância: {caminho_instancia}")
    print(f"Planejamento: 16 configurações x {num_execucoes} execuções")
    print("="*120)
    exp = Experimento(
        caminho_instancia=caminho_instancia, 
        n_execucoes=num_execucoes, 
        n_geracoes=num_geracoes
    )
    tabela_final = exp.rodar()
    exp.gerar_graficos()
    
if __name__ == "__main__":
    main()