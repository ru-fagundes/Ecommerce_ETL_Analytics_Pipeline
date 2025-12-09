# -*- coding: utf-8 -*-
"""
Teste rápido das funcionalidades do dashboard
Simula execução das queries principais sem abrir o Streamlit
"""

import sqlite3
import pandas as pd
import os
import sys

def get_db_connection():
    """Obtém conexão com o database"""
    db_paths = [
        "ecommerce_sqlite.db",
        "data/ecommerce_sqlite.db"
    ]
    
    for path in db_paths:
        if os.path.exists(path):
            return sqlite3.connect(path)
    
    raise FileNotFoundError("Database não encontrado!")

def test_kpis():
    """Testa cálculo dos KPIs principais"""
    print("\n" + "="*70)
    print("📊 TESTANDO KPIs DO DASHBOARD")
    print("="*70)
    
    conn = get_db_connection()
    
    try:
        # Faturamento Total
        query = "SELECT SUM(valor_total) as total FROM fato_vendas"
        faturamento = pd.read_sql(query, conn)['total'][0]
        print(f"  💰 Faturamento Total: R$ {faturamento:,.2f}")
        
        # Ticket Médio
        query = """
        SELECT AVG(total_pedido) as ticket
        FROM (
            SELECT pedido_id, SUM(valor_total) as total_pedido
            FROM fato_vendas
            GROUP BY pedido_id
        )
        """
        ticket = pd.read_sql(query, conn)['ticket'][0]
        print(f"  📈 Ticket Médio: R$ {ticket:,.2f}")
        
        # Total de Pedidos
        query = "SELECT COUNT(DISTINCT pedido_id) as total FROM fato_vendas"
        pedidos = pd.read_sql(query, conn)['total'][0]
        print(f"  🛍️  Total de Pedidos: {pedidos:,}")
        
        # Clientes Únicos
        query = "SELECT COUNT(DISTINCT cliente_id) as total FROM fato_vendas"
        clientes = pd.read_sql(query, conn)['total'][0]
        print(f"  👥 Clientes Únicos: {clientes:,}")
        
        # Itens Vendidos
        query = "SELECT SUM(quantidade) as total FROM fato_vendas"
        itens = pd.read_sql(query, conn)['total'][0]
        print(f"  📦 Itens Vendidos: {itens:,}")
        
        print("\n  ✅ Todos os KPIs calculados com sucesso!")
        return True
        
    except Exception as e:
        print(f"  ❌ Erro ao calcular KPIs: {e}")
        return False
    finally:
        conn.close()

def test_queries():
    """Testa as queries principais do dashboard"""
    print("\n" + "="*70)
    print("🔍 TESTANDO QUERIES DO DASHBOARD")
    print("="*70)
    
    conn = get_db_connection()
    
    queries = {
        'Faturamento Mensal': """
            SELECT 
                strftime('%Y-%m', dt.data) AS mes,
                SUM(f.valor_total) AS faturamento
            FROM fato_vendas f
            JOIN dim_tempo dt ON f.tempo_id = dt.tempo_id
            GROUP BY mes
            ORDER BY mes
            LIMIT 5
        """,
        
        'Top 5 Produtos': """
            SELECT 
                p.nome AS produto,
                SUM(f.quantidade) AS total_vendido
            FROM fato_vendas f
            JOIN dim_produto p ON f.produto_id = p.produto_id
            GROUP BY p.nome
            ORDER BY total_vendido DESC
            LIMIT 5
        """,
        
        'Top 5 Clientes': """
            SELECT 
                c.nome AS cliente,
                SUM(f.valor_total) AS total_gasto
            FROM fato_vendas f
            JOIN dim_cliente c ON f.cliente_id = c.cliente_id
            GROUP BY c.nome
            ORDER BY total_gasto DESC
            LIMIT 5
        """,
        
        'Categorias': """
            SELECT 
                p.categoria,
                SUM(f.valor_total) AS receita
            FROM fato_vendas f
            JOIN dim_produto p ON f.produto_id = p.produto_id
            GROUP BY p.categoria
            ORDER BY receita DESC
        """,
        
        'Vendas por Dia da Semana': """
            SELECT 
                dt.dia_semana,
                COUNT(DISTINCT f.pedido_id) AS num_pedidos
            FROM fato_vendas f
            JOIN dim_tempo dt ON f.tempo_id = dt.tempo_id
            GROUP BY dt.dia_semana
            ORDER BY dt.dia_semana
        """
    }
    
    all_ok = True
    for nome, query in queries.items():
        try:
            df = pd.read_sql(query, conn)
            print(f"  ✅ {nome:30s} - {len(df)} linhas")
        except Exception as e:
            print(f"  ❌ {nome:30s} - Erro: {e}")
            all_ok = False
    
    conn.close()
    
    if all_ok:
        print("\n  ✅ Todas as queries executadas com sucesso!")
    
    return all_ok

def test_filters():
    """Testa os filtros disponíveis"""
    print("\n" + "="*70)
    print("🔎 TESTANDO FILTROS DO DASHBOARD")
    print("="*70)
    
    conn = get_db_connection()
    
    try:
        # Categorias disponíveis
        query = "SELECT DISTINCT categoria FROM dim_produto ORDER BY categoria"
        categorias = pd.read_sql(query, conn)
        print(f"  📦 Categorias: {len(categorias)} encontradas")
        print(f"      {', '.join(categorias['categoria'].head(5).tolist())}")
        
        # Range de datas
        query = "SELECT MIN(data) as min_data, MAX(data) as max_data FROM dim_tempo"
        datas = pd.read_sql(query, conn)
        print(f"  📅 Período: {datas['min_data'][0]} a {datas['max_data'][0]}")
        
        # Clientes
        query = "SELECT COUNT(DISTINCT cliente_id) as total FROM dim_cliente"
        clientes = pd.read_sql(query, conn)
        print(f"  👥 Total de Clientes: {clientes['total'][0]}")
        
        print("\n  ✅ Filtros validados!")
        return True
        
    except Exception as e:
        print(f"  ❌ Erro ao testar filtros: {e}")
        return False
    finally:
        conn.close()

def main():
    """Executa todos os testes do dashboard"""
    print("\n" + "="*70)
    print("🎨 TESTE DO DASHBOARD STREAMLIT")
    print("="*70)
    
    results = {
        'KPIs': test_kpis(),
        'Queries': test_queries(),
        'Filtros': test_filters(),
    }
    
    print("\n" + "="*70)
    print("📋 RESUMO")
    print("="*70)
    
    for test_name, result in results.items():
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"  {test_name:20s}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "="*70)
    if all_passed:
        print("🎉 DASHBOARD PRONTO PARA USO!")
        print("\n💡 Execute: streamlit run dashboard/app.py")
    else:
        print("⚠️  CORRIJA OS ERROS ANTES DE EXECUTAR O DASHBOARD")
    print("="*70 + "\n")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
