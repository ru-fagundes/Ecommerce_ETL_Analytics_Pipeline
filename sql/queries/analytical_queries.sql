
-- Queries analíticas geradas pelo notebook (para passo D)
-- 1) Faturamento mensal
SELECT strftime('%Y-%m', dt.data) AS ano_mes, SUM(f.valor_total) AS faturamento
FROM fato_vendas f JOIN dim_tempo dt ON f.tempo_id = dt.tempo_id
GROUP BY ano_mes ORDER BY ano_mes;

-- 2) Ticket médio por pedido
SELECT AVG(sub.total_por_pedido) AS ticket_medio FROM (
  SELECT pedido_id, SUM(valor_total) AS total_por_pedido
  FROM fato_vendas
  GROUP BY pedido_id
) sub;

-- 3) Top 10 produtos por quantidade vendida
SELECT p.produto_id, p.nome, SUM(f.quantidade) AS total_vendido
FROM fato_vendas f JOIN dim_produto p ON f.produto_id = p.produto_id
GROUP BY p.produto_id, p.nome
ORDER BY total_vendido DESC
LIMIT 10;

-- 4) Top 10 clientes por faturamento
SELECT c.cliente_id, c.nome, SUM(f.valor_total) AS total_gasto
FROM fato_vendas f JOIN dim_cliente c ON f.cliente_id = c.cliente_id
GROUP BY c.cliente_id, c.nome
ORDER BY total_gasto DESC
LIMIT 10;
