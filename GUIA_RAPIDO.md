# 🚀 Guia Rápido de Uso

## Comandos Principais

### ✅ Verificar Sistema
```bash
# Validar database e tabelas
python scripts/verificar_database.py
```
**Saída esperada:**
```
✅ Tabelas encontradas (9):
  - stg_cliente: 500 registros
  - stg_produto: 200 registros
  - stg_pedido: 2000 registros
  ...
```

---

### 📊 Gerar Análises Rápidas
```bash
# KPIs e relatórios no terminal
python scripts/analise_dados.py
```
**Saída esperada:**
```
📊 KPIs PRINCIPAIS DO E-COMMERCE
💰 Faturamento Total: R$ 9,629,301.57
📦 Total de Pedidos: 2,000
👥 Total de Clientes: 483
🎯 Ticket Médio: R$ 4,814.65
...
```

---

### 🔄 Recarregar Dados (se necessário)
```bash
# Opção 1: ETL simplificado (apenas staging)
python scripts/sqlite_etl.py

# Opção 2: Pipeline completo (staging + dimensões + fato)
python scripts/pipeline_carga.py
```

---

### 📓 Análise Interativa Completa
```bash
# Abrir Jupyter Notebook
jupyter notebook notebooks/notebook_etl_analysis.ipynb
```

**No notebook:**
1. Execute todas as células: `Cell → Run All`
2. Visualize KPIs e gráficos
3. Explore os dados interativamente

---

## 📁 Estrutura de Arquivos

### Dados
```
data/raw/
├── clientes.csv       → Dados de clientes
├── produtos.csv       → Catálogo de produtos
├── pedidos.csv        → Pedidos realizados
└── item_pedido.csv    → Itens dos pedidos
```

### Scripts
```
scripts/
├── verificar_database.py  → Validação do DB
├── analise_dados.py       → KPIs e relatórios
├── sqlite_etl.py          → ETL simples
└── pipeline_carga.py      → ETL completo
```

### SQL
```
sql/
├── ddl/
│   ├── ddl_transacional.sql  → Schema OLTP
│   └── ddl_analitico.sql     → Schema DW
└── queries/
    ├── analytical_queries.sql → Análises
    └── quality_checks.sql     → Validações
```

---

## 🎯 Casos de Uso

### 1. Primeira Execução
```bash
# 1. Verificar se tudo está OK
python scripts/verificar_database.py

# 2. Gerar análises
python scripts/analise_dados.py

# 3. Explorar no Jupyter
jupyter notebook notebooks/notebook_etl_analysis.ipynb
```

### 2. Atualizar Dados
```bash
# 1. Coloque novos CSVs em data/raw/

# 2. Execute o pipeline
python scripts/pipeline_carga.py

# 3. Verifique os dados
python scripts/verificar_database.py
```

### 3. Análise Ad-hoc
```bash
# Opção 1: Terminal
python scripts/analise_dados.py

# Opção 2: Jupyter (recomendado)
jupyter notebook notebooks/notebook_etl_analysis.ipynb
```

### 4. Consultas SQL Customizadas
```bash
# Abrir SQLite
sqlite3 ecommerce_sqlite.db

# Executar queries
SELECT * FROM dim_produto LIMIT 10;
```

---

## 📊 Principais Análises Disponíveis

### KPIs Financeiros
- Faturamento total
- Faturamento mensal
- Ticket médio
- Receita por categoria

### KPIs Operacionais
- Total de pedidos
- Pedidos por status
- Taxa de conversão
- Produtos mais vendidos

### KPIs de Cliente
- Base de clientes
- Clientes ativos
- Top clientes
- Frequência de compra

---

## 🐛 Troubleshooting

### Erro: "Database não encontrado"
**Solução:**
```bash
# Verificar se está na raiz do projeto
pwd  # Linux/Mac
cd   # Windows

# O arquivo deve estar aqui:
ls ecommerce_sqlite.db  # Linux/Mac
dir ecommerce_sqlite.db # Windows
```

### Erro: "ModuleNotFoundError: No module named 'pandas'"
**Solução:**
```bash
pip install pandas matplotlib jupyter
```

### Erro: "No such table: stg_cliente"
**Solução:**
```bash
# Recarregar dados
python scripts/sqlite_etl.py
```

### Notebook não abre
**Solução:**
```bash
# Instalar Jupyter
pip install jupyter

# Verificar instalação
jupyter --version

# Abrir novamente
jupyter notebook
```

---

## 💡 Dicas Úteis

1. **Execute sempre da raiz do projeto** para evitar erros de path
2. **Use o notebook** para análises exploratórias
3. **Use os scripts Python** para análises rápidas/automações
4. **Consulte REVISAO_COMPLETA.md** para detalhes técnicos
5. **Verifique o database** antes de executar análises

---

## 📞 Comandos de Ajuda

```bash
# Ajuda de cada script
python scripts/analise_dados.py --help    # (se implementado)
python scripts/pipeline_carga.py --help   # (se implementado)

# Versão do Python
python --version

# Pacotes instalados
pip list | grep -E "pandas|matplotlib|jupyter"
```

---

## ✅ Checklist de Validação

Antes de começar a trabalhar:

- [ ] Database existe (`ecommerce_sqlite.db`)
- [ ] Pandas instalado (`pip install pandas`)
- [ ] Matplotlib instalado (`pip install matplotlib`)
- [ ] Jupyter instalado (`pip install jupyter`)
- [ ] CSVs em `data/raw/`
- [ ] Scripts Python executam sem erros

---

**Última atualização:** 16/10/2025
