# 🌐 Site de Projetos

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-green?logo=django&logoColor=white)
![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-orange)
![License](https://img.shields.io/badge/license-MIT-blue)

Um site desenvolvido em **Django** para organizar e exibir projetos pessoais.  
Possui **API documentada com Swagger**, painel administrativo e deploy configurado para produção.  

---

## ✨ Funcionalidades  

✅ Exibição de projetos com título, descrição e links  
✅ Painel administrativo (CRUD de projetos) via Django Admin  
✅ API documentada com **Swagger**  
✅ Front-end responsivo com HTML, CSS e JS  
✅ Deploy automático no **Vercel** e **Fly.io**  

---

## 📸 Demonstração  

🔗 [Acesse o site online](https://sitedeprojetoskauanjpk.fly.dev)  

![Site funcionando](https://i.imgur.com/cAmEPqu.png)

---

## 🛠️ Tecnologias Utilizadas  

- **Python 3.10+**  
- **Django**  
- **Swagger** (documentação da API)  
- **SQLite** como banco padrão  
- **HTML, CSS, JavaScript**  
- **Docker** (opcional)  
- **Fly.io** para deploy  

---

## 📂 Estrutura do Projeto 
```
Site-De-Projetos/
├── SiteDeProjetos/ # Configurações principais do Django
├── home/ # Página inicial e listagem de projetos
├── sobre/ # Página "Sobre mim"
├── contato/ # Página de contato
├── assets/ # Arquivos estáticos (CSS, JS, imagens)
├── staticfiles/ # Gerado pelo collectstatic
├── manage.py # Script principal do Django
├── requirements.txt # Dependências do projeto
├── Dockerfile # Configuração Docker
├── fly.toml # Configuração de deploy (Fly.io)
├── db.sqlite3 # Banco local
└── README.md # Este arquivo
```

## 🚀 Como Rodar Localmente

# Clone o repositório
```
git clone https://github.com/KauanJPK/Site-De-Projetos.git
cd Site-De-Projetos
```
# Crie e ative o ambiente virtual
```
python -m venv venv
```
# Linux/macOS
```
source venv/bin/activate
```
# Windows
```
venv\Scripts\activate
```

```
```
# Instale as dependências
```
pip install -r requirements.txt
```

# Rode as migrações do banco
```
python manage.py migrate
```
# Inicie o servidor
```
python manage.py runserver
```
Depois, abra no navegador:
👉 http://127.0.0.1:8000/
