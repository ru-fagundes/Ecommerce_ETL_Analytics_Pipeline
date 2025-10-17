"""
Script ETL simples para carregar CSVs no SQLite
Sistema de Administração de Dados para E-commerce

Este é um script alternativo mais simples que apenas carrega os CSVs
para tabelas staging no SQLite.

Uso:
    python scripts/sqlite_etl.py
"""

import os
import sqlite3
import pandas as pd
from datetime import datetime

# Configurações
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "ecommerce_sqlite.db")
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")

def carregar_dados():
    """Carrega CSVs para SQLite"""
    print(f"📁 Base dir: {BASE_DIR}")
    print(f"💾 Database: {DB_PATH}")
    print(f"📂 Data dir: {DATA_DIR}\n")
    
    try:
        conn = sqlite3.connect(DB_PATH)
        
        # Carregar cada CSV
        arquivos = {
            'stg_cliente': 'clientes.csv',
            'stg_produto': 'produtos.csv',
            'stg_pedido': 'pedidos.csv',
            'stg_item_pedido': 'item_pedido.csv'
        }
        
        for tabela, arquivo in arquivos.items():
            csv_path = os.path.join(DATA_DIR, arquivo)
            print(f"📥 Carregando {arquivo}...")
            
            df = pd.read_csv(csv_path)
            
            # Converter datas se necessário
            if 'data_pedido' in df.columns:
                df['data_pedido'] = pd.to_datetime(df['data_pedido'])
            if 'data_cadastro' in df.columns:
                df['data_cadastro'] = pd.to_datetime(df['data_cadastro'])
            
            df.to_sql(tabela, conn, if_exists='replace', index=False)
            print(f"  ✅ {len(df)} registros em {tabela}")
        
        conn.close()
        print(f"\n✅ Dados carregados com sucesso em {DB_PATH}")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        raise

if __name__ == "__main__":
    carregar_dados()
