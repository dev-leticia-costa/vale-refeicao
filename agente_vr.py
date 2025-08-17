import pandas as pd
import unicodedata
from pathlib import Path

# --- CONFIGURAÇÃO ---
INPUT_DIR = Path("dados_entrada")

class AgenteVR:
    """
    Agente responsável por automatizar o cálculo e a geração do
    arquivo de compra de Vale Refeição.
    """
    def __init__(self, input_dir: Path):
        self.input_dir = input_dir
        self.dados = {}
        self.status = "Iniciado"
        print(">> AgenteVR criado e pronto para a execução. <<")

    def _normalizar_nome(self, texto: str) -> str:
        texto_str = str(texto)
        texto_normalizado = ''.join(
            c for c in unicodedata.normalize('NFD', texto_str)
            if unicodedata.category(c) != 'Mn'
        )
        return texto_normalizado.lower().replace(' ', '').replace('_', '')

    def _carregar_dados(self) -> bool:
        print("\n--- [FASE 1] Iniciando Carregamento de Dados ---")
        print(f" -> Procurando por arquivos .xlsx na pasta '{self.input_dir}'...")
        
        self.input_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            arquivos_encontrados = list(self.input_dir.glob('*.xlsx'))
            
            if not arquivos_encontrados:
                print(f" [AVISO] Nenhum arquivo Excel (.xlsx) foi encontrado na pasta '{self.input_dir}'.")
                self.status = "Finalizado sem dados"
                return False

            for caminho in arquivos_encontrados:
                nome_base = self._normalizar_nome(caminho.stem)
                self.dados[nome_base] = pd.read_excel(caminho)
                print(f" [OK] Arquivo '{caminho.name}' carregado com dados brutos.")

            self.status = "Dados Carregados"
            print("--- [FASE 1] Todos os arquivos foram carregados com sucesso! ---")
            return True
            
        except Exception as e:
            print(f"\n!! [ERRO CRÍTICO] Falha durante o carregamento de arquivos: {e} !!")
            self.status = f"Erro no carregamento: {e}"
            return False

    # MÉTODO ATUALIZADO PARA REALIZAR A NORMALIZAÇÃO
    def _preparar_dados(self):
        """
        Executa a limpeza e padronização dos dados, incluindo a normalização
        dos nomes das colunas de todas as tabelas carregadas.
        """
        print("\n--- [FASE 2] Iniciando Preparação e Normalização de Dados ---")
        if not self.dados:
            print(" -> Nenhum dado para preparar.")
            return

        print(" -> Normalizando nomes das colunas de todas as tabelas...")
        for nome_tabela, dataframe in self.dados.items():
            # Esta linha substitui a lista de colunas atual por uma nova,
            # onde cada nome de coluna foi passado pela função de normalização.
            dataframe.columns = [self._normalizar_nome(col) for col in dataframe.columns]
            print(f"    - Tabela '{nome_tabela}': colunas normalizadas.")

        self.status = "Dados Preparados"
        print("--- [FASE 2] Preparação de dados concluída. ---")
        print("\n--- [AGENTE] Iniciando Fase 3: Preparação dos Dados ---")




    def inspecionar_dados(self):
        """
        Imprime a estrutura ATUAL dos dados (pós-processamento), mostrando 
        os nomes de colunas já normalizados.
        """
        print("\n--- [INSPEÇÃO] Verificando estrutura dos dados processados ---")
        
        if not self.dados:
            print(" -> Nenhum dado para inspecionar.")
            return

        print(" -> Estrutura final encontrada:")
        for nome_tabela, dataframe in self.dados.items():
            print(f"\n  [Tabela: {nome_tabela}]")
            print(f"    - Dimensões: {dataframe.shape[0]} linhas, {dataframe.shape[1]} colunas")
            print(f"    - Colunas (Normalizadas): {dataframe.columns.tolist()}")
            print(f"    - Colunas (Normalizadas): {dataframe.head()}")
            print(f"    - Colunas (Normalizadas): {dataframe.info()}")
            
        print("\n--- [INSPEÇÃO] Fim da verificação ---")

    def _consolidar_dados(self):
        """
        [FASE 3] Consolida as tabelas de Ativos, Férias, Desligados e Admissão
        em uma única base de dados, usando 'matricula' como chave.
        """
        print("\n--- [FASE 3] Iniciando Consolidação dos Dados ---")
        
        # --- ETAPA 1: Definições e Verificações ---
        chave_primaria = 'matricula'
        
        # Nomes normalizados das tabelas que vamos usar
        tabela_base_nome = 'ativos'
        nomes_para_juntar = ['ferias', 'desligados', 'admissaoabril']
        if tabela_base_nome not in self.dados:
            print(f"  [ERRO CRÍTICO] A tabela base '{tabela_base_nome}' não foi encontrada. A consolidação não pode continuar.")
            return
        df_consolidado = self.dados[tabela_base_nome].copy()
        print(f" -> Base inicial '{tabela_base_nome}' definida com {len(df_consolidado)} registros {df_consolidado.shape[1]} colunas.")
        # Loop para juntar as outras tabelas
        for nome_tabela in nomes_para_juntar:
            # Verifica se a tabela da vez existe nos dados carregados
            if nome_tabela in self.dados:
                print(f"   -> Juntando dados da tabela '{nome_tabela}'...")
                
                tabela_para_juntar = self.dados[nome_tabela]
                
                # Verifica se a tabela tem a chave primária antes de juntar
                if chave_primaria in tabela_para_juntar.columns:
                    df_consolidado = df_consolidado.merge(
                        tabela_para_juntar,
                        on=chave_primaria,
                        how='left' # 'left' para manter todos da tabela de ativos
                    )
                else:
                    print(f"   [AVISO] A tabela '{nome_tabela}' foi pulada pois não contém a chave '{chave_primaria}'.")
            else:
                print(f"   [AVISO] A tabela '{nome_tabela}' não foi encontrada nos dados carregados e será pulada.")
    # --- ETAPA 3: Armazenamento e Verificação ---
        # Armazena o resultado final em um novo atributo do agente
        self.df_consolidado = df_consolidado
        
        print("--- [FASE 3] Consolidação concluída com sucesso! ---")
        print("\n -> Verificando o resultado da consolidação...")
        print("   Amostra da Tabela Consolidada:")
        print(self.df_consolidado.head())
        print(f"\n   Tabela final criada com {self.df_consolidado.shape[0]} linhas e {self.df_consolidado.shape[1]} colunas.")

    def executar(self):
        """
        Orquestra a execução de todas as tarefas do agente na ordem correta.
        """
        print("\n========================================================")
        print("|           INICIANDO EXECUÇÃO DO AGENTE VR            |")
        print("========================================================")
        
        if self._carregar_dados():
            # ORDEM DE EXECUÇÃO ALTERADA
            # 1. Prepara e normaliza os dados primeiro.
            self._preparar_dados()
            self._consolidar_dados()
            # 2. Inspeciona os dados DEPOIS de terem sido alterados.
            # self.inspecionar_dados()
        else:
            print("\n[AGENTE] A execução não pode continuar pois o carregamento de dados falhou ou não encontrou arquivos.")
        
        print("\n>> Execução do AgenteVR finalizada. <<")

# ======================================================================
# | PAINEL DE CONTROLE: PONTO DE ENTRADA DA EXECUÇÃO                   |
# ======================================================================
if __name__ == "__main__":
    agente = AgenteVR(input_dir=INPUT_DIR)
    agente.executar()