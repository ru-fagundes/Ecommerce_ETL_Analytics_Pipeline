
-- QC: checar nulos em colunas essenciais e duplicados
-- 1) nulos em stg_cliente.cpf
SELECT COUNT(*) as null_cpf FROM stg_cliente WHERE cpf IS NULL OR trim(cpf)='';
-- 2) duplicados em stg_cliente (cpf)
SELECT cpf, COUNT(*) as cnt FROM stg_cliente GROUP BY cpf HAVING cnt>1;
-- 3) pedidos com cliente inexistente
SELECT COUNT(*) as pedidos_sem_cliente FROM stg_pedido p LEFT JOIN stg_cliente c ON p.cliente_id=c.cliente_id WHERE c.cliente_id IS NULL;
-- 4) itens com produto inexistente
SELECT COUNT(*) as itens_sem_produto FROM stg_item_pedido i LEFT JOIN stg_produto pr ON i.produto_id=pr.produto_id WHERE pr.produto_id IS NULL;
-- 5) total de pedidos por status
SELECT status, COUNT(*) as qtd FROM stg_pedido GROUP BY status;
