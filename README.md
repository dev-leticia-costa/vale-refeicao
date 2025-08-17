# 🤖 Gemini Agent

Agente de IA simples usando a **API gratuita** do Google Gemini com interface de linha de comando.

## 🆓 Modelo Gratuito

- **Modelo:** gemini-1.5-flash
- **Limites:** 15 requisições/minuto, 1500/dia
- **Custo:** Gratuito para sempre
- **Funcionalidades:** Chat interativo, testes de API, menu intuitivo

## 📋 Pré-requisitos

- Python 3.9 ou superior
- Conta Google (para chave API gratuita)
- Poetry (opcional, mas recomendado)

## 🚀 Instalação

Escolha uma das opções abaixo:

### 📥 Opção 1: Clonar Repositório Existente


```bash
# Clonar o repositório
git clone https://github.com/dev-leticia-costa/gemini-integration-api.git
cd gemini-agent
```

```

**Sem Poetry:**
```bash
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
