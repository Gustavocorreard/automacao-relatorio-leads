
# 📧 Automação de Relatórios de Leads por E-mail

Este projeto tem como objetivo automatizar o envio de relatórios de leads por e-mail, utilizando Python. A automação permite gerar e enviar arquivos de forma recorrente, reduzindo tarefas manuais e otimizando processos operacionais.

---

## 🎯 Objetivo

- Gerar um relatório em CSV com dados de leads (simulado ou real).
- Enviar esse relatório automaticamente por e-mail, utilizando Python.

---

## 🔧 Funcionalidades

- 📊 Leitura de dados de leads (planilhas, bases .csv, ou outras fontes).
- 📤 Geração de relatório consolidado.
- ✉️ Envio automático do relatório via e-mail para destinatários definidos.

---

## 🚀 Como Executar o Projeto

### ✅ Pré-requisitos:

- Python 3.x instalado
- Conta de e-mail (Gmail, Outlook, etc.) com acesso SMTP liberado
- Configuração de senha de aplicativo (para Gmail, por exemplo)

### ✅ Instalação:

1. Clone o repositório:
```bash
git clone https://github.com/Gustavocorreard/automacao-relatorio-leads.git
cd automacao-relatorio-leads
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### ✅ Configuração do E-mail:

No script `enviar_relatorio.py`, altere as variáveis:

```python
EMAIL_ORIGEM = "seuemail@gmail.com"
SENHA = "sua_senha_de_aplicativo"
EMAIL_DESTINO = "destinatario@email.com"
```

### ✅ Execução:

Execute o script:

```bash
python src/enviar_relatorio.py
```

Ou rode o notebook:

```bash
notebooks/automacao_relatorio_leads.ipynb
```

---

## 📚 Tecnologias e Bibliotecas

- Python 3
- Pandas
- smtplib (envio de e-mails)
- email.message (construção do e-mail)
- os / datetime (para manipulação de arquivos)

---

## 🛡️ Observações de Segurança

> ⚠️ **Importante:** Nunca compartilhe sua senha de e-mail diretamente no código. Utilize variáveis de ambiente ou arquivos `.env` para proteger suas credenciais.

---

## 📌 Conclusão

Automatizar tarefas como o envio de relatórios ajuda empresas a ganharem eficiência, reduzir erros e otimizar tempo. Este projeto demonstra como Python pode ser uma poderosa ferramenta para automações de processos corporativos.

---

## 👨‍💻 Autor

**Gustavo Correard**  
🔗 [LinkedIn](https://www.linkedin.com/in/gustavocorreard/)  
🔗 [GitHub](https://github.com/Gustavocorreard)
