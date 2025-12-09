# 📸 Screenshots do Projeto

## Como Gerar Screenshots

Para documentar visualmente o projeto, siga estas etapas:

### 1. Dashboard Streamlit

#### Executar o Dashboard
```powershell
streamlit run dashboard/app.py
```

#### Screenshots Necessários

1. **dashboard_main.png** - Tela principal com KPIs
   - Capturar: Página inicial completa com todos os KPIs visíveis
   - Tamanho recomendado: 1920x1080

2. **faturamento_mensal.png** - Gráfico de faturamento
   - Capturar: Seção "Faturamento Mensal" em destaque
   - Tamanho recomendado: 1200x600

3. **top_produtos.png** - Top 10 produtos
   - Capturar: Gráfico horizontal de produtos mais vendidos
   - Tamanho recomendado: 1200x600

4. **categorias.png** - Análise por categoria
   - Capturar: Pizza chart de categorias
   - Tamanho recomendado: 800x600

5. **analise_geografica.png** - Distribuição geográfica
   - Capturar: Aba de análise geográfica
   - Tamanho recomendado: 1920x1080

### 2. Jupyter Notebook

#### Executar o Notebook
```powershell
jupyter notebook notebooks/notebook_etl_analysis.ipynb
```

#### Screenshots Necessários

1. **notebook_serie_temporal.png** - Gráfico de séries temporais
   - Executar célula de séries temporais
   - Capturar: Gráfico com médias móveis

2. **notebook_heatmap.png** - Heatmap de vendas
   - Executar célula de heatmap
   - Capturar: Visualização de heatmap completo

3. **notebook_categorias.png** - Análise comparativa
   - Executar célula de categorias
   - Capturar: Dashboard multi-gráfico de categorias

4. **notebook_dashboard.png** - Dashboard executivo
   - Executar célula final de dashboard
   - Capturar: Dashboard executivo completo

### 3. Ferramentas para Captura

#### Windows
- **Ferramenta Snipping (Recorte e Esboço)**
  - Atalho: `Win + Shift + S`
  - Selecione área desejada
  - Salve em `docs/screenshots/`

- **Print Screen**
  - `PrtScn` - Captura tela inteira
  - `Alt + PrtScn` - Captura janela ativa

#### Extensões de Navegador
- **Awesome Screenshot** (Chrome/Edge)
- **Fireshot** (Firefox)

### 4. Edição e Otimização

#### Ferramentas Recomendadas
- **Paint.NET** (Windows)
- **GIMP** (Multiplataforma)
- **Photopea** (Online)

#### Otimização
```powershell
# Comprimir imagens com Python
pip install Pillow

# Script de compressão
python -c "
from PIL import Image
import os

for img_file in os.listdir('docs/screenshots'):
    if img_file.endswith(('.png', '.jpg')):
        img_path = os.path.join('docs/screenshots', img_file)
        img = Image.open(img_path)
        img.save(img_path, optimize=True, quality=85)
        print(f'Otimizado: {img_file}')
"
```

### 5. Nomenclatura de Arquivos

Use nomes descritivos e padronizados:

```
dashboard_main.png          # Tela principal do dashboard
dashboard_kpis.png          # Cards de KPIs
faturamento_mensal.png      # Gráfico de faturamento
top_produtos.png            # Top produtos
top_clientes.png            # Top clientes
categorias.png              # Análise de categorias
analise_geografica.png      # Distribuição por estado
serie_temporal.png          # Gráfico de séries temporais
heatmap_vendas.png          # Heatmap de vendas
distribuicao_valores.png    # Distribuição estatística
notebook_completo.png       # Visão geral do notebook
arquitetura_pipeline.png    # Diagrama de arquitetura
```

### 6. Checklist de Screenshots

- [ ] Dashboard principal (visão geral)
- [ ] KPIs principais (cards coloridos)
- [ ] Gráfico de faturamento mensal
- [ ] Top 10 produtos mais vendidos
- [ ] Top 10 clientes por faturamento
- [ ] Análise por categoria (pizza chart)
- [ ] Análise geográfica (por estado)
- [ ] Série temporal com médias móveis
- [ ] Heatmap de vendas
- [ ] Distribuição estatística
- [ ] Notebook Jupyter (visão geral)
- [ ] Dashboard executivo do notebook
- [ ] Terminal executando pipeline
- [ ] Código Python (exemplo)

### 7. Exemplo de Uso no README

Depois de gerar os screenshots, use assim no README:

```markdown
### Screenshots

#### Dashboard Principal
![Dashboard Principal](docs/screenshots/dashboard_main.png)

#### Análise de Faturamento
![Faturamento Mensal](docs/screenshots/faturamento_mensal.png)

#### Top Produtos
![Top Produtos](docs/screenshots/top_produtos.png)
```

### 8. Dicas de Qualidade

#### Resolução
- **Mínimo**: 1280x720 (HD)
- **Recomendado**: 1920x1080 (Full HD)
- **Máximo**: 2560x1440 (2K)

#### Formato
- **PNG**: Para gráficos e dashboards (melhor qualidade)
- **JPG**: Para fotos e imagens grandes (menor tamanho)

#### Tamanho de Arquivo
- Máximo: 500KB por imagem
- Use compressão se necessário

#### Clareza
- Texto legível
- Cores vibrantes
- Sem elementos cortados
- Fundo limpo

---

## 🎨 Exemplo de Fluxo Completo

```powershell
# 1. Iniciar dashboard
streamlit run dashboard/app.py

# 2. Esperar carregar completamente

# 3. Capturar tela principal
Win + Shift + S

# 4. Salvar como 'dashboard_main.png' em docs/screenshots/

# 5. Navegar para diferentes seções e capturar

# 6. Fechar dashboard (Ctrl+C)

# 7. Abrir notebook
jupyter notebook notebooks/notebook_etl_analysis.ipynb

# 8. Executar todas as células
# Cell → Run All

# 9. Capturar os gráficos gerados

# 10. Salvar em docs/screenshots/
```

---

## 📋 Template de Descrições

Use estas descrições no README ao adicionar as imagens:

```markdown
### Dashboard Interativo

O dashboard Streamlit oferece visualização em tempo real dos dados:

![Dashboard Principal](docs/screenshots/dashboard_main.png)
*Dashboard principal com KPIs e gráficos interativos*

### Análise de Faturamento

Acompanhe a evolução do faturamento ao longo do tempo:

![Faturamento Mensal](docs/screenshots/faturamento_mensal.png)
*Série temporal de faturamento com médias móveis*

### Top Produtos

Identifique os produtos mais vendidos:

![Top Produtos](docs/screenshots/top_produtos.png)
*Top 10 produtos por quantidade vendida e receita*
```

---

## ✅ Status das Screenshots

- [ ] Dashboard principal
- [ ] Faturamento mensal
- [ ] Top produtos
- [ ] Categorias
- [ ] Análise geográfica
- [ ] Série temporal
- [ ] Heatmap
- [ ] Dashboard executivo
- [ ] Notebook overview

**Última atualização**: A fazer

---

## 🆘 Problemas Comuns

### Dashboard não carrega
```powershell
# Verificar se o database existe
python scripts/verificar_database.py

# Reexecutar pipeline se necessário
python scripts/pipeline_carga.py
```

### Gráficos não aparecem no notebook
```python
# Adicionar no início do notebook
%matplotlib inline
```

### Imagens muito grandes
```powershell
# Redimensionar com Python
python -c "
from PIL import Image
img = Image.open('screenshot.png')
img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
img.save('screenshot_resized.png', optimize=True, quality=85)
"
```

---

<div align="center">

**📸 Boas capturas! Documente bem seu projeto!**

</div>
