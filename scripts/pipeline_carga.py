"""
Pipeline ETL para carregar dados CSV no SQLite e popular tabelas DW
Sistema de Administração de Dados para E-commerce

Este script:
1. Carrega CSVs da pasta data/raw/ para tabelas staging (stg_*)
2. Processa e popula as dimensões (dim_*)
3. Cria a tabela fato (fato_vendas)

Uso:
    python scripts/pipeline_carga.py
"""

import os
import sqlite3
import pandas as pd
from datetime import datetime

# Configurações
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "ecommerce_sqlite.db")
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")

def log(mensagem):
    """Log com timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {mensagem}")

def criar_conexao():
    """Cria conexão com SQLite"""
    try:
        conn = sqlite3.connect(DB_PATH)
        log(f"✅ Conectado ao database: {DB_PATH}")
        return conn
    except Exception as e:
        log(f"❌ Erro ao conectar: {e}")
        raise

def carregar_staging(conn):
    """Carrega CSVs para tabelas staging"""
    log("📥 Iniciando carga das tabelas staging...")
    
    arquivos = {
        'stg_cliente': 'clientes.csv',
        'stg_produto': 'produtos.csv',
        'stg_pedido': 'pedidos.csv',
        'stg_item_pedido': 'item_pedido.csv'
    }
    
    for tabela, arquivo in arquivos.items():
        try:
            csv_path = os.path.join(DATA_DIR, arquivo)
            df = pd.read_csv(csv_path)
            
            # Converter colunas de data
            if 'data_' in arquivo or 'pedido' in arquivo:
                for col in df.columns:
                    if 'data' in col.lower():
                        df[col] = pd.to_datetime(df[col], errors='coerce')
            
            df.to_sql(tabela, conn, if_exists='replace', index=False)
            log(f"  ✅ {tabela}: {len(df)} registros carregados de {arquivo}")
            
        except Exception as e:
            log(f"  ❌ Erro ao carregar {tabela}: {e}")
            raise

def popular_dimensoes(conn):
    """Popula tabelas dimensão a partir do staging"""
    log("\n🔄 Populando dimensões...")
    
    # dim_cliente
    try:
        query_cliente = """
        INSERT OR REPLACE INTO dim_cliente 
        SELECT cliente_id, cpf, nome, email, telefone, data_cadastro, ativo
        FROM stg_cliente
        """
        conn.execute(query_cliente)
        count = conn.execute("SELECT COUNT(*) FROM dim_cliente").fetchone()[0]
        log(f"  ✅ dim_cliente: {count} registros")
    except Exception as e:
        log(f"  ❌ Erro dim_cliente: {e}")
    
    # dim_produto
    try:
        query_produto = """
        INSERT OR REPLACE INTO dim_produto (produto_id, nome, categoria, preco)
        SELECT produto_id, nome, categoria, preco
        FROM stg_produto
        """
        conn.execute(query_produto)
        count = conn.execute("SELECT COUNT(*) FROM dim_produto").fetchone()[0]
        log(f"  ✅ dim_produto: {count} registros")
    except Exception as e:
        log(f"  ❌ Erro dim_produto: {e}")
    
    conn.commit()

def popular_fato(conn):
    """Popula tabela fato_vendas"""
    log("\n📊 Populando fato_vendas...")
    
    try:
        # Primeiro popular dim_tempo
        log("  📅 Populando dim_tempo...")
        query_tempo = """
        INSERT OR IGNORE INTO dim_tempo (data, dia, mes, trimestre, ano, dia_semana, fim_semana, nome_mes)
        SELECT DISTINCT
            DATE(data_pedido) as data,
            CAST(strftime('%d', data_pedido) AS INTEGER) as dia,
            CAST(strftime('%m', data_pedido) AS INTEGER) as mes,
            CASE 
                WHEN CAST(strftime('%m', data_pedido) AS INTEGER) <= 3 THEN 1
                WHEN CAST(strftime('%m', data_pedido) AS INTEGER) <= 6 THEN 2
                WHEN CAST(strftime('%m', data_pedido) AS INTEGER) <= 9 THEN 3
                ELSE 4
            END as trimestre,
            CAST(strftime('%Y', data_pedido) AS INTEGER) as ano,
            CASE CAST(strftime('%w', data_pedido) AS INTEGER)
                WHEN 0 THEN 'Domingo'
                WHEN 1 THEN 'Segunda'
                WHEN 2 THEN 'Terça'
                WHEN 3 THEN 'Quarta'
                WHEN 4 THEN 'Quinta'
                WHEN 5 THEN 'Sexta'
                WHEN 6 THEN 'Sábado'
            END as dia_semana,
            CASE WHEN CAST(strftime('%w', data_pedido) AS INTEGER) IN (0, 6) THEN 1 ELSE 0 END as fim_semana,
            CASE CAST(strftime('%m', data_pedido) AS INTEGER)
                WHEN 1 THEN 'Janeiro' WHEN 2 THEN 'Fevereiro' WHEN 3 THEN 'Março'
                WHEN 4 THEN 'Abril' WHEN 5 THEN 'Maio' WHEN 6 THEN 'Junho'
                WHEN 7 THEN 'Julho' WHEN 8 THEN 'Agosto' WHEN 9 THEN 'Setembro'
                WHEN 10 THEN 'Outubro' WHEN 11 THEN 'Novembro' WHEN 12 THEN 'Dezembro'
            END as nome_mes
        FROM stg_pedido
        """
        conn.execute(query_tempo)
        tempo_count = conn.execute("SELECT COUNT(*) FROM dim_tempo").fetchone()[0]
        log(f"    ✅ dim_tempo: {tempo_count} registros")
        
        # Agora popular fato_vendas
        query_fato = """
        INSERT OR REPLACE INTO fato_vendas (tempo_id, pedido_id, cliente_id, produto_id, quantidade, valor_unitario, valor_desconto, valor_total, custo_produto)
        SELECT 
            dt.tempo_id,
            p.pedido_id,
            p.cliente_id,
            ip.produto_id,
            ip.quantidade,
            ip.valor_unitario,
            COALESCE(ip.desconto, 0) as valor_desconto,
            (ip.quantidade * ip.valor_unitario - COALESCE(ip.desconto, 0)) as valor_total,
            ip.custo_produto
        FROM stg_item_pedido ip
        JOIN stg_pedido p ON ip.pedido_id = p.pedido_id
        JOIN dim_tempo dt ON DATE(p.data_pedido) = dt.data
        """
        conn.execute(query_fato)
        count = conn.execute("SELECT COUNT(*) FROM fato_vendas").fetchone()[0]
        conn.commit()
        log(f"  ✅ fato_vendas: {count} registros")
    except Exception as e:
        log(f"  ❌ Erro fato_vendas: {e}")
        raise

def executar_pipeline():
    """Executa pipeline ETL completo"""
    log("🚀 Iniciando Pipeline ETL")
    log(f"📁 Diretório base: {BASE_DIR}")
    log(f"💾 Database: {DB_PATH}")
    log(f"📂 Dados CSV: {DATA_DIR}\n")
    
    try:
        conn = criar_conexao()
        
        # Etapa 1: Staging
        carregar_staging(conn)
        
        # Etapa 2: Dimensões
        popular_dimensoes(conn)
        
        # Etapa 3: Fato
        popular_fato(conn)
        
        conn.close()
        
        log("\n✅ Pipeline ETL concluído com sucesso!")
        
    except Exception as e:
        log(f"\n❌ Pipeline falhou: {e}")
        raise

if __name__ == "__main__":
    executar_pipeline()
