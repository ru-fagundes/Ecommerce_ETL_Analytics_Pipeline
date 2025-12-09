# -*- coding: utf-8 -*-
"""
Script para criar tabelas analíticas (Star Schema) no SQLite
"""

import sqlite3
import os

# Caminho do banco de dados
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ecommerce_sqlite.db')

# DDL adaptado para SQLite
ddl_commands = [
    """
    CREATE TABLE IF NOT EXISTS dim_tempo (
        tempo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE NOT NULL UNIQUE,
        dia INTEGER,
        mes INTEGER,
        trimestre INTEGER,
        ano INTEGER,
        dia_semana VARCHAR(20),
        fim_semana BOOLEAN,
        nome_mes VARCHAR(20)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS dim_cliente (
        cliente_id INTEGER PRIMARY KEY,
        cpf VARCHAR(11),
        nome VARCHAR(100),
        email VARCHAR(150),
        telefone VARCHAR(20),
        data_cadastro TIMESTAMP,
        ativo BOOLEAN
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS dim_produto (
        produto_id INTEGER PRIMARY KEY,
        nome VARCHAR(200),
        categoria VARCHAR(50),
        preco DECIMAL(10,2)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS fato_vendas (
        venda_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tempo_id INTEGER REFERENCES dim_tempo(tempo_id),
        pedido_id INTEGER,
        cliente_id INTEGER REFERENCES dim_cliente(cliente_id),
        produto_id INTEGER REFERENCES dim_produto(produto_id),
        quantidade INTEGER,
        valor_unitario DECIMAL(10,2),
        valor_desconto DECIMAL(10,2),
        valor_total DECIMAL(12,2),
        custo_produto DECIMAL(10,2)
    );
    """
]

def criar_tabelas_analiticas():
    """Cria as tabelas analíticas no banco SQLite"""
    try:
        print(f"📁 Conectando ao banco: {db_path}")
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        
        print("\n🔨 Criando tabelas analíticas...")
        for i, ddl in enumerate(ddl_commands, 1):
            try:
                cur.execute(ddl)
                tabela = ddl.split("TABLE IF NOT EXISTS ")[1].split(" (")[0]
                print(f"  ✅ {tabela} criada com sucesso")
            except Exception as e:
                print(f"  ❌ Erro ao criar tabela {i}: {e}")
        
        conn.commit()
        
        # Verificar tabelas criadas
        tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()
        print(f"\n✅ Total de tabelas no banco: {len(tables)}")
        for t in tables:
            print(f"   - {t[0]}")
        
        conn.close()
        print("\n✨ Tabelas analíticas criadas com sucesso!")
        return True
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        return False

if __name__ == "__main__":
    criar_tabelas_analiticas()
