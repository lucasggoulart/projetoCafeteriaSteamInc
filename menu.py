import tkinter as tk
from tkinter import ttk
import json
import os
import tkinter as tk
from header import criar_header
import sys
import subprocess

ARQUIVO_PEDIDO = "pedido_temp.json"

def menu_screen():
    janela = tk.Tk()
    janela.title("Menu")
    janela.geometry("800x600")
    janela.configure(bg="#5d3800")

    criar_header(janela, pagina_atual="menu")

    titulo = tk.Label(janela, text="CARDÁPIO - STEAM INC", font=("Bahnschrift Light", 22, "bold"), bg="#ffdc6a")
    titulo.pack(pady=20)

    cafes = {
        "☕ Expresso": 6.00,
        "☕ Cappuccino": 10.00,
        "☕ Latte": 12.00,
        "☕ Mocha": 14.00,
        "☕ Macchiato": 11.00
    }

    frame_cafes = tk.Frame(janela, bg="#ffdc6a")
    frame_cafes.pack()

    carrinho = {}
    total_var = tk.StringVar(value="Total: R$ 0.00")
    quantidade_labels = {}  # Armazena labels de quantidade

    def atualizar_total():
        total = sum(qtd * cafes[nome] for nome, qtd in carrinho.items())
        total_var.set(f"Total: R$ {total:.2f}")

    def atualizar_quantidade(nome):
        qtd = carrinho.get(nome, 0)
        quantidade_labels[nome].config(text=f"Quantidade: {qtd}")

    def adicionar(nome):
        carrinho[nome] = carrinho.get(nome, 0) + 1
        atualizar_total()
        atualizar_quantidade(nome)

    def remover(nome):
        if nome in carrinho and carrinho[nome] > 0:
            carrinho[nome] -= 1
            if carrinho[nome] == 0:
                del carrinho[nome]
            atualizar_total()
            atualizar_quantidade(nome)

    for nome, preco in cafes.items():
        frame = tk.Frame(frame_cafes, bg="#ffdc6a")
        frame.pack(pady=5)

        lbl = tk.Label(frame, text=f"{nome} - R$ {preco:.2f}", bg="#ffdc6a", font=("Segoe UI", 12))
        lbl.pack(side="left", padx=10)

        btn_add = tk.Button(frame, text="+", width=3, bg="#3ec22d", fg="white",
                            command=lambda n=nome: adicionar(n))
        btn_add.pack(side="left")

        btn_rem = tk.Button(frame, text="-", width=3, bg="#900000", fg="white",
                            command=lambda n=nome: remover(n))
        btn_rem.pack(side="left", padx=5)

        # Label da quantidade
        qtd_label = tk.Label(frame, text="Quantidade: 0", bg="#ffdc6a", font=("Segoe UI", 10, "bold"))
        qtd_label.pack(side="left", padx=10)
        quantidade_labels[nome] = qtd_label

    total_label = tk.Label(janela, textvariable=total_var, font=("Segoe UI", 14, "bold"), bg="#ffdc6a")
    total_label.pack(pady=20)

    tk.Label(janela, text="Seu nome:", bg="#ffdc6a", font=("Segoe UI", 12)).pack()
    nome_entry = tk.Entry(janela, font=("Segoe UI", 12))
    nome_entry.pack(pady=5)

    def finalizar():
        nome = nome_entry.get().strip()
        if not nome:
            nome_entry.insert(0, "Digite seu nome!")
            return
        
        salvar_pedido(nome, carrinho)
        janela.destroy()
        subprocess.Popen([sys.executable, r"C:\Users\gamew\OneDrive\Área de Trabalho\VSCode Projetos\marcos\projetoCafeteriaSteamInc\order.py"])

    btn_finalizar = tk.Button(janela, text="FINALIZAR PEDIDO", bg="#905700", fg="white",
                              font=("Segoe UI", 12, "bold"), command=finalizar)
    btn_finalizar.pack(pady=20)

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

def salvar_pedido(nome_cliente, carrinho):
    """Salva múltiplos pedidos sem sobrescrever os antigos."""
    novo_pedido = {
        "cliente": nome_cliente,
        "itens": carrinho
    }

    pedidos = []

    # Se o arquivo existe, lê os pedidos antigos
    if os.path.exists(ARQUIVO_PEDIDO):
        with open(ARQUIVO_PEDIDO, "r", encoding="utf-8") as f:
            try:
                pedidos = json.load(f)
            except json.JSONDecodeError:
                pedidos = []

    # Adiciona o novo pedido
    pedidos.append(novo_pedido)

    # Salva todos os pedidos de volta
    with open(ARQUIVO_PEDIDO, "w", encoding="utf-8") as f:
        json.dump(pedidos, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    menu_screen()
