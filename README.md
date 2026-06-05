# CRUD — Rede Hospitalar Cuidar
Aplicação back-end Flask com MySQL para cadastro de pacientes.

---

## Pré-requisitos (sua máquina local)
- Python 3.10+
- MySQL rodando localmente (ou acesso ao Ubuntu Server)

---

## 1. Configurar o banco de dados

No MySQL do Ubuntu Server (192.168.18.75), execute:

```bash
mysql -u root -p < setup_db.sql
```

Isso cria o banco `hospital_cuidar`, o usuário `cuidar_user` e a tabela `pacientes`.

---

## 2. Instalar dependências localmente

```bash
pip install -r requirements.txt
```

---

## 3. Rodar localmente para testar

```bash
python app.py
```

Acesse: http://localhost:5000

---

## 4. Subir no GitHub

```bash
git init
git add .
git commit -m "feat: aplicacao CRUD Hospital Cuidar"
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git push -u origin main
```

---

## 5. Deploy no Ubuntu Server (192.168.18.75)

Conecte via SSH:
```bash
ssh usuario@192.168.18.75
```

Clone o repositório:
```bash
cd /var/www/
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git crud-cuidar
cd crud-cuidar
```

Instale as dependências no servidor:
```bash
pip3 install -r requirements.txt
```

Execute o banco:
```bash
mysql -u root -p < setup_db.sql
```

Rode a aplicação:
```bash
python3 app.py
```

Acesse pelo navegador: http://192.168.18.75:5000

---

## Estrutura do projeto

```
crud-cuidar/
├── app.py               # Aplicação principal Flask (rotas CRUD)
├── setup_db.sql         # Script de criação do banco e tabela
├── requirements.txt     # Dependências Python
├── README.md            # Este arquivo
└── templates/
    ├── base.html        # Layout base com identidade visual
    ├── index.html       # Listagem de pacientes
    ├── cadastrar.html   # Formulário de cadastro
    └── editar.html      # Formulário de edição
```

---

## Funcionalidades
- Listar todos os pacientes cadastrados
- Cadastrar novo paciente (nome, CPF, nascimento, unidade)
- Editar registro existente
- Remover paciente com confirmação

## Unidades disponíveis
- Matriz - BH
- Secretaria
- UPA 1
- UPA 2
- UPA 3
