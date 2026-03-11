import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

def carregar_excel():
    caminho = filedialog.askopenfilename(
        title="Selecionar arquivo Excel",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )

    if not caminho:
        return

    try:
        dados = pd.read_excel(caminho)

        if dados.empty:
            messagebox.showerror("Erro", "Arquivo sem dados.")
            return

        colunas = dados.columns

        if len(colunas) < 2:
            messagebox.showerror("Erro", "Arquivo precisa ter pelo menos 2 colunas.")
            return

        categorias = dados[colunas[0]]

        dados_numericos = dados.select_dtypes(include="number")

        if dados_numericos.empty:
            messagebox.showerror("Erro", "Nenhuma coluna numérica encontrada.")
            return

        x = np.arange(len(categorias))
        largura = 0.8 / len(dados_numericos.columns)

        plt.figure()

        for i, coluna in enumerate(dados_numericos.columns):
            plt.bar(
                x + i * largura,
                dados_numericos[coluna],
                largura,
                label=coluna
            )

        plt.xticks(x + largura * len(dados_numericos.columns) / 2, categorias)

        plt.title("Comparação de dados")
        plt.xlabel(colunas[0])
        plt.ylabel("Valores")
        plt.legend()

        plt.show()

    except Exception as e:
        messagebox.showerror("Erro", f"Arquivo incompatível.\n{e}")

janela = tk.Tk()
janela.title("Analisador de Excel")
janela.geometry("320x160")

botao = tk.Button(
    janela,
    text="Selecionar Excel",
    command=carregar_excel,
    height=2,
    width=20
)

botao.pack(expand=True)

janela.mainloop()