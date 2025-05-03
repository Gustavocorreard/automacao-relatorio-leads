
# 📊 Projeto: Automação de Relatório de Leads com Python

Este projeto demonstra como automatizar a geração de um relatório com dados de leads utilizando Python.  
Ele inclui leitura de planilha, análise de dados, geração de gráficos e envio automático de e-mail com PDF.

---

## 🔧 Tecnologias Utilizadas

- Python 3.10+
- pandas
- matplotlib
- fpdf
- yagmail
- Jupyter Notebook (opcional)

---

## 🧭 Etapas do Projeto

1. Leitura dos dados de leads (`leads.xlsx`)
2. Análise de dados: canais de aquisição e status dos leads
3. Geração de dois gráficos:
   - Leads por Canal
   - Status dos Leads
4. Exportação para um PDF automático
5. Envio do relatório por e-mail com `yagmail`

---

## 🚀 Como Rodar o Projeto

### 🔹 Versão Notebook:
1. Abra o arquivo `automacao_relatorio_leads.ipynb` no Jupyter ou Google Colab
2. Execute as células em ordem

### 🔹 Versão Script:
1. Instale as dependências:  
   ```bash
   pip install pandas matplotlib fpdf yagmail
   ```
2. Execute:  
   ```bash
   python automacao_relatorio_leads.py
   ```

---

## 🛡️ Segurança
Para enviar e-mails via Gmail, é necessário usar uma [senha de app](https://myaccount.google.com/apppasswords).

---

## 📁 Estrutura do Projeto

```
automacao-relatorio/
├── dados/                        # Planilha de entrada
├── output/                       # Gráficos e relatórios gerados
├── scripts/
│   ├── automacao_relatorio_leads.ipynb
│   └── automacao_relatorio_leads.py
├── README.md
└── .gitignore
```

---

## 📬 Contato

Feito por **@pyautoGus**. 
Meu perfil no [LinkedIn](https://www.linkedin.com/in/gustavo-correard/)
