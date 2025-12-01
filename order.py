import tkinter as tk
from tkinter import ttk
import json
import os
import tkinter as tk
from header import criar_header
import sys
import subprocess

ARQUIVO_PEDIDO = "pedido_temp.json"

def apagar_pedido_individual(index, frame_itens, pedidos):
    """Apaga um pedido específico pelo índice e atualiza a tela."""
    # Remove o pedido do array
    pedidos.pop(index)

    # Salva a lista atualizada de volta no arquivo
    if pedidos:
        with open(ARQUIVO_PEDIDO, "w", encoding="utf-8") as f:
            json.dump(pedidos, f, ensure_ascii=False, indent=4)
    else:
        # Se não houver pedidos, apaga o arquivo
        if os.path.exists(ARQUIVO_PEDIDO):
            os.remove(ARQUIVO_PEDIDO)

    # Atualiza a tela
    atualizar_tela(frame_itens, pedidos)

def atualizar_tela(frame_itens, pedidos):
    """Atualiza o frame de pedidos."""
    for widget in frame_itens.winfo_children():
        widget.destroy()

    if pedidos:
        for i, pedido in enumerate(pedidos, start=1):
            cliente = pedido.get("cliente", "Cliente")
            itens = pedido.get("itens", {})

            # Frame para cada pedido
            frame_pedido = tk.Frame(frame_itens, bg="#ffdc6a", bd=2, relief="groove")
            frame_pedido.pack(fill="x", pady=5, padx=10)

            # Nome do cliente
            lbl_cliente = tk.Label(frame_pedido, text=f"{i}. Cliente: {cliente}", font=("Segoe UI", 14, "bold"), bg="#ffdc6a")
            lbl_cliente.pack(anchor="w", padx=5, pady=(5,0))

            # Lista de itens
            if itens:
                for nome, qtd in itens.items():
                    tk.Label(frame_pedido, text=f"{nome} x{qtd}", font=("Segoe UI", 12), bg="#ffdc6a").pack(anchor="w", padx=10)
            else:
                tk.Label(frame_pedido, text="Nenhum item no pedido.", bg="#ffdc6a").pack(anchor="w", padx=10)

            # Botão apagar pedido individual
            btn_apagar = tk.Button(frame_pedido, text="Apagar Pedido", bg="#c62828", fg="white",
                                   font=("Segoe UI", 10, "bold"),
                                   command=lambda idx=i-1: apagar_pedido_individual(idx, frame_itens, pedidos))
            btn_apagar.pack(anchor="e", padx=5, pady=5)
    else:
        tk.Label(frame_itens, text="Nenhum pedido feito.", font=("Segoe UI", 12), bg="#ffdc6a").pack(pady=20)

def apagar_todos_pedidos(frame_itens):
    """Apaga todos os pedidos e atualiza a tela."""
    if os.path.exists(ARQUIVO_PEDIDO):
        os.remove(ARQUIVO_PEDIDO)
    atualizar_tela(frame_itens, [])

def order_screen():
    janela = tk.Tk()
    janela.title("Steam Inc - Pedidos")
    janela.geometry("500x600")
    janela.configure(bg="#5d3800")

    criar_header(janela, pagina_atual="order")

    titulo = tk.Label(janela, text="PEDIDOS FEITOS", font=("Bahnschrift Light", 22, "bold"), bg="#ffdc6a")
    titulo.pack(pady=20)

    frame_itens = tk.Frame(janela, bg="#ffdc6a")
    frame_itens.pack(pady=10, fill="both", expand=True)

    # Carregar pedidos existentes
    if os.path.exists(ARQUIVO_PEDIDO):
        try:
            with open(ARQUIVO_PEDIDO, "r", encoding="utf-8") as f:
                pedidos = json.load(f)
        except json.JSONDecodeError:
            pedidos = []
    else:
        pedidos = []

    # Inicializa a tela com os pedidos
    atualizar_tela(frame_itens, pedidos)

    # Botão apagar todos
    btn_apagar_todos = tk.Button(janela, text="APAGAR TODOS OS PEDIDOS", bg="#c62828", fg="white",
                                 font=("Segoe UI", 12, "bold"),
                                 command=lambda: apagar_todos_pedidos(frame_itens))
    btn_apagar_todos.pack(pady=10)

    # Botão fechar
    tk.Button(janela, text="FECHAR", bg="#905700", fg="white", font=("Segoe UI", 12, "bold"),
              command=janela.destroy).pack(pady=20)
    
    def abrir_site():
        webbrowser.open("https://github.com/lucasggoulart/projetoCafeteriaSteamInc")

    separador = ttk.Separator(janela, orient='horizontal')
    separador.pack(fill='x')

    rodape = tk.Frame(janela, bg="#000000")
    rodape.pack(fill="x")

    texto_rodape = tk.Label(
        rodape,
        text="© 2025 Steam Inc. Todos os direitos reservados.\n"
             "Cliente: Felipe Cesare | Desenvolvedor: Lucas Goulart",
        font=("Arial", 9),
        fg="white",
        bg="#000000"
    )
    texto_rodape.pack()

    link_contato = tk.Label(
        rodape,
        text="→ Repositório Oficial do GitHub",
        font=("Arial", 9, "underline"),
        fg="white",
        cursor="hand2",
        bg="#000000"
    )
    link_contato.pack()
    link_contato.bind("<Button-1>", lambda e: abrir_site())

    janela.mainloop()


if __name__ == "__main__":
    order_screen()
