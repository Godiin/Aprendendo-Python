import customtkinter as ctk

# Configurações iniciais da interface
ctk.set_appearance_mode("dark")     # Opções: "light", "dark", "system"
ctk.set_default_color_theme("blue") # Opções: "blue", "green", "dark-blue"

# Criar a janela principal
janela = ctk.CTk()
janela.title("Calculadora Moderna Ygor")
janela.geometry("300x400")
janela.resizable(False, False)

# Variável para exibir os números/dígitos
entrada = ctk.CTkEntry(janela, width=280, height=60, font=("Arial", 24), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Funções
def clicar(valor):
    entrada.insert("end", valor)

def limpar():
    entrada.delete(0, "end")

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, "end")
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, "end")
        entrada.insert(0, "Erro")

# Botões
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0, 4)
]

for item in botoes:
    texto = item[0]
    linha = item[1]
    coluna = item[2]
    colspan = item[3] if len(item) == 4 else 1

    comando = (
        limpar if texto == "C" else
        calcular if texto == "=" else
        lambda x=texto: clicar(x)
    )

    botao = ctk.CTkButton(janela, text=texto, width=60 * colspan, height=50, command=comando)
    botao.grid(row=linha, column=coluna, columnspan=colspan, padx=5, pady=5)

# Rodar a aplicação
janela.mainloop()

# pyinstaller --onefile --noconsole calculadora.py // gera um arquivo executável do código
