# agente_vr.py

import pandas as pd
from pathlib import Path

# --- CONFIGURAÇÃO ---
INPUT_DIR = Path("dados_entrada")


class AgenteVR:
    """
    Agente responsável por automatizar o cálculo e a geração do
    arquivo de compra de Vale Refeição.
    """
    def __init__(self, input_dir: Path):
        # Inicializa as variáveis que serão usadas
        self.input_dir = input_dir
        # self.arquivos_esperados foi removido daqui também.
        self.dados = {}
        self.status = "Iniciado"
        print(">> AgenteVR criado e pronto para a execução. <<")

    def _carregar_dados(self) -> bool:
        """
        (Método interno) Fase 2.1: Coleta os dados de TODOS os arquivos .xlsx
        encontrados no diretório de entrada.
        """
        print("\n--- [AGENTE] Iniciando Fase 2.1: Coleta de Dados Dinâmica ---")
        print(f"  -> Procurando por arquivos .xlsx na pasta '{self.input_dir}'...")
        try:
            # Usa o método .glob() para encontrar todos os arquivos que terminam com .xlsx
            arquivos_encontrados = list(self.input_dir.glob('*.xlsx'))
            
            if not arquivos_encontrados:
                print(f"  [ERRO] Nenhum arquivo Excel (.xlsx) foi encontrado na pasta '{self.input_dir}'.")
                return False

            # Itera sobre a lista de arquivos que foram encontrados
            for caminho in arquivos_encontrados:
                # O nome do arquivo sem a extensão (.xlsx) será usado como chave
                nome_base = caminho.stem
                self.dados[nome_base] = pd.read_excel(caminho)
                print(f"  [OK] Arquivo '{caminho.name}' carregado com sucesso.")

            self.status = "Dados Carregados"
            print("\n--- [AGENTE] Todos os arquivos encontrados foram carregados! ---")
            return True
        except Exception as e:
            print(f"\n!! [AGENTE] FALHA CRÍTICA DURANTE O CARREGAMENTO !!\n  {e}")
            self.status = f"Erro no carregamento: {e}"
            return False

    # --- MÉTODO DE EXECUÇÃO SIMPLIFICADO PARA TESTE ---
    def executar_carregamento(self):
        """ Método de teste que executa apenas o carregamento dos dados. """
        print("\n=========================================================")
        print("| [AGENTE] INICIANDO TAREFA DE TESTE: CARREGAR DADOS    |")
        print("=========================================================")
        
        self._carregar_dados()

# ======================================================================
# | PAINEL DE CONTROLE: PONTO DE ENTRADA DA EXECUÇÃO                   |
# ======================================================================
if __name__ == "__main__":
    # 1. Cria o agente, entregando a ele o caminho da pasta
    agente = AgenteVR(input_dir=INPUT_DIR)
    
    # 2. Executa APENAS a tarefa de carregamento de dados
    agente.executar_carregamento()