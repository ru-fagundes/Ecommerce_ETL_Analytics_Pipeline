# 🚀 Guia: Como Criar o Repositório no GitHub

Este guia irá te ajudar a criar e publicar seu projeto no GitHub em poucos minutos.

---

## 📋 Pré-requisitos

- [ ] Conta no GitHub (crie em https://github.com/join se não tiver)
- [ ] Git instalado no seu computador
  - Verifique: `git --version`
  - Se não tiver, baixe em: https://git-scm.com/download/win

---

## 🔧 Configuração Inicial do Git (Apenas uma vez)

Se é a primeira vez usando Git, configure seu nome e email:

```powershell
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

---

## 📦 Passo a Passo para Criar o Repositório

### 1️⃣ Criar Repositório no GitHub (Website)

1. Acesse: https://github.com/new
2. Preencha os campos:
   - **Repository name:** `ecommerce-etl-analytics-pipeline`
   - **Description:** `Complete end-to-end ETL pipeline for e-commerce analytics using Python, Pandas, and SQLite`
   - **Visibility:** Public (para portfólio)
   - ⚠️ **NÃO marque:** "Add a README file", "Add .gitignore", "Choose a license"
     (já temos esses arquivos!)
3. Clique em **"Create repository"**

### 2️⃣ Configurar Tags/Topics no GitHub

Após criar o repositório, adicione as seguintes **topics** (tags):

1. Clique em ⚙️ **Settings** (ou na engrenagem ao lado de "About")
2. Adicione estas topics:
   ```
   etl, data-engineering, data-analytics, ecommerce, python, pandas, 
   sqlite, data-pipeline, jupyter-notebook, data-warehouse, star-schema, 
   business-intelligence, portfolio-project, data-science
   ```
3. Clique em **"Save changes"**

### 3️⃣ Inicializar Git Localmente

Abra o PowerShell na pasta do projeto e execute:

```powershell
# Navegar até a pasta do projeto (se ainda não estiver nela)
cd "D:\Portfólio\sistema-ecommerce-etl-analise"

# Inicializar repositório Git (se ainda não foi inicializado)
git init

# Adicionar todos os arquivos
git add .

# Verificar o que será commitado (opcional)
git status

# Fazer o primeiro commit
git commit -m "🎉 Initial commit: Complete E-commerce ETL Analytics Pipeline"
```

### 4️⃣ Conectar com GitHub e Fazer Push

**Seu repositório será criado em: https://github.com/ru-fagundes/ecommerce-etl-analytics-pipeline**

```powershell
# Renomear branch para 'main' (se necessário)
git branch -M main

# Adicionar repositório remoto
git remote add origin https://github.com/ru-fagundes/ecommerce-etl-analytics-pipeline.git

# Verificar se foi adicionado corretamente
git remote -v

# Enviar código para GitHub
git push -u origin main
```

**Se pedir autenticação:**
- Use seu **username** do GitHub
- Para senha, use um **Personal Access Token** (não funciona mais com senha normal):
  - Crie em: https://github.com/settings/tokens
  - Click em "Generate new token (classic)"
  - Marque: `repo` (acesso completo)
  - Copie o token e use como senha

---

## ✅ Verificação Final

Após o push, acesse: `https://github.com/ru-fagundes/ecommerce-etl-analytics-pipeline`

Você deve ver:
- ✅ Todos os arquivos do projeto
- ✅ README.md renderizado com badges
- ✅ Pasta `docs/`, `scripts/`, `sql/`, `data/`, `notebooks/`
- ✅ Arquivo LICENSE
- ✅ Topics/tags configuradas

---

## 🎯 Próximos Passos (Opcional)

### 1. Atualizar README com suas informações

Edite o `README.md` e substitua:
- `[Seu Nome]` pelo seu nome
- `[@seu-usuario]` pelo seu username
- Seus links de LinkedIn e email

```powershell
# Após editar:
git add README.md
git commit -m "docs: Update author information"
git push
```

### 2. Adicionar Descrição e Website no GitHub

1. Vá para: `https://github.com/ru-fagundes/ecommerce-etl-analytics-pipeline`
2. Clique em ⚙️ (About)
3. Adicione:
   - **Description:** `Complete end-to-end ETL pipeline for e-commerce analytics`
   - **Website:** Seu portfólio pessoal (se tiver)
   - **Topics:** (já adicionadas anteriormente)
4. Marque: ✅ "Use your GitHub profile"

### 3. Criar GitHub Pages (Opcional - para documentação online)

```powershell
# Criar branch gh-pages
git checkout -b gh-pages
git push -u origin gh-pages

# Voltar para main
git checkout main
```

Depois:
1. Settings → Pages
2. Source: `gh-pages` branch
3. Sua documentação estará em: `https://ru-fagundes.github.io/ecommerce-etl-analytics-pipeline`

---

## 🔄 Comandos Úteis para o Futuro

```powershell
# Ver status do repositório
git status

# Adicionar arquivos modificados
git add .

# Fazer commit
git commit -m "sua mensagem aqui"

# Enviar para GitHub
git push

# Ver histórico de commits
git log --oneline

# Criar nova branch
git checkout -b nome-da-branch

# Ver branches
git branch

# Voltar para main
git checkout main
```

---

## 📱 Divulgação do Projeto

Após publicar, compartilhe:

### LinkedIn
```
🚀 Novo projeto no portfólio!

Desenvolvi um pipeline ETL completo para análise de dados de e-commerce usando Python, Pandas e SQLite.

✨ Destaques:
• Pipeline automatizado de ETL
• Modelo dimensional (Star Schema)
• 2.000 pedidos processados
• R$ 9,6M em faturamento analisado
• Análises interativas em Jupyter

🔗 Confira no GitHub: [link do repo]

#DataEngineering #Python #ETL #DataAnalytics #Portfolio
```

### Twitter/X
```
🚀 Novo projeto: ETL Pipeline para E-commerce

🔄 Automated ETL
📊 Star Schema Design  
💰 R$ 9.6M analyzed
🐍 Python + Pandas + SQLite

Open source! 👇
[link]

#DataEngineering #Python #ETL
```

---

## 🆘 Problemas Comuns

### Erro: "fatal: remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/SEU-USUARIO/ecommerce-etl-analytics-pipeline.git
```

### Erro: "src refspec main does not match any"
```powershell
git branch -M main
git push -u origin main
```

### Erro de autenticação
- Use Personal Access Token em vez de senha
- Ou configure SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

---

## 📞 Ajuda Adicional

- Documentação Git: https://git-scm.com/doc
- GitHub Docs: https://docs.github.com
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf

---

**Boa sorte com seu repositório! 🎉**
