import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry

# Função para converter a data para o formato UTM com o dia da semana abreviado
def formatar_data_utm(data):
    data_formatada = data.strftime("%Y-%m-%d")  # Formato AAAA-MM-DD
    dia_semana = data.strftime("%a").lower()  # Abreviação do dia da semana (qua, ter, etc.)
    return f"{data_formatada}-{dia_semana}"

# Função para gerar o link UTM
def gerar_utm():
    base_url = entrada_url.get()  # URL base digitada
    utm_source = source_selecionada.get()  # UTM Source
    utm_medium = f"{medium_selecionado.get()}-{local_selecionado.get()}"  # UTM Medium e Local juntos

    # Obtendo a data selecionada e formatando-a para UTM
    data_selecionada_obj = data_selecionada.get_date()  # Obtém o objeto datetime
    data_formatada = formatar_data_utm(data_selecionada_obj)  # Formata a data corretamente para UTM Campaign

    # Gerando o utm_campaign no formato: eve_2024-10-31-qui_1nmtr-1abae-1teai
    utm_campaign = f"{campanha_selecionada.get()}_{data_formatada}_{descricao.get()}_{produto.get()}_{comp_add.get()}"

    utm_content = f"{editoria_selecionada.get()}_{serie_selecionada.get()}"  # UTM Content

    # Criar o link UTM
    utm_link = f"{base_url}?utm_source={utm_source}&utm_medium={utm_medium}&utm_campaign={utm_campaign}&utm_content={utm_content}"

    # Exibir o link UTM gerado
    messagebox.showinfo("Link UTM Gerado", f"Link Gerado: {utm_link}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Gerador de Links UTM")

# Definir cores
cor_fundo = "#000000"  # Preto
cor_campo = "#FFFFFF"  # Branco
cor_botao = "#F8495D"  # Vermelho
cor_titulo = "#00205B"  # Azul escuro

# Configuração do fundo
janela.configure(bg=cor_fundo)

# Definir as colunas
col1 = tk.Frame(janela, bg=cor_fundo)
col1.pack(side=tk.LEFT, padx=20, pady=10)

col2 = tk.Frame(janela, bg=cor_fundo)
col2.pack(side=tk.LEFT, padx=20, pady=10)

col3 = tk.Frame(janela, bg=cor_fundo)
col3.pack(side=tk.LEFT, padx=20, pady=10)

# Estilo para os widgets
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background=cor_fundo, foreground=cor_campo)
style.configure("TEntry", fieldbackground=cor_campo, background=cor_campo, foreground="black")
style.configure("TCombobox", fieldbackground=cor_campo, background=cor_campo, foreground="black")
style.configure("TButton", background=cor_botao, foreground=cor_campo)

# --- Primeira coluna ---
# Label e entrada para URL base
label_url = ttk.Label(col1, text="URL Base:", style="TLabel")
label_url.pack(pady=5)
entrada_url = ttk.Entry(col1, width=40, style="TEntry")
entrada_url.pack(pady=5)

# Label e seleção para UTM Source
label_source = ttk.Label(col1, text="UTM Source:", style="TLabel")
label_source.pack(pady=5)
sources = ["meta", "google", "telegram", "rd-station", "linkedin"]
source_selecionada = ttk.Combobox(col1, values=sources, width=37, style="TCombobox")
source_selecionada.pack(pady=5)

# Label e seleção para UTM Medium
label_medium = ttk.Label(col1, text="UTM Medium:", style="TLabel")
label_medium.pack(pady=5)
mediums = ["whatsapp", "instagram", "facebook", "email", "youtube"]
medium_selecionado = ttk.Combobox(col1, values=mediums, width=37, style="TCombobox")
medium_selecionado.pack(pady=5)

# --- Segunda coluna ---
# Label e seleção para Local (parte do Medium)
label_local = ttk.Label(col2, text="Local (Medium):", style="TLabel")
label_local.pack(pady=5)
locais = ["newsletter", "story", "feed", "bio", "grupo", "comunidade"]
local_selecionado = ttk.Combobox(col2, values=locais, width=37, style="TCombobox")
local_selecionado.pack(pady=5)

# Label e seleção para Campanha
label_campaign = ttk.Label(col2, text="Frente de Campanha:", style="TLabel")
label_campaign.pack(pady=5)
campanhas = ["eve", "tpg", "rmk", "cro", "clu", "mnt"]
campanha_selecionada = ttk.Combobox(col2, values=campanhas, width=37, style="TCombobox")
campanha_selecionada.pack(pady=5)

# Label e entrada para Data com calendário
label_data = ttk.Label(col2, text="Selecione a Data:", style="TLabel")
label_data.pack(pady=5)
data_selecionada = DateEntry(col2, width=20, background='darkblue', foreground='white', borderwidth=2)
data_selecionada.pack(pady=5)

# --- Terceira coluna ---
# Label e entrada para Descrição
label_descricao = ttk.Label(col3, text="Descrição:", style="TLabel")
label_descricao.pack(pady=5)
descricao = ttk.Entry(col3, width=40, style="TEntry")
descricao.pack(pady=5)

# Label e entrada para Produto
label_produto = ttk.Label(col3, text="Produto:", style="TLabel")
label_produto.pack(pady=5)
produto = ttk.Entry(col3, width=40, style="TEntry")
produto.pack(pady=5)

# Label e entrada para Complemento Adicional
label_comp_add = ttk.Label(col3, text="Complemento Adicional:", style="TLabel")
label_comp_add.pack(pady=5)
comp_add = ttk.Entry(col3, width=40, style="TEntry")
comp_add.pack(pady=5)

# --- Fim da terceira coluna ---
# Label e seleção para Editoria
label_editoria = ttk.Label(col3, text="Editoria:", style="TLabel")
label_editoria.pack(pady=5)
editorias = ["informativo", "divulgacao", "branding", "divertido"]
editoria_selecionada = ttk.Combobox(col3, values=editorias, width=37, style="TCombobox")
editoria_selecionada.pack(pady=5)

# Label e seleção para Série
label_serie = ttk.Label(col3, text="Série:", style="TLabel")
label_serie.pack(pady=5)
series = ["tabela", "lancamento", "evento", "palestra"]
serie_selecionada = ttk.Combobox(col3, values=series, width=37, style="TCombobox")
serie_selecionada.pack(pady=5)

# Botão para gerar o link UTM
botao_gerar = ttk.Button(janela, text="Gerar Link UTM", command=gerar_utm)
botao_gerar.pack(pady=20)

# Executar a janela principal
janela.mainloop()
