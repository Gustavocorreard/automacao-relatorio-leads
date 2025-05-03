# Este notebook mostra o passo a passo para automatizar a geração de um relatório a partir de uma planilha de leads.

# Vamos:
# 1. Ler os dados
# 2. Analisar as informações
# 3. Gerar gráficos
# 4. Criar um PDF com os resultados

######################################################
# IMPORTS:
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
import yagmail

# ## 📥 1. Leitura dos Dados
df = pd.read_excel('leads.xlsx')
df.head()


# ## 📊 2. Gráfico de Leads por Canal

canal_counts = df['Canal'].value_counts()

plt.figure(figsize=(8, 5))
ax = canal_counts.plot(kind='bar', color='blue')
plt.title('Leads por Canal')
plt.xlabel('Canal')
plt.ylabel('Quantidade de Leads')

# Adicionar rótulos
for i in ax.patches:
    ax.text(i.get_x() + i.get_width()/2,
            i.get_height() + 0.5,
            str(int(i.get_height())),
            ha='center')

plt.tight_layout()
# Salvando o gráfico em png
plt.savefig("grafico_canal_labels.png")
plt.close()


# ## 🥧 3. Gráfico de Distribuição de Status dos Leads

status_counts = df['Status'].value_counts()

plt.figure(figsize=(7, 5))
ax = status_counts.plot(kind='barh', color='teal')
plt.title('Distribuição de Status dos Leads')
plt.xlabel('Quantidade')
plt.ylabel('Status')

# Adicionar rótulos
for i in ax.patches:
    ax.text(i.get_width() + 0.5,
            i.get_y() + i.get_height()/2,
            str(int(i.get_width())),
            va='center')

plt.tight_layout()
# Salvando o gráfico em png
plt.savefig("grafico_status_barras_horizontal_labels.png")
plt.close()


# ## 📄 5. Gerando PDF com os Gráficos
# Caminhos para os gráficos
grafico_canal_final = "/content/grafico_canal_labels.png"
grafico_status_final = "/content/grafico_status_barras_horizontal_labels.png"
pdf_path_final = "relatorio_completo_leads_final.pdf"

# Criando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt="Relatório de Leads", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Leads por Canal de Aquisição", align='C', ln=True)
pdf.image(grafico_canal_final, x=10, y=30, w=180)

# Nova página para o segundo gráfico
pdf.add_page()
pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt="Distribuição de Status dos Leads", align='C', ln=True)
pdf.image(grafico_status_final, x=20, y=30, w=170)

# Salvar o PDF
pdf.output(pdf_path_final)

# ## ✉️ Envio do Relatório por E-mail

# ### ✉️ Configurar o Gmail para uso com yagmail
# ######1 - Ative a verificação em duas etapas na sua conta Gmail:
#     https://myaccount.google.com/security
# 
# #####2 - Gere uma senha de app nesta página:
#     https://myaccount.google.com/apppasswords
# 
#   * Copie e guarde essa senha: ela será usada no script.

# Dados do remetente
usuario = "seuemail@gmail.com"
senha = "sua_senha_de_app"  # gerada no passo anterior

# Inicializar cliente yagmail
yag = yagmail.SMTP(user=usuario, password=senha)

# Informações do e-mail
destinatario = "destino@email.com"
assunto = "Relatório Automático de Leads"
corpo = "Olá,\n\nSegue em anexo o relatório automático de leads gerado com Python.\n\nAtenciosamente,\nPyAutoGus 🤖"

# Anexo
anexo = "relatorio_completo_leads_final.pdf"

# Enviar
yag.send(to=destinatario, subject=assunto, contents=corpo, attachments=anexo)

print("✅ E-mail enviado com sucesso!")

