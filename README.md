
# Sistema de Administração de Dados para E-commerce

Este projeto implementa um sistema completo de administração de dados para e-commerce, incluindo pipeline ETL, modelagem dimensional e análises.

> **✅ Projeto Revisado e Aprovado** - Última atualização: 16/10/2025  
> 📖 **[COMECE AQUI](COMECE_AQUI.md)** para início rápido  
> 📚 Consulte [REVISAO_COMPLETA.md](REVISAO_COMPLETA.md) para detalhes técnicos completos

## 📁 Estrutura do Projeto

```
├── data/                          # Dados do projeto
│   ├── raw/                      # Dados brutos (CSV originais)
│   │   ├── clientes.csv          # 500 clientes
│   │   ├── produtos.csv          # 200 produtos
│   │   ├── pedidos.csv           # 2.000 pedidos
│   │   └── item_pedido.csv       # 3.183 itens
│   └── processed/                # Dados processados
│
├── sql/                          # Scripts SQL
│   ├── ddl/                      # Definições de estruturas
│   │   ├── ddl_transacional.sql  # Schema transacional (OLTP)
│   │   └── ddl_analitico.sql     # Schema analítico (DW - Star Schema)
│   └── queries/                  # Consultas e análises
│       ├── analytical_queries.sql # Queries de análise
│       └── quality_checks.sql    # Verificações de qualidade
│
├── scripts/                      # Scripts Python ✅ REVISADOS
│   ├── pipeline_carga.py         # Pipeline ETL completo
│   ├── sqlite_etl.py            # ETL simplificado
│   ├── analise_dados.py         # Análise e KPIs ✨ NOVO
│   └── verificar_database.py    # Verificação DB ✨ NOVO
│
├── notebooks/                    # Notebooks de análise
│   └── notebook_etl_analysis.ipynb # Análise completa e visualizações
│
├── docs/                         # Documentação
│   ├── diagrams/                 # Diagramas do projeto
│   │   ├── er_diagram.mmd       # Diagrama ER (Mermaid)
│   │   └── er_diagram.png       # Diagrama ER (PNG)
│   └── dicionario_de_dados.xlsx # Dicionário de dados
│
├── ecommerce_sqlite.db          # Database principal (SQLite)
└── README.md                    # Este arquivo
```

```
## 🚀 Como Executar

### 1. Preparação do Ambiente
```bash
# Clone o repositório
git clone <repository-url>
cd sistema-administracao-dados-ecommerce

# Instale as dependências
pip install pandas matplotlib jupyter
```

### 2. Verificar Database (Opcional)
```bash
# Validar integridade do database
python scripts/verificar_database.py
```

### 3. Executar Pipeline ETL (Opcional)
```bash
# Pipeline completo (staging → dimensões → fato)
python scripts/pipeline_carga.py

# OU versão simplificada (apenas staging)
python scripts/sqlite_etl.py
```

### 4. Análise de Dados

#### Opção A: Script Python (Rápido)
```bash
# Gerar KPIs e relatórios no terminal
python scripts/analise_dados.py
```

#### Opção B: Jupyter Notebook (Interativo - Recomendado)
```bash
# Abrir notebook com análises completas
jupyter notebook notebooks/notebook_etl_analysis.ipynb
```

## 📊 Funcionalidades

- **Pipeline ETL Completo**: Carregamento de CSVs para SQLite com transformações
- **Modelagem Dimensional**: Star Schema com dimensões e fatos
- **Análises e KPIs**: Faturamento, ticket médio, top produtos
- **Visualizações**: Gráficos interativos com matplotlib
- **Scripts Utilitários**: Verificação, análise e carga de dados
- **Documentação Completa**: Diagramas ER e dicionário de dados

### � KPIs Disponíveis
- 💰 Faturamento Total e Mensal
- 📦 Total de Pedidos
- 👥 Base de Clientes
- 🎯 Ticket Médio
- 🏆 Top Produtos (quantidade e receita)
- 📋 Análise por Status
- 📅 Evolução Temporal

## �🛠️ Tecnologias Utilizadas

- **Python 3.13+**: Linguagem principal
- **pandas**: Manipulação de dados
- **SQLite**: Database relacional
- **matplotlib**: Visualizações
- **Jupyter**: Análises interativas
- **SQL**: Consultas e transformações

## 📊 Funcionalidades

- **Pipeline ETL Completo**: Carregamento de CSVs para SQLite com transformações
- **Modelagem Dimensional**: Star Schema com dimensões e fatos
- **Análises e KPIs**: Faturamento, ticket médio, top produtos
- **Visualizações**: Gráficos interativos com matplotlib
- **Dashboard BI**: Interface web interativa com Streamlit e Plotly
- **Documentação Completa**: Diagramas ER e dicionário de dados

### 🎯 Dashboard BI - Principais Recursos:
- **📈 KPIs em Tempo Real**: Faturamento, pedidos, clientes, ticket médio
- **📊 Gráficos Interativos**: Evolução temporal, rankings, distribuições
- **🔍 Análises Detalhadas**: Por status, categoria, método de pagamento
- **👥 Gestão de Clientes**: Top clientes e segmentação
- **🎛️ Filtros Dinâmicos**: Períodos, categorias, valores
- **📱 Interface Responsiva**: Adaptável a diferentes dispositivos

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal
- **pandas**: Manipulação de dados
- **SQLite**: Database relacional
- **matplotlib**: Visualizações estáticas
- **Streamlit**: Dashboard web interativo
- **Plotly**: Gráficos interativos avançados
- **Jupyter**: Análises interativas
- **SQL**: Consultas e transformações
