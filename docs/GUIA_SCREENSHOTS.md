# 📸 Guia de Captura de Screenshots

Este guia orienta a captura de screenshots dos principais gráficos e visualizações do projeto para documentação.

## 📋 Lista de Screenshots Necessários

### 1. Dashboard Executivo (Célula 37)
**Arquivo**: `dashboard_executivo.png`  
**Localização**: Notebook célula 37  
**Conteúdo**:
- KPI Cards (Faturamento Total, Ticket Médio, Total Pedidos, Clientes)
- Evolução do Faturamento Mensal
- Participação de Receita por Categoria (Pizza)
- Top 5 Produtos Mais Vendidos
- Distribuição de Pedidos por Faixa de Valor
- Tabela de Métricas

**Como capturar**:
1. Execute a célula 37 do notebook
2. Aguarde o gráfico renderizar completamente
3. Clique com botão direito no gráfico → "Save Image As..."
4. Salvar como: `docs/screenshots/dashboard_executivo.png`

---

### 2. Heatmap - Vendas por Dia da Semana (Célula 29)
**Arquivo**: `heatmap_vendas_dia.png`  
**Localização**: Notebook célula 29  
**Conteúdo**:
- Faturamento por Dia da Semana (barras horizontais)
- Número de Pedidos por Dia (barras verticais)
- Ticket Médio por Dia (linha)
- Performance Normalizada (heatmap)

**Como capturar**:
1. Execute a célula 29
2. Salvar como: `docs/screenshots/heatmap_vendas_dia.png`

---

### 3. Análise de Categorias (Célula 31)
**Arquivo**: `analise_categorias.png`  
**Localização**: Notebook célula 31  
**Conteúdo**:
- Faturamento por Categoria
- Número de Produtos por Categoria
- Ticket Médio por Categoria
- Distribuição de Receita (Pizza)

**Como capturar**:
1. Execute a célula 31
2. Salvar como: `docs/screenshots/analise_categorias.png`

---

### 4. Top Clientes (Célula 33)
**Arquivo**: `top_clientes.png`  
**Localização**: Notebook célula 33  
**Conteúdo**:
- Top 10 Clientes por Faturamento
- Top 10 Clientes por Frequência
- Distribuição de Clientes por Segmento

**Como capturar**:
1. Execute a célula 33
2. Salvar como: `docs/screenshots/top_clientes.png`

---

### 5. Distribuições Estatísticas (Célula 35)
**Arquivo**: `distribuicoes_estatisticas.png`  
**Localização**: Notebook célula 35  
**Conteúdo**:
- Histograma de Valores de Pedidos
- Boxplot de Valores de Pedidos
- Análise de Outliers
- Distribuição de Itens por Pedido

**Como capturar**:
1. Execute a célula 35
2. Salvar como: `docs/screenshots/distribuicoes_estatisticas.png`

---

### 6. Série Temporal (Célula 27)
**Arquivo**: `serie_temporal.png`  
**Localização**: Notebook célula 27  
**Conteúdo**:
- Evolução do Faturamento Diário
- Tendência de vendas ao longo do tempo

**Como capturar**:
1. Execute a célula 27
2. Salvar como: `docs/screenshots/serie_temporal.png`

---

### 7. Diagrama ER (Se disponível)
**Arquivo**: `diagrama_er.png`  
**Localização**: `docs/diagrams/er_diagram.mmd`  
**Conteúdo**:
- Modelo dimensional (Star Schema)
- Relacionamentos entre tabelas

**Como capturar**:
1. Abrir arquivo `.mmd` em visualizador Mermaid
2. Exportar como PNG
3. Salvar como: `docs/screenshots/diagrama_er.png`

---

## 🎯 Padrões de Captura

### Resolução
- **Mínimo**: 1920x1080 (Full HD)
- **Recomendado**: 2560x1440 (2K) ou superior
- **DPI**: 96 ou superior

### Formato
- **Tipo**: PNG (melhor qualidade)
- **Compressão**: Sem perdas
- **Fundo**: Branco ou transparente

### Qualidade
- ✅ Gráficos completamente renderizados
- ✅ Texto legível em todos os tamanhos
- ✅ Cores vibrantes e contrastes adequados
- ✅ Sem cortes nas bordas
- ✅ Legendas e títulos visíveis

---

## 📁 Estrutura de Arquivos

Após a captura, organize assim:

```
docs/
└── screenshots/
    ├── README.md
    ├── dashboard_executivo.png
    ├── heatmap_vendas_dia.png
    ├── analise_categorias.png
    ├── top_clientes.png
    ├── distribuicoes_estatisticas.png
    ├── serie_temporal.png
    └── diagrama_er.png
```

---

## 🔧 Ferramentas Recomendadas

### Captura de Tela
- **Windows**: Snipping Tool, Greenshot
- **Mac**: Command + Shift + 4
- **Linux**: Shutter, GNOME Screenshot

### Edição (se necessário)
- **Crop**: IrfanView, GIMP
- **Resize**: ImageMagick
- **Compressão**: TinyPNG, OptiPNG

---

## ✅ Checklist Final

Antes de usar as screenshots no README:

- [ ] Todas as 7 screenshots capturadas
- [ ] Resolução mínima 1920x1080
- [ ] Formato PNG
- [ ] Arquivos salvos em `docs/screenshots/`
- [ ] Nomes de arquivo corretos
- [ ] Gráficos completamente visíveis
- [ ] Cores e texto legíveis
- [ ] README.md atualizado com referências

---

## 📝 Uso no README

Após capturar, adicione ao README.md:

```markdown
## 📊 Resultados

### Dashboard Executivo
![Dashboard Executivo](docs/screenshots/dashboard_executivo.png)

### Análise por Dia da Semana
![Heatmap Vendas](docs/screenshots/heatmap_vendas_dia.png)

### Análise de Categorias
![Análise Categorias](docs/screenshots/analise_categorias.png)

### Top Clientes
![Top Clientes](docs/screenshots/top_clientes.png)

### Distribuições Estatísticas
![Distribuições](docs/screenshots/distribuicoes_estatisticas.png)

### Série Temporal
![Série Temporal](docs/screenshots/serie_temporal.png)
```

---

## 🎨 Dicas de Apresentação

1. **Ordem lógica**: Comece com visão geral (dashboard), depois detalhes
2. **Legendas descritivas**: Explique o que cada gráfico mostra
3. **Contexto**: Adicione insights principais abaixo de cada imagem
4. **Responsividade**: Verifique como ficam em telas menores
5. **Consistência**: Use mesmo estilo em todas as capturas

---

*Última atualização: 07/12/2025*
