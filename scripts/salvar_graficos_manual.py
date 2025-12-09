"""
Script simples para salvar os gráficos gerados no notebook
Execute este script DEPOIS de rodar todas as células do notebook
"""

from pathlib import Path
import matplotlib.pyplot as plt

# Criar diretório
screenshots_dir = Path(__file__).parent.parent / 'docs' / 'screenshots'
screenshots_dir.mkdir(parents=True, exist_ok=True)

print("📸 SALVANDO SCREENSHOTS DOS GRÁFICOS...")
print("=" * 80)

# Pegar todas as figuras abertas do matplotlib
figs = [plt.figure(n) for n in plt.get_fignums()]

if len(figs) == 0:
    print("❌ Nenhuma figura encontrada!")
    print("\n💡 SOLUÇÃO:")
    print("   1. Abra o notebook: notebooks/notebook_etl_analysis.ipynb")
    print("   2. Execute todas as células de visualização")
    print("   3. Com as figuras ainda abertas, execute este script")
else:
    print(f"✅ Encontradas {len(figs)} figuras ativas\n")
    
    # Nomes sugeridos para as figuras
    nomes = [
        'faturamento_mensal.png',
        'status_pedidos.png',
        'top_produtos.png',
        'serie_temporal.png',
        'heatmap_vendas_dia.png',
        'analise_categorias.png',
        'top_clientes.png',
        'distribuicoes_estatisticas.png',
        'dashboard_executivo.png'
    ]
    
    for i, fig in enumerate(figs):
        if i < len(nomes):
            nome = nomes[i]
        else:
            nome = f'grafico_{i+1}.png'
        
        filepath = screenshots_dir / nome
        fig.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✅ {nome:40} → Salvo!")

print("\n" + "=" * 80)
print(f"📁 Localização: {screenshots_dir.resolve()}")
print("✅ Screenshots salvos com sucesso!")
print("=" * 80)
