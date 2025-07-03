# 🔐 Gerenciador de Senhas em Python

## 📌 Descrição
Projeto pessoal para gerenciar senhas de forma simples, com interface gráfica usando Tkinter e banco de dados local (postgresql). O objetivo é armazenar senhas com segurança, oferecendo funções de cadastro, edição, exclusão e consulta.

---

## 🚀 Funcionalidades previstas

- [ ] Cadastro de senhas (serviço, login, senha)
- [ ] Listagem de senhas salvas
- [ ] Busca por nome do serviço
- [ ] Edição de senhas
- [ ] Exclusão de senhas
- [ ] Copiar senha para área de transferência
- [ ] Interface com Tkinter
- [ ] Criptografia das senhas com Fernet
- [ ] Banco de dados local com Postgresql

---

## 🛠 Tecnologias utilizadas

- Python 3.12+
- Tkinter (GUI)
- Postgresql
- Cryptography (para proteger as senhas)

---

## 🧩 Estrutura do Projeto (planejada)
<pre> gerenciador_senhas/
  ├── main.py # Interface gráfica
  ├── banco.py # Conexão e controle do banco
  ├── seguranca.py # Funções de criptografia
  ├── utils.py # Funções auxiliares
  └── README.md # Documentação do projeto </pre>

---

🔐 Sobre a segurança
As senhas são criptografadas com a biblioteca Fernet da Cryptography, garantindo que os dados armazenados não fiquem expostos em texto puro. A chave de criptografia é gerada e armazenada localmente.


💡 Melhorias futuras
Suporte a múltiplos perfis de usuário
Exportação das senhas criptografadas
Geração de senhas fortes
Autenticação para acesso ao sistema

👨‍💻 Autor
Rafael Toledo

![Concept Art](concept01.png)

