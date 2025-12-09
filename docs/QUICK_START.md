# 🚀 Guia Rápido - Como Executar o Projeto

## 📋 Pré-requisitos

- Python 3.8 ou superior instalado
- pip (gerenciador de pacotes Python)
- Terminal/PowerShell

---

## ⚡ Início Rápido (5 minutos)

### 1️⃣ Instalar Dependências

```powershell
# Navegar até o diretório do projeto
cd "d:\Portfólio\Ecommerce_ETL_Analytics_Pipeline"

# Instalar todas as dependências
pip install -r config/requirements.txt
```

### 2️⃣ Executar Pipeline ETL

```powershell
# Carregar dados CSV → Database SQLite
python scripts/pipeline_carga.py
```

**Resultado esperado:**
```
[2025-12-07 10:30:15] ✅ Conectado ao database
[2025-12-07 10:30:16] 📥 Carregando staging...
[2025-12-07 10:30:17] ✅ stg_cliente: 1000 registros
...
[2025-12-07 10:30:25] ✅ Pipeline concluído com sucesso!
```

### 3️⃣ Executar Análises

```powershell
# Gerar KPIs e relatórios
python scripts/analise_dados.py
```

### 4️⃣ Abrir Dashboard Interativo 🎨

```powershell
# Iniciar aplicação Streamlit
streamlit run dashboard/app.py
```

O dashboard será aberto automaticamente em: **http://localhost:8501**

### 5️⃣ Explorar Notebook Jupyter 📓

```powershell
# Iniciar Jupyter
jupyter notebook

# Depois abrir: notebooks/notebook_etl_analysis.ipynb
```

---

## 🎯 Comandos Úteis

### Verificar Database

```powershell
python scripts/verificar_database.py
```

### Verificar Instalação Python

```powershell
python --version
pip --version
```

### Instalar Dependências Específicas

```powershell
# Apenas visualização
pip install matplotlib seaborn plotly

# Apenas dashboard
pip install streamlit

# Apenas notebook
pip install jupyter notebook
```

---

## 📊 O que você verá no Dashboard

### Página Principal
- **KPIs em tempo real**: Faturamento, ticket médio, pedidos, clientes
- **Gráficos interativos**: Faturamento mensal, categorias, produtos
- **Filtros dinâmicos**: Por período, categoria, estado

### Recursos Disponíveis
- ✅ Séries temporais com médias móveis
- ✅ Heatmaps de vendas
- ✅ Análise geográfica por estado/cidade
- ✅ Comparativos de categorias
- ✅ Top 10 produtos e clientes
- ✅ Distribuição de vendas por dia da semana
- ✅ Exportação de dados

---

## 🔧 Solução de Problemas

### Erro: "Module not found"

```powershell
# Reinstalar todas as dependências
pip install --upgrade -r config/requirements.txt
```

### Erro: "Database not found"

```powershell
# Reexecutar pipeline ETL
python scripts/pipeline_carga.py
```

### Dashboard não abre automaticamente

```powershell
# Abrir manualmente no navegador
# URL: http://localhost:8501
```

### Porta 8501 já em uso

```powershell
# Usar porta alternativa
streamlit run dashboard/app.py --server.port 8502
```

---

## 📁 Estrutura de Arquivos Importantes

```
Ecommerce_ETL_Analytics_Pipeline/
│
├── 📂 data/raw/              # Dados CSV originais
│   ├── clientes.csv
│   ├── produtos.csv
│   ├── pedidos.csv
│   └── item_pedido.csv
│
├── 📂 scripts/               # Scripts Python
│   ├── pipeline_carga.py     # ⭐ ETL principal
│   ├── analise_dados.py      # Geração de KPIs
│   └── verificar_database.py # Diagnóstico
│
├── 📂 dashboard/             # Dashboard Streamlit
│   └── app.py                # ⭐ Aplicação web
│
├── 📂 notebooks/             # Análise interativa
│   └── notebook_etl_analysis.ipynb  # ⭐ Jupyter Notebook
│
├── 🗄️ ecommerce_sqlite.db   # ⭐ Database SQLite (gerado)
│
└── 📄 README.md              # Documentação completa
```

---

## 💡 Dicas de Uso

### Dashboard Streamlit

1. **Filtros**: Use a barra lateral para filtrar por período, categoria e estado
2. **Atualização**: Clique em "🔄 Atualizar Dashboard" para recarregar dados
3. **Exportação**: (Recurso em desenvolvimento)

### Jupyter Notebook

1. **Executar todas as células**: Menu → Cell → Run All
2. **Executar célula individual**: Shift + Enter
3. **Adicionar nova célula**: Pressione B (below) ou A (above)

### Análise de Dados

```powershell
# Análise específica
python -c "from scripts.analise_dados import gerar_kpis; print(gerar_kpis())"
```

---

## 🎓 Próximos Passos

1. ✅ Explorar o dashboard interativo
2. ✅ Executar o notebook Jupyter
3. ✅ Modificar queries SQL em `sql/queries/`
4. ✅ Adicionar novos gráficos ao dashboard
5. ✅ Criar seus próprios relatórios

---

## 📚 Recursos Adicionais

- [📄 README Completo](README.md) - Documentação detalhada
- [📊 Relatório Final](docs/RELATORIO_FINAL.md) - Análise completa
- [🗺️ Diagramas](docs/diagrams/) - Arquitetura do sistema
- [💾 SQL Queries](sql/queries/) - Queries prontas para usar

---

## 🆘 Precisa de Ajuda?

### Documentação
- Consulte o [README.md](README.md) para informações detalhadas
- Veja os [diagramas de arquitetura](docs/diagrams/) para entender o fluxo

### Suporte
- 🐛 [Reportar Bug](https://github.com/seu-usuario/ecommerce-etl-pipeline/issues)
- 💡 [Solicitar Feature](https://github.com/seu-usuario/ecommerce-etl-pipeline/issues)

---

## ✨ Exemplo de Fluxo Completo

```powershell
# 1. Instalar dependências
pip install -r config/requirements.txt

# 2. Executar ETL
python scripts/pipeline_carga.py

# 3. Gerar análises
python scripts/analise_dados.py

# 4. Abrir dashboard
streamlit run dashboard/app.py

# 5. Em outra janela, abrir notebook
jupyter notebook
```

**Tempo total: ~5 minutos** ⏱️

---

<div align="center">

**🎉 Pronto! Seu ambiente está configurado!**

Aproveite a exploração dos dados! 📊

</div>
