# 🛒 E-commerce ETL Analytics Pipeline

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57.svg)](https://www.sqlite.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)]()
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458.svg)](https://pandas.pydata.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **Complete end-to-end ETL pipeline** | E-commerce Data Analytics | Python & SQL  
> **Pipeline ETL completo** | Análise de Dados de E-commerce | Python & SQL

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

## <a name="português"></a>🇧🇷 Português

Sistema completo de **ETL (Extract, Transform, Load)** e análise de dados para e-commerce, processando vendas, clientes e produtos. Inclui pipeline automatizado, análises interativas em Jupyter e queries SQL otimizadas.

### ✨ Key Features

- 🔄 **Pipeline ETL Automatizado** - Extração, transformação e carga de dados sem intervenção manual
- 📊 **Star Schema Design** - Modelo dimensional otimizado para análises (9 tabelas)
- 🎯 **KPIs de Negócio** - Métricas pré-calculadas para e-commerce
- 📈 **Análise Interativa** - Jupyter notebook com visualizações e insights
- ✅ **Validação de Qualidade** - Verificações automáticas de integridade dos dados
- 🚀 **Setup Rápido** - Comece em 5 minutos
- 📚 **Documentação Completa** - Guias detalhados e exemplos

---

## 🎯 Destaques do Projeto

- 💰 **Faturamento Total**: R$ 9.629.301,57 analisados
- 📦 **2.000 pedidos** processados
- 👥 **483 clientes** únicos
- 🎯 **Ticket Médio**: R$ 4.814,65
- 📊 **9 tabelas** no modelo dimensional (Star Schema)
- ✅ **6.383 registros** validados
- 🔄 **Pipeline ETL** completo e automatizado

---

## 🚀 Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| **Python 3.10+** | Linguagem principal |
| **Pandas** | Manipulação e transformação de dados |
| **SQLite** | Banco de dados relacional |
| **Jupyter Notebook** | Análise exploratória interativa |
| **Matplotlib/Seaborn** | Visualizações de dados |
| **SQL** | Queries analíticas e validações |

---

## 📂 Estrutura do Projeto

```
ecommerce-etl-analytics-pipeline/
├── data/
│   ├── raw/                   # Dados brutos CSV
│   │   ├── clientes.csv
│   │   ├── produtos.csv
│   │   ├── pedidos.csv
│   │   └── item_pedido.csv
│   ├── processed/             # Dados processados
│   └── ecommerce_sqlite.db    # Database SQLite
├── sql/
│   ├── ddl/                   # Schemas de banco
│   │   ├── ddl_transacional.sql
│   │   └── ddl_analitico.sql
│   └── queries/               # Queries analíticas
│       ├── analytical_queries.sql
│       └── quality_checks.sql
├── scripts/
│   ├── pipeline_carga.py      # ETL completo
│   ├── sqlite_etl.py          # ETL simplificado
│   ├── analise_dados.py       # KPIs e relatórios
│   └── verificar_database.py  # Validação do DB
├── notebooks/
│   └── notebook_etl_analysis.ipynb  # Análise interativa
├── docs/                      # Documentação completa
│   ├── COMECE_AQUI.md
│   ├── GUIA_RAPIDO.md
│   ├── RELATORIO_FINAL.md
│   └── diagrams/
├── requirements.txt           # Dependências Python
├── LICENSE                    # Licença MIT
└── README.md
```

---

## 💻 Como Usar

### 📋 Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

### ⚙️ Instalação

```bash
# Clone o repositório
git clone https://github.com/ru-fagundes/ecommerce-etl-analytics-pipeline.git
cd ecommerce-etl-analytics-pipeline

# Crie um ambiente virtual (recomendado)
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt
```

### 🚀 Início Rápido (5 minutos)

#### 1️⃣ Verificar Sistema
```bash
python scripts/verificar_database.py
```
**Resultado esperado:** 9 tabelas, 6.383 registros ✅

#### 2️⃣ Gerar Análises
```bash
python scripts/analise_dados.py
```
**Resultado esperado:** KPIs e faturamento de R$ 9,6M ✅

#### 3️⃣ Explorar Interativamente
```bash
jupyter notebook notebooks/notebook_etl_analysis.ipynb
```
**Resultado esperado:** Notebook com gráficos e análises ✅

---

## 🔄 Pipeline ETL

### Arquitetura do Sistema

```
[CSV Files] → [ETL Python] → [SQLite Database] → [Analytics & Reports]
    ↓              ↓                ↓                    ↓
Clientes     Transformação    Star Schema        KPIs/Dashboards
Produtos     Limpeza          Fato + Dimensões   Visualizações
Pedidos      Validação        9 tabelas          Jupyter
```

### Como Recarregar Dados

```bash
# Opção 1: ETL Simplificado (apenas staging)
python scripts/sqlite_etl.py

# Opção 2: Pipeline Completo (staging + dimensões + fato)
python scripts/pipeline_carga.py
```

---

## 📊 Análises Disponíveis

### KPIs Principais
- 💰 Faturamento Total
- 📦 Total de Pedidos
- 👥 Total de Clientes
- 🎯 Ticket Médio
- 📈 Top 10 Produtos
- 🏆 Clientes VIP

### Visualizações
- Distribuição de vendas por produto
- Análise de clientes por região
- Evolução temporal de pedidos
- Matriz de correlação de vendas

### Queries SQL
Localização: sql/queries/analytical_queries.sql
- Faturamento por cliente
- Produtos mais vendidos
- Análise de performance
- Validações de qualidade

---

## 📚 Documentação

| Arquivo | Descrição |
|---------|-----------|
| [COMECE_AQUI.md](docs/COMECE_AQUI.md) | Guia de início rápido |
| [GUIA_RAPIDO.md](docs/GUIA_RAPIDO.md) | Manual de uso detalhado |
| [RELATORIO_FINAL.md](docs/RELATORIO_FINAL.md) | Relatório completo do projeto |
| [INDICE_DOCUMENTACAO.md](docs/INDICE_DOCUMENTACAO.md) | Índice de toda documentação |

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

**Rubia Fagundes**

- GitHub: [@ru-fagundes](https://github.com/ru-fagundes)
- LinkedIn: [Rubia Fagundes](https://www.linkedin.com/in/rubiafagundes)
- Email: rubiafagundes_ds@outlook.com

---

## ⭐ Dê uma estrela!

Se este projeto foi útil para você, considere dar uma ⭐ no repositório!

---

## 🎯 Casos de Uso

### 1. Análise de Vendas
- Identificar produtos mais vendidos
- Calcular ticket médio por cliente
- Analisar sazonalidade de vendas

### 2. Segmentação de Clientes
- Identificar clientes VIP (maior faturamento)
- Análise de comportamento de compra
- Segmentação por região

### 3. Gestão de Estoque
- Produtos com maior giro
- Análise de performance por categoria
- Previsão de demanda

---

## 🔍 Modelo de Dados

### Star Schema (Data Warehouse)

```
            dim_cliente
                 |
                 |
dim_produto --- fato_vendas --- dim_tempo
                 |
                 |
            dim_categoria
```

**Tabelas:**
- **Staging:** stg_cliente, stg_produto, stg_pedido, stg_item_pedido
- **Dimensões:** dim_cliente, dim_produto, dim_categoria, dim_tempo
- **Fato:** ato_vendas

---

## 💡 Insights e Resultados

### 📈 Principais Descobertas
- **Faturamento Total:** R$ 9.629.301,57
- **Ticket Médio:** R$ 4.814,65
- **Total de Pedidos:** 2.000
- **Clientes Ativos:** 483
- **Produtos Cadastrados:** 200
- **Taxa de Conversão:** Alta fidelidade de clientes recorrentes

### 🎯 Recomendações
1. Focar em produtos de alto giro
2. Implementar programa de fidelidade para clientes VIP
3. Otimizar estoque com base em análise preditiva
4. Expandir categorias de maior rentabilidade

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:
1. Fork o projeto
2. Crie uma branch: git checkout -b feature/nova-analise
3. Commit suas mudanças: git commit -m 'Adiciona análise X'
4. Push para a branch: git push origin feature/nova-analise
5. Abra um Pull Request

---

## 👤 Autor

**Rubia Fagundes**  
Projeto de Análise de Dados e ETL para E-commerce

---

## 📝 Licença

Este projeto é de código aberto para fins educacionais e de aprendizado.

---

## 📧 Contato

Para dúvidas ou sugestões, abra uma issue no GitHub.

---

**⭐ Gostou do projeto? Deixe uma estrela no repositório!**

---

## 🚀 Status do Projeto

✅ **Projeto Completo e Funcional**  
📅 **Última atualização:** Outubro de 2025  
📊 **Database validado:** 6.383 registros  
✅ **Documentação completa:** 4 guias disponíveis
