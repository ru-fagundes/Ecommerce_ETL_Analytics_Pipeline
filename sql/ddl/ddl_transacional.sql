
-- ddl_transacional.sql (generated)
CREATE TABLE cliente (
    cliente_id INTEGER PRIMARY KEY,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    data_cadastro TIMESTAMP,
    ativo BOOLEAN
);

CREATE TABLE produto (
    produto_id INTEGER PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    categoria VARCHAR(50),
    preco DECIMAL(10,2),
    custo DECIMAL(10,2),
    estoque INTEGER
);

CREATE TABLE pedido (
    pedido_id INTEGER PRIMARY KEY,
    cliente_id INTEGER REFERENCES cliente(cliente_id),
    data_pedido TIMESTAMP,
    status VARCHAR(20),
    valor_total DECIMAL(12,2),
    metodo_pagamento VARCHAR(50),
    endereco_id INTEGER
);

CREATE TABLE item_pedido (
    item_pedido_id INTEGER PRIMARY KEY,
    pedido_id INTEGER REFERENCES pedido(pedido_id),
    produto_id INTEGER REFERENCES produto(produto_id),
    quantidade INTEGER,
    valor_unitario DECIMAL(10,2),
    desconto DECIMAL(10,2),
    custo_produto DECIMAL(10,2)
);
