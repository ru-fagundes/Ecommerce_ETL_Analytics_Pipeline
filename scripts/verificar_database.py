"""
Script para verificar a integridade do database SQLite
"""
import sqlite3
import os

def verificar_database():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ecommerce_sqlite.db')
    
    print(f"Database path: {db_path}")
    print(f"Arquivo existe: {os.path.exists(db_path)}\n")
    
    if not os.path.exists(db_path):
        print("❌ Database não encontrado!")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        
        # Listar tabelas
        tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        print(f"✅ Tabelas encontradas ({len(tables)}):")
        for t in tables:
            # Contar registros
            count = cur.execute(f"SELECT COUNT(*) FROM {t[0]}").fetchone()[0]
            print(f"  - {t[0]}: {count} registros")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    verificar_database()
