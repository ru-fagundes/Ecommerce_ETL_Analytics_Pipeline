# -*- coding: utf-8 -*-
"""
Dashboard Interativo - E-commerce Analytics
Sistema de visualização e análise de dados em tempo real

Desenvolvido com Streamlit e Plotly
Autor: E-commerce ETL Pipeline
Data: 2025
"""

import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os

# Configuração da página
st.set_page_config(
    page_title="E-commerce Analytics Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .stMetric {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Funções auxiliares
@st.cache_resource
def get_connection():
    """Cria conexão com o database SQLite"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Tentar ambos os locais possíveis do database
    db_paths = [
        os.path.join(base_dir, "ecommerce_sqlite.db"),
        os.path.join(base_dir, "data", "ecommerce_sqlite.db")
    ]
    
    db_path = None
    for path in db_paths:
        if os.path.exists(path):
            db_path = path
            break
    
    if not db_path:
        st.error(f"❌ Database não encontrado. Procurado em:")
        for path in db_paths:
            st.error(f"  - {path}")
        st.info("💡 Execute primeiro: `python scripts/pipeline_carga.py`")
        st.stop()
    
    return sqlite3.connect(db_path, check_same_thread=False)

@st.cache_data(ttl=300)
def carregar_dados(_conn, query):
    """Carrega dados do database com cache"""
    return pd.read_sql(query, _conn)

@st.cache_data(ttl=300)
def calcular_kpis(_conn):
    """Calcula KPIs principais"""
    kpis = {}
    
    # Faturamento Total
    query = "SELECT SUM(valor_total) as total FROM fato_vendas"
    kpis['faturamento'] = pd.read_sql(query, _conn)['total'][0]
    
    # Ticket Médio
    query = """
    SELECT AVG(total_pedido) as ticket
    FROM (
        SELECT pedido_id, SUM(valor_total) as total_pedido
        FROM fato_vendas
        GROUP BY pedido_id
    )
    """
    kpis['ticket_medio'] = pd.read_sql(query, _conn)['ticket'][0]
    
    # Total de Pedidos
    query = "SELECT COUNT(DISTINCT pedido_id) as total FROM fato_vendas"
    kpis['total_pedidos'] = pd.read_sql(query, _conn)['total'][0]
    
    # Clientes Únicos
    query = "SELECT COUNT(DISTINCT cliente_id) as total FROM fato_vendas"
    kpis['clientes_unicos'] = pd.read_sql(query, _conn)['total'][0]
    
    # Itens Vendidos
    query = "SELECT SUM(quantidade) as total FROM fato_vendas"
    kpis['itens_vendidos'] = pd.read_sql(query, _conn)['total'][0]
    
    # Produtos Únicos Vendidos
    query = "SELECT COUNT(DISTINCT produto_id) as total FROM fato_vendas"
    kpis['produtos_vendidos'] = pd.read_sql(query, _conn)['total'][0]
    
    return kpis

# Conexão com database
conn = get_connection()

# Header
st.markdown('<h1 class="main-header">🛒 E-commerce Analytics Dashboard</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar - Filtros
with st.sidebar:
    st.header("🔍 Filtros")
    
    # Filtro de período
    st.subheader("📅 Período")
    
    # Obter range de datas disponíveis
    query_datas = "SELECT MIN(data) as min_data, MAX(data) as max_data FROM dim_tempo"
    datas = pd.read_sql(query_datas, conn)
    
    if not datas.empty and datas['min_data'][0] is not None:
        data_min = pd.to_datetime(datas['min_data'][0])
        data_max = pd.to_datetime(datas['max_data'][0])
        
        data_inicio = st.date_input("Data Início", data_min, min_value=data_min, max_value=data_max)
        data_fim = st.date_input("Data Fim", data_max, min_value=data_min, max_value=data_max)
    else:
        st.warning("Sem dados de datas disponíveis")
        data_inicio = datetime.now().date()
        data_fim = datetime.now().date()
    
    # Filtro de categoria
    st.subheader("📦 Categoria")
    query_categorias = "SELECT DISTINCT categoria FROM dim_produto ORDER BY categoria"
    categorias_df = pd.read_sql(query_categorias, conn)
    categorias = ["Todas"] + categorias_df['categoria'].tolist()
    categoria_selecionada = st.selectbox("Selecione a categoria", categorias)
    
    st.markdown("💡 **Nota**: Filtros aplicados nas próximas versões")
    # TODO: Implementar filtros nas queries
    
    st.markdown("---")
    
    # Botão de atualização
    if st.button("🔄 Atualizar Dashboard", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
    
    # Info
    st.info("💡 Os dados são atualizados automaticamente a cada 5 minutos")

# KPIs Principais
st.header("📊 KPIs Principais")

kpis = calcular_kpis(conn)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric(
        label="💰 Faturamento Total",
        value=f"R$ {kpis['faturamento']:,.2f}",
        delta="Todos os períodos"
    )

with col2:
    st.metric(
        label="📈 Ticket Médio",
        value=f"R$ {kpis['ticket_medio']:,.2f}",
        delta="Por pedido"
    )

with col3:
    st.metric(
        label="🛍️ Pedidos",
        value=f"{kpis['total_pedidos']:,}",
        delta="Total"
    )

with col4:
    st.metric(
        label="👥 Clientes",
        value=f"{kpis['clientes_unicos']:,}",
        delta="Únicos"
    )

with col5:
    st.metric(
        label="📦 Itens Vendidos",
        value=f"{kpis['itens_vendidos']:,}",
        delta="Unidades"
    )

with col6:
    st.metric(
        label="🎯 Produtos",
        value=f"{kpis['produtos_vendidos']:,}",
        delta="Diferentes"
    )

st.markdown("---")

# Gráficos principais
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Faturamento Mensal")
    
    query_faturamento = """
    SELECT 
        strftime('%Y-%m', dt.data) AS mes,
        SUM(f.valor_total) AS faturamento,
        COUNT(DISTINCT f.pedido_id) AS pedidos
    FROM fato_vendas f
    JOIN dim_tempo dt ON f.tempo_id = dt.tempo_id
    GROUP BY mes
    ORDER BY mes
    """
    
    df_fat = carregar_dados(conn, query_faturamento)
    
    if not df_fat.empty:
        fig = go.Figure()
        
        # Linha de faturamento
        fig.add_trace(go.Scatter(
            x=df_fat['mes'],
            y=df_fat['faturamento'],
            mode='lines+markers',
            name='Faturamento',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8),
            hovertemplate='<b>%{x}</b><br>Faturamento: R$ %{y:,.2f}<extra></extra>'
        ))
        
        fig.update_layout(
            height=400,
            xaxis_title="Mês",
            yaxis_title="Faturamento (R$)",
            hovermode='x unified',
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Sem dados de faturamento")

with col2:
    st.subheader("🥧 Participação por Categoria")
    
    query_categoria = """
    SELECT 
        p.categoria,
        SUM(f.valor_total) AS receita
    FROM fato_vendas f
    JOIN dim_produto p ON f.produto_id = p.produto_id
    GROUP BY p.categoria
    ORDER BY receita DESC
    """
    
    df_cat = carregar_dados(conn, query_categoria)
    
    if not df_cat.empty:
        fig = px.pie(
            df_cat,
            values='receita',
            names='categoria',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            hovertemplate='<b>%{label}</b><br>Receita: R$ %{value:,.2f}<br>Participação: %{percent}<extra></extra>'
        )
        
        fig.update_layout(height=400)
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Sem dados de categoria")

# Segunda linha de gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top 10 Produtos Mais Vendidos")
    
    query_top_produtos = """
    SELECT 
        p.nome AS produto,
        SUM(f.quantidade) AS total_vendido,
        SUM(f.valor_total) AS receita
    FROM fato_vendas f
    JOIN dim_produto p ON f.produto_id = p.produto_id
    GROUP BY p.nome
    ORDER BY total_vendido DESC
    LIMIT 10
    """
    
    df_top = carregar_dados(conn, query_top_produtos)
    
    if not df_top.empty:
        fig = px.bar(
            df_top,
            y='produto',
            x='total_vendido',
            orientation='h',
            color='receita',
            color_continuous_scale='Blues',
            labels={'total_vendido': 'Quantidade Vendida', 'receita': 'Receita (R$)'}
        )
        
        fig.update_layout(
            height=400,
            yaxis={'categoryorder': 'total ascending'},
            xaxis_title="Quantidade Vendida",
            yaxis_title="",
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Sem dados de produtos")

with col2:
    st.subheader("👥 Top 10 Clientes por Faturamento")
    
    query_top_clientes = """
    SELECT 
        c.nome AS cliente,
        c.email,
        SUM(f.valor_total) AS total_gasto,
        COUNT(DISTINCT f.pedido_id) AS num_pedidos
    FROM fato_vendas f
    JOIN dim_cliente c ON f.cliente_id = c.cliente_id
    GROUP BY c.nome, c.email
    ORDER BY total_gasto DESC
    LIMIT 10
    """
    
    df_top_cli = carregar_dados(conn, query_top_clientes)
    
    if not df_top_cli.empty:
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            y=df_top_cli['cliente'],
            x=df_top_cli['total_gasto'],
            orientation='h',
            marker=dict(
                color=df_top_cli['total_gasto'],
                colorscale='Greens',
                showscale=False
            ),
            text=df_top_cli['total_gasto'].apply(lambda x: f'R$ {x:,.2f}'),
            textposition='auto',
            hovertemplate='<b>%{y}</b><br>Total Gasto: R$ %{x:,.2f}<br>Pedidos: %{customdata}<extra></extra>',
            customdata=df_top_cli['num_pedidos']
        ))
        
        fig.update_layout(
            height=400,
            yaxis={'categoryorder': 'total ascending'},
            xaxis_title="Total Gasto (R$)",
            yaxis_title="",
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Sem dados de clientes")

# Terceira linha - Análises avançadas
st.markdown("---")
st.header("📊 Análises Avançadas")

tab1, tab2, tab3 = st.tabs(["📅 Vendas por Dia da Semana", "👥 Análise de Clientes", "📊 Série Temporal"])

with tab1:
    query_dia_semana = """
    SELECT 
        CASE dt.dia_semana
            WHEN 0 THEN 'Domingo'
            WHEN 1 THEN 'Segunda'
            WHEN 2 THEN 'Terça'
            WHEN 3 THEN 'Quarta'
            WHEN 4 THEN 'Quinta'
            WHEN 5 THEN 'Sexta'
            WHEN 6 THEN 'Sábado'
        END AS dia,
        dt.dia_semana,
        COUNT(DISTINCT f.pedido_id) AS num_pedidos,
        SUM(f.valor_total) AS faturamento,
        AVG(f.valor_total) AS ticket_medio
    FROM fato_vendas f
    JOIN dim_tempo dt ON f.tempo_id = dt.tempo_id
    GROUP BY dt.dia_semana
    ORDER BY dt.dia_semana
    """
    
    df_dia = carregar_dados(conn, query_dia_semana)
    
    if not df_dia.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.bar(
                df_dia,
                x='dia',
                y='num_pedidos',
                color='faturamento',
                color_continuous_scale='Viridis',
                labels={'num_pedidos': 'Número de Pedidos', 'faturamento': 'Faturamento (R$)'},
                title="Pedidos por Dia da Semana"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.line(
                df_dia,
                x='dia',
                y='ticket_medio',
                markers=True,
                labels={'ticket_medio': 'Ticket Médio (R$)'},
                title="Ticket Médio por Dia da Semana"
            )
            fig.update_traces(line_color='#ff7f0e', line_width=3, marker_size=10)
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Sem dados de dia da semana")

with tab2:
    query_clientes = """
    SELECT 
        c.nome,
        c.email,
        SUM(f.valor_total) AS total_gasto,
        COUNT(DISTINCT f.pedido_id) AS num_pedidos,
        SUM(f.quantidade) AS itens_comprados
    FROM fato_vendas f
    JOIN dim_cliente c ON f.cliente_id = c.cliente_id
    GROUP BY c.nome, c.email
    ORDER BY total_gasto DESC
    LIMIT 20
    """
    
    df_clientes = carregar_dados(conn, query_clientes)
    
    if not df_clientes.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.bar(
                df_clientes.head(15),
                y='nome',
                x='total_gasto',
                orientation='h',
                color='num_pedidos',
                color_continuous_scale='Viridis',
                labels={'total_gasto': 'Valor Total (R$)', 'num_pedidos': 'Pedidos', 'nome': 'Cliente'},
                title="Top 15 Clientes por Valor Total"
            )
            fig.update_layout(yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.scatter(
                df_clientes,
                x='num_pedidos',
                y='total_gasto',
                size='itens_comprados',
                hover_name='nome',
                labels={
                    'num_pedidos': 'Número de Pedidos',
                    'total_gasto': 'Valor Total Gasto (R$)',
                    'itens_comprados': 'Itens Comprados'
                },
                title="Relação: Pedidos x Valor Gasto"
            )
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Sem dados de clientes")

with tab3:
    query_serie = """
    SELECT 
        dt.data,
        SUM(f.valor_total) AS faturamento_diario,
        COUNT(DISTINCT f.pedido_id) AS pedidos_diario,
        AVG(f.valor_total) AS ticket_medio_diario
    FROM fato_vendas f
    JOIN dim_tempo dt ON f.tempo_id = dt.tempo_id
    GROUP BY dt.data
    ORDER BY dt.data
    """
    
    df_serie = carregar_dados(conn, query_serie)
    
    if not df_serie.empty:
        df_serie['data'] = pd.to_datetime(df_serie['data'])
        
        # Calcular médias móveis
        df_serie['ma7'] = df_serie['faturamento_diario'].rolling(window=7, min_periods=1).mean()
        df_serie['ma30'] = df_serie['faturamento_diario'].rolling(window=30, min_periods=1).mean()
        
        fig = go.Figure()
        
        # Faturamento diário
        fig.add_trace(go.Scatter(
            x=df_serie['data'],
            y=df_serie['faturamento_diario'],
            mode='lines',
            name='Faturamento Diário',
            line=dict(color='lightblue', width=1),
            opacity=0.5
        ))
        
        # Média móvel 7 dias
        fig.add_trace(go.Scatter(
            x=df_serie['data'],
            y=df_serie['ma7'],
            mode='lines',
            name='Média Móvel 7 dias',
            line=dict(color='blue', width=2)
        ))
        
        # Média móvel 30 dias
        fig.add_trace(go.Scatter(
            x=df_serie['data'],
            y=df_serie['ma30'],
            mode='lines',
            name='Média Móvel 30 dias',
            line=dict(color='darkblue', width=3)
        ))
        
        fig.update_layout(
            title="Série Temporal de Faturamento com Médias Móveis",
            xaxis_title="Data",
            yaxis_title="Faturamento (R$)",
            hovermode='x unified',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Sem dados de série temporal")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p><strong>E-commerce Analytics Dashboard</strong> | Desenvolvido com ❤️ usando Streamlit e Plotly</p>
    <p>Dados atualizados em: {}</p>
</div>
""".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")), unsafe_allow_html=True)

# Fechar conexão ao final
# conn.close() # Não fechar pois o Streamlit gerencia isso
