# -*- coding: utf-8 -*-
"""
Script de teste para validar todos os componentes do projeto
"""

import os
import sys
import sqlite3

def test_database():
    """Testa a conexão e estrutura do database"""
    print("\n" + "="*70)
    print("🔍 TESTANDO DATABASE")
    print("="*70)
    
    # Procurar database
    db_paths = [
        "ecommerce_sqlite.db",
        "data/ecommerce_sqlite.db"
    ]
    
    db_path = None
    for path in db_paths:
        if os.path.exists(path):
            db_path = path
            break
    
    if not db_path:
        print("❌ Database não encontrado!")
        print("📝 Execute: python scripts/pipeline_carga.py")
        return False
    
    print(f"✅ Database encontrado: {db_path}")
    
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        
        # Listar tabelas
        tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        print(f"\n📊 Tabelas encontradas ({len(tables)}):")
        for table in tables:
            count = cur.execute(f"SELECT COUNT(*) FROM {table[0]}").fetchone()[0]
            print(f"  ✅ {table[0]}: {count:,} registros")
        
        # Testar query básica
        if 'fato_vendas' in [t[0] for t in tables]:
            faturamento = cur.execute("SELECT SUM(valor_total) FROM fato_vendas").fetchone()[0]
            if faturamento:
                print(f"\n💰 Faturamento total: R$ {faturamento:,.2f}")
        
        conn.close()
        print("\n✅ Database OK!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar database: {e}")
        return False

def test_imports():
    """Testa se todas as bibliotecas necessárias estão instaladas"""
    print("\n" + "="*70)
    print("📦 TESTANDO DEPENDÊNCIAS")
    print("="*70)
    
    required = {
        'pandas': 'Manipulação de dados',
        'matplotlib': 'Gráficos estáticos',
        'seaborn': 'Visualizações estatísticas',
        'streamlit': 'Dashboard interativo',
        'plotly': 'Gráficos interativos',
        'numpy': 'Operações numéricas',
    }
    
    all_ok = True
    for module, desc in required.items():
        try:
            __import__(module)
            print(f"  ✅ {module:15s} - {desc}")
        except ImportError:
            print(f"  ❌ {module:15s} - NÃO INSTALADO")
            all_ok = False
    
    if all_ok:
        print("\n✅ Todas as dependências instaladas!")
    else:
        print("\n❌ Instale dependências faltantes: pip install -r config/requirements.txt")
    
    return all_ok

def test_files():
    """Testa se todos os arquivos necessários existem"""
    print("\n" + "="*70)
    print("📁 TESTANDO ARQUIVOS")
    print("="*70)
    
    required_files = [
        ('scripts/pipeline_carga.py', 'Pipeline ETL'),
        ('scripts/analise_dados.py', 'Análise de dados'),
        ('dashboard/app.py', 'Dashboard Streamlit'),
        ('notebooks/notebook_etl_analysis.ipynb', 'Notebook Jupyter'),
        ('README.md', 'Documentação principal'),
        ('QUICK_START.md', 'Guia rápido'),
        ('config/requirements.txt', 'Dependências'),
    ]
    
    all_ok = True
    for filepath, desc in required_files:
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"  ✅ {filepath:40s} - {desc} ({size:,} bytes)")
        else:
            print(f"  ❌ {filepath:40s} - NÃO ENCONTRADO")
            all_ok = False
    
    return all_ok

def test_data_files():
    """Testa se os arquivos CSV existem"""
    print("\n" + "="*70)
    print("📂 TESTANDO DADOS CSV")
    print("="*70)
    
    csv_files = [
        'data/raw/clientes.csv',
        'data/raw/produtos.csv',
        'data/raw/pedidos.csv',
        'data/raw/item_pedido.csv'
    ]
    
    all_ok = True
    for csv_file in csv_files:
        if os.path.exists(csv_file):
            size = os.path.getsize(csv_file)
            lines = sum(1 for _ in open(csv_file, encoding='utf-8'))
            print(f"  ✅ {csv_file:35s} - {lines:,} linhas ({size:,} bytes)")
        else:
            print(f"  ❌ {csv_file:35s} - NÃO ENCONTRADO")
            all_ok = False
    
    return all_ok

def main():
    """Executa todos os testes"""
    print("\n" + "="*70)
    print("🧪 TESTE COMPLETO DO PROJETO")
    print("E-commerce ETL Analytics Pipeline")
    print("="*70)
    
    results = {
        'Arquivos': test_files(),
        'Dados CSV': test_data_files(),
        'Dependências': test_imports(),
        'Database': test_database(),
    }
    
    print("\n" + "="*70)
    print("📋 RESUMO DOS TESTES")
    print("="*70)
    
    for test_name, result in results.items():
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"  {test_name:20s}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "="*70)
    if all_passed:
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("\n💡 Próximos passos:")
        print("  1. Execute o dashboard: streamlit run dashboard/app.py")
        print("  2. Abra o notebook: jupyter notebook notebooks/notebook_etl_analysis.ipynb")
        print("  3. Gere análises: python scripts/analise_dados.py")
    else:
        print("⚠️  ALGUNS TESTES FALHARAM")
        print("\n💡 Corrija os problemas acima antes de continuar")
    print("="*70 + "\n")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
