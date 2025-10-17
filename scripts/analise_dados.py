"""
Script de Análise de Dados - E-commerce
Gera KPIs e relatórios do sistema

Uso:
    python scripts/analise_dados.py
"""

import os
import sqlite3
import pandas as pd
from datetime import datetime

# Configurações
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "ecommerce_sqlite.db")

def conectar_db():
    """Conecta ao database"""
    return sqlite3.connect(DB_PATH)

def kpis_principais():
    """Calcula KPIs principais do negócio"""
    conn = conectar_db()
    
    print("=" * 60)
    print("📊 KPIs PRINCIPAIS DO E-COMMERCE")
    print("=" * 60)
    
    # Faturamento Total
    query = """
    SELECT 
        SUM(quantidade * valor_unitario - COALESCE(desconto, 0)) as faturamento_total,
        COUNT(DISTINCT p.pedido_id) as total_pedidos,
        COUNT(DISTINCT p.cliente_id) as total_clientes
    FROM stg_item_pedido ip
    JOIN stg_pedido p ON ip.pedido_id = p.pedido_id
    """
    df = pd.read_sql_query(query, conn)
    
    faturamento = df['faturamento_total'].iloc[0]
    pedidos = df['total_pedidos'].iloc[0]
    clientes = df['total_clientes'].iloc[0]
    ticket_medio = faturamento / pedidos if pedidos > 0 else 0
    
    print(f"\n💰 Faturamento Total: R$ {faturamento:,.2f}")
    print(f"📦 Total de Pedidos: {pedidos:,}")
    print(f"👥 Total de Clientes: {clientes:,}")
    print(f"🎯 Ticket Médio: R$ {ticket_medio:,.2f}")
    
    # Top 5 Produtos
    print("\n" + "=" * 60)
    print("🏆 TOP 5 PRODUTOS MAIS VENDIDOS")
    print("=" * 60)
    
    query_top = """
    SELECT 
        pr.nome,
        pr.categoria,
        SUM(ip.quantidade) as qtd_vendida,
        SUM(ip.quantidade * ip.valor_unitario - COALESCE(ip.desconto, 0)) as receita
    FROM stg_item_pedido ip
    JOIN stg_produto pr ON ip.produto_id = pr.produto_id
    GROUP BY pr.produto_id, pr.nome, pr.categoria
    ORDER BY qtd_vendida DESC
    LIMIT 5
    """
    df_top = pd.read_sql_query(query_top, conn)
    
    for i, row in df_top.iterrows():
        print(f"\n{i+1}. {row['nome']}")
        print(f"   Categoria: {row['categoria']}")
        print(f"   Quantidade: {row['qtd_vendida']:.0f} unidades")
        print(f"   Receita: R$ {row['receita']:,.2f}")
    
    # Análise por Status
    print("\n" + "=" * 60)
    print("📋 PEDIDOS POR STATUS")
    print("=" * 60)
    
    query_status = """
    SELECT 
        status,
        COUNT(*) as qtd_pedidos,
        SUM(valor_total) as valor_total
    FROM stg_pedido
    GROUP BY status
    ORDER BY qtd_pedidos DESC
    """
    df_status = pd.read_sql_query(query_status, conn)
    
    for _, row in df_status.iterrows():
        print(f"\n{row['status']}: {row['qtd_pedidos']} pedidos (R$ {row['valor_total']:,.2f})")
    
    # Faturamento Mensal
    print("\n" + "=" * 60)
    print("📈 FATURAMENTO ÚLTIMOS 6 MESES")
    print("=" * 60)
    
    query_mensal = """
    SELECT 
        strftime('%Y-%m', p.data_pedido) as ano_mes,
        COUNT(DISTINCT p.pedido_id) as num_pedidos,
        SUM(ip.quantidade * ip.valor_unitario - COALESCE(ip.desconto, 0)) as faturamento
    FROM stg_pedido p
    JOIN stg_item_pedido ip ON p.pedido_id = ip.pedido_id
    WHERE p.data_pedido IS NOT NULL
    GROUP BY ano_mes
    ORDER BY ano_mes DESC
    LIMIT 6
    """
    df_mensal = pd.read_sql_query(query_mensal, conn)
    
    for _, row in df_mensal.iterrows():
        print(f"\n{row['ano_mes']}: R$ {row['faturamento']:,.2f} ({row['num_pedidos']} pedidos)")
    
    conn.close()
    print("\n" + "=" * 60)

if __name__ == "__main__":
    try:
        kpis_principais()
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
