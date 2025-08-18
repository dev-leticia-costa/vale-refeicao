import pandas as pd

from pathlib import Path

# --- CONFIGURAÇÃO ---
# Pasta onde estão os seus arquivos Excel para unir.
PASTA_ENTRADA = Path("dados_entrada")
# Nome da coluna que servirá como chave para unir as tabelas.
COLUNA_CHAVE = 'matricula'

def analisar_planilhas():
    """
    Lê todos os arquivos .xlsx em uma pasta e gera um perfil detalhado de cada um.
    """
    print("--- Iniciando Análise e Perfilamento de Dados ---")

    # Garante que a pasta de entrada exista.
    PASTA_ENTRADA.mkdir(exist_ok=True)

    # Encontra todos os arquivos .xlsx na pasta de entrada.
    arquivos_excel = list(PASTA_ENTRADA.glob("*.xlsx"))

    if not arquivos_excel:
        print(f"\n[AVISO] Nenhum arquivo .xlsx encontrado na pasta '{PASTA_ENTRADA}'.")
        print("Por favor, adicione seus arquivos e execute o script novamente.")
        return

    # Itera sobre cada arquivo encontrado para analisá-lo individualmente.
    for caminho_arquivo in arquivos_excel:
        print(f"\n{'='*70}\nAnalisando o arquivo: {caminho_arquivo.name}\n{'='*70}")

        try:
            # Carrega a planilha para um DataFrame do pandas.
            df = pd.read_excel(caminho_arquivo)

            # 1. INFORMAÇÕES GERAIS
            print("\n[ 1. Informações Gerais ]")
            print(f"Dimensões: {df.shape[0]} linhas e {df.shape[1]} colunas.")
            print(f"AMOSTRA: {df.head()} ")

            # 2. RESUMO DAS COLUNAS (TIPO, NULOS, ETC.)
            print("\n[ 2. Resumo das Colunas ]")
            # Cria um DataFrame para sumarizar as informações de cada coluna.
            resumo = pd.DataFrame({
                'Tipo de Dado': df.dtypes,
                'Valores Nulos': df.isnull().sum(),
                '% Nulos': (df.isnull().sum() / df.shape[0]) * 100,
                'Valores Únicos': df.nunique()
                
            })
            print(resumo)
            print("-" * 70)
            print("\n[ 3. Estatísticas Descritivas ]")
            print(df.describe(include='all'))
            print("-" * 70)

        except Exception as e:
            print(f"\n[ERRO] Não foi possível processar o arquivo '{caminho_arquivo.name}': {e}")

    print(f"\n{'='*70}\nAnálise concluída para todos os arquivos.\n{'='*70}")

# Ponto de entrada do script
if __name__ == "__main__":
    analisar_planilhas()