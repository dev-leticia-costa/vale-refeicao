# ⚙️ Automação de Cálculo de Vale-Refeição

Este projeto automatiza o processo de consolidação e preparação de dados de RH para o cálculo do benefício de Vale-Refeição. O sistema é construído em Python e utiliza a biblioteca `pandas` para manipulação de dados, sendo capaz de ler múltiplos arquivos Excel, limpá-los, normalizá-los e uni-los em bases de dados coesas e prontas para análise.

## 🚀 Funcionalidades Principais

-   **Carregamento Dinâmico:** Lê todos os arquivos Excel (`.xlsx`) de uma pasta de entrada pré-configurada.
-   **Limpeza e Normalização:** Padroniza nomes de arquivos e colunas, removendo acentos, espaços e caracteres especiais para garantir consistência.
-   **Consolidação de Dados:** Une diferentes bases de dados (ex: funcionários ativos, férias, desligamentos) utilizando uma chave primária (matrícula) para criar uma visão unificada.
-   **Análise e Perfilamento:** Inclui um script auxiliar para gerar um relatório detalhado sobre a qualidade e estrutura de cada arquivo de entrada antes do processamento.
-   **Processamento em Fases:** A execução do agente principal é dividida em fases claras (Carregamento, Preparação, Consolidação, Limpeza), facilitando a depuração e manutenção.

## 📂 Estrutura do Projeto

A estrutura de arquivos e pastas do projeto está organizada da seguinte forma:

VALE-REFEICAO/
│
├── dados_entrada/
│   ├── ADMISSÃO ABRIL.xlsx'
│   ├── 'AFASTAMENTOS.xlsx'
│   ├── 'APRENDIZ.xlsx'
│   ├── 'ATIVOS.xlsx'
│   ├── 'Base dias uteis.xlsx'
│   ├── 'Base sindicato x valor.xlsx'
│   ├── 'DESLIGADOS.xlsx'
│   ├── 'ESTÁGIO.xlsx'
│   ├── 'EXTERIOR.xlsx'
│   ├── 'FÉRIAS.xlsx'
│   ├── 'VR MENSAL 05.2025.xlsx'
│
├── agente_vr.py          # Script principal que executa a automação
├── discover_data.py      # Script para análise exploratória dos dados
│
├── .env                  # Arquivo para variáveis de ambiente (não versionado)
├── .env.example          # Exemplo de arquivo de configuração
├── .gitignore            # Arquivos ignorados pelo Git
├── README.md             # Este arquivo
└── requirements.txt      # Dependências do projeto Python


## 🛠️ Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento e executar o projeto.

**1. Clone o Repositório**

```bash
git clone <url-do-seu-repositorio>
cd VALE-REFEICAO
2. Crie um Ambiente Virtual (Recomendado)

É uma boa prática isolar as dependências do projeto.

Bash

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
3. Instale as Dependências

O arquivo requirements.txt contém todas as bibliotecas Python necessárias.

Bash

pip install -r requirements.txt
4. Prepare a Pasta de Dados

Certifique-se de que a pasta dados_entrada exista.

Coloque todos os arquivos Excel (.xlsx) que serão processados dentro desta pasta.

5. Configure as Variáveis de Ambiente

Renomeie o arquivo .env.example para .env.

Ajuste as variáveis necessárias dentro do arquivo .env (se houver alguma).

▶️ Como Usar
O projeto possui dois scripts principais. A recomendação é sempre analisar os dados antes de executar a automação completa.

Passo 1: Analisar os Dados de Entrada (discover_data.py)
Este script gera um relatório completo no terminal para cada arquivo na pasta dados_entrada. Ele mostra as dimensões, tipos de dados, valores nulos e estatísticas descritivas, ajudando a identificar problemas de qualidade nos dados antes do processamento.

Para executá-lo, use o comando:

Bash

python discover_data.py
Passo 2: Executar a Automação Principal (agente_vr.py)
Este é o script principal que executa todo o fluxo de trabalho de ETL (Extração, Transformação e Carga). Ele orquestra todas as fases do processo, desde o carregamento dos arquivos até a consolidação final.

Para executá-lo, use o comando:

Bash

python agente_vr.py
O agente irá imprimir no console o progresso de cada fase:

Carregamento: Leitura dos arquivos da pasta dados_entrada.

Preparação: Normalização dos nomes das colunas.

Consolidação: União das diferentes tabelas (funcionários, referências de sindicato, etc.).

Limpeza: Tratamento de valores ausentes conforme as regras definidas.

📦 Dependências
pandas: Biblioteca fundamental para manipulação e análise de dados.

openpyxl: Dependência do pandas para ler e escrever arquivos no formato .xlsx.

Todas as dependências estão listadas no arquivo requirements.txt.


```bash
# Clonar o repositório
git clone https://github.com/dev-leticia-costa/vale_refeicao.git
```

```

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com sua chave de API
```
