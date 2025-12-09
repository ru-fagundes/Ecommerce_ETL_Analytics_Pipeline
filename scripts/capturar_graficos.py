"""
Script para capturar screenshots dos gráficos do Jupyter Notebook

INSTRUÇÕES:
1. Abra o notebook: notebooks/notebook_etl_analysis.ipynb
2. Execute TODAS as células (Kernel → Restart & Run All)
3. Depois, com o notebook ABERTO e os gráficos visíveis, execute este script:
   python scripts/capturar_graficos.py

Este script utilizará a API do Jupyter para extrair as imagens das células
"""

import json
import base64
from pathlib import Path

# Caminhos
NOTEBOOK_PATH = Path(__file__).parent.parent / 'notebooks' / 'notebook_etl_analysis.ipynb'
SCREENSHOTS_DIR = Path(__file__).parent.parent / 'docs' / 'screenshots'
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

print("📸 CAPTURANDO GRÁFICOS DO NOTEBOOK")
print("=" * 80)

# Ler o notebook
with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Células que contêm gráficos (baseado nos IDs e sumário do notebook)
graficos_cells = {
    '#VSC-27e87757': 'faturamento_mensal.png',           # Célula 11 - image/png
    '#VSC-1386af4b': 'status_pedidos.png',               # Célula 14 - image/png
    '#VSC-0e922928': 'top_produtos.png',                 # Célula 17 - image/png
    '#VSC-91509548': 'analise_categorias.png',           # Célula 27 - image/png
    '#VSC-cbf83e8d': 'top_clientes.png',                 # Célula 29 - image/png
    '#VSC-d4cf3d83': 'distribuicoes_estatisticas.png',   # Célula 31 - image/png
    '#VSC-87c512ce': 'dashboard_executivo.png',          # Célula 33 - image/png
    '#VSC-08e0e6e8': 'serie_temporal_avancada.png',      # Célula 35 - image/png
    '#VSC-b0922281': 'heatmap_vendas_dia.png'            # Célula 37 - image/png
}

imagens_salvas = 0
contador = 0

# Nomes padrão para os gráficos
nomes_graficos = [
    'faturamento_mensal.png',
    'status_pedidos.png',
    'top_produtos.png',
    'serie_temporal.png',
    'heatmap_vendas_dia.png',
    'analise_categorias.png',
    'top_clientes.png',
    'distribuicoes_estatisticas.png',
    'dashboard_executivo.png',
    'serie_temporal_avancada.png',
    'analise_completa.png'
]

# Percorrer células do notebook
for idx, cell in enumerate(notebook.get('cells', [])):
    # Procurar outputs com imagens
    outputs = cell.get('outputs', [])
    for output in outputs:
        # Verificar se tem dados de imagem
        data = output.get('data', {})
        
        # Tentar PNG primeiro
        if 'image/png' in data:
            img_data = data['image/png']
            
            # Decodificar base64
            img_bytes = base64.b64decode(img_data)
            
            # Nome do arquivo
            if contador < len(nomes_graficos):
                nome_arquivo = nomes_graficos[contador]
            else:
                nome_arquivo = f'grafico_{contador+1}.png'
            
            # Salvar arquivo
            filepath = SCREENSHOTS_DIR / nome_arquivo
            with open(filepath, 'wb') as img_file:
                img_file.write(img_bytes)
            
            print(f"✅ {nome_arquivo:40} → Salvo! (célula {idx+1})")
            imagens_salvas += 1
            contador += 1
            break

print("\n" + "=" * 80)
if imagens_salvas > 0:
    print(f"✅ {imagens_salvas} gráficos capturados com sucesso!")
    print(f"📁 Localização: {SCREENSHOTS_DIR.resolve()}")
    print("\n💡 Agora as imagens aparecerão no README.md!")
else:
    print("❌ Nenhuma imagem encontrada!")
    print("\n💡 SOLUÇÃO:")
    print("   1. Abra o notebook no Jupyter ou VS Code")
    print("   2. Execute TODAS as células (Kernel → Restart & Run All)")
    print("   3. Aguarde todos os gráficos serem gerados")
    print("   4. Execute este script novamente")
print("=" * 80)
