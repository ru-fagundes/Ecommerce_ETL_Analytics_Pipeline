# 📝 Template de Commits Semânticos

Para manter seu histórico de commits organizado, use este padrão:

## 🎯 Formato

```
<tipo>(<escopo>): <mensagem curta>

<descrição detalhada - opcional>
```

---

## 📋 Tipos de Commit

| Tipo | Emoji | Descrição | Exemplo |
|------|-------|-----------|---------|
| `feat` | ✨ | Nova funcionalidade | `feat(etl): add data validation step` |
| `fix` | 🐛 | Correção de bug | `fix(pipeline): correct date parsing error` |
| `docs` | 📚 | Documentação | `docs(readme): update installation steps` |
| `style` | 💄 | Formatação/estilo | `style(scripts): format code with black` |
| `refactor` | ♻️ | Refatoração | `refactor(etl): simplify data loading` |
| `test` | ✅ | Testes | `test(pipeline): add unit tests` |
| `chore` | 🔧 | Tarefas/manutenção | `chore(deps): update pandas to 2.1` |
| `perf` | ⚡ | Performance | `perf(queries): optimize SQL queries` |

---

## 💡 Exemplos Práticos

### Initial Commit
```bash
git commit -m "🎉 Initial commit: Complete E-commerce ETL Analytics Pipeline"
```

### Adicionar feature
```bash
git commit -m "✨ feat(analytics): add customer segmentation analysis"
```

### Corrigir bug
```bash
git commit -m "🐛 fix(etl): handle missing values in produto table"
```

### Atualizar documentação
```bash
git commit -m "📚 docs(readme): add architecture diagram"
```

### Refatoração
```bash
git commit -m "♻️ refactor(pipeline): split ETL into modular functions"
```

### Melhorar performance
```bash
git commit -m "⚡ perf(queries): add indexes to improve query speed"
```

---

## 🚀 Comandos Rápidos

```powershell
# Commit com mensagem curta
git commit -m "tipo(escopo): mensagem"

# Commit com descrição detalhada
git commit -m "tipo(escopo): mensagem curta" -m "Descrição detalhada do que foi feito e por quê"

# Ver histórico de commits
git log --oneline --graph --all

# Alterar último commit (antes do push)
git commit --amend -m "nova mensagem"
```

---

## 📌 Dicas

1. **Seja específico** - "fix: correct SQL query" é melhor que "fix: bug"
2. **Use imperativo** - "add feature" não "added feature"
3. **Máximo 50 caracteres** no título
4. **Use emojis** (opcional) - tornam o histórico visual
5. **Commit frequente** - commits pequenos e focados

---

## 🎨 Exemplo de Histórico Limpo

```
✨ feat(dashboard): add real-time sales dashboard
🐛 fix(etl): handle null values in customer data
📚 docs(api): document all endpoint parameters
♻️ refactor(models): simplify data schema
⚡ perf(db): add database indexes
🔧 chore(deps): update requirements.txt
✅ test(pipeline): add integration tests
💄 style(code): format with black and isort
```

---

**Use este guia para manter seu repositório profissional! 🎯**
