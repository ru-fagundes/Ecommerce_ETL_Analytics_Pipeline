
-- ddl_analitico.sql (generated star schema)
CREATE TABLE dim_tempo (
    tempo_id SERIAL PRIMARY KEY,
    data DATE NOT NULL UNIQUE,
    dia INTEGER,
    mes INTEGER,
    trimestre INTEGER,
    ano INTEGER,
    dia_semana VARCHAR(20),
    fim_semana BOOLEAN,
    nome_mes VARCHAR(20)
);

CREATE TABLE dim_cliente (
    cliente_id INTEGER PRIMARY KEY,
    cpf VARCHAR(11),
    nome VARCHAR(100),
    email VARCHAR(150),
    telefone VARCHAR(20),
    data_cadastro TIMESTAMP,
    ativo BOOLEAN
);

CREATE TABLE dim_produto (
    produto_id INTEGER PRIMARY KEY,
    nome VARCHAR(200),
    categoria VARCHAR(50),
    preco DECIMAL(10,2)
);

CREATE TABLE fato_vendas (
    venda_id SERIAL PRIMARY KEY,
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
