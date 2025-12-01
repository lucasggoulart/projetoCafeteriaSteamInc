import tkinter as tk
from tkinter import ttk
import subprocess
import sys
from PIL import Image, ImageDraw, ImageTk
from tkinter import font
import webbrowser
from header import criar_header

def abrir_site():
    webbrowser.open("https://github.com/lucasggoulart/projetoCafeteriaSteamInc")

def abrir_cardapio():
    subprocess.Popen([sys.executable, r"C:\Users\gamew\OneDrive\Área de Trabalho\VSCode Projetos\marcos\projetoCafeteriaSteamInc\menu.py"])

def abrir_pedidos():
    subprocess.Popen([sys.executable, r"C:\Users\gamew\OneDrive\Área de Trabalho\VSCode Projetos\marcos\projetoCafeteriaSteamInc\order.py"])

def aboutus_screen():
    janela = tk.Tk()
    janela.title("Steam Inc - Sobre Nós")
    janela.geometry("1000x600")
    janela.configure(bg="#5d3800")

    criar_header(janela, pagina_atual="aboutus")

    #frame_header = tk.Frame(janela, bg="#905700")
    #frame_header.pack(side="top", fill="x")

    frame_principal = tk.Frame(janela, bg="#ffdc6a")
    frame_principal.pack(fill="both", expand=True, pady=40)

    fundo_label = tk.Label(frame_principal, bg="#ffdc6a")
    fundo_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame_esquerda = tk.Frame(frame_principal, bg="#ffdc6a")
    frame_esquerda.pack(side="left", expand=True, padx=20, pady=20)

    label_emoji = tk.Label(frame_esquerda, text="☕", font=("Helvetica", 100), bg="#ffdc6a")
    label_emoji.pack()

    frame_direita = tk.Frame(frame_principal, bg="#ffdc6a")
    frame_direita.pack(side="right", expand=True, padx=20, pady=20)

    #titulo = tk.Label(frame_header, text="STEAM INC", font=("Bahnschrift Light", 25, "bold"), bg="#905700")
    #titulo.pack(side="left") 

    #botao_pedidos = tk.Button(frame_header, text="PEDIDOS", bg="#ffdc6a", fg="black", relief="flat",
                             #padx=15, pady=5, command=abrir_pedidos)
    #botao_pedidos.pack(side="right", padx=5)
    
    #botao_cardapio = tk.Button(frame_header, text="CARDÁPIO", bg="#ffdc6a", fg="black", relief="flat",
                             #padx=15, pady=5, command=abrir_cardapio)
    #botao_cardapio.pack(side="right")

    #fonts = list(font.families())
    #fonts.sort()

    #for f in fonts:
        #print(f)

    subtitulo = tk.Label(frame_direita, text="Quem somos?", font=("Segoe UI Semibold", 24, "bold"), bg="#ffdc6a")
    subtitulo.pack(anchor="w", pady=(10, 5))

    sobre_label = tk.Label(frame_direita, text="SOBRE NÓS:", font=("Segoe UI Semibold", 13, "bold"), bg="#ffdc6a", fg="#6b4f4f")
    sobre_label.pack(anchor="w", pady=(5, 0))

    descricao = (
        "A Steam Inc é uma solução online desenvolvida para modernizar o processo de pedidos em cafeterias. "
        "O sistema simula "
        "um totem de autoatendimento que facilita e agiliza a experiência do cliente.\n\n"
        "Nosso objetivo é oferecer uma plataforma intuitiva, com navegação simples, para que os clientes possam "
        "conhecer nossos produtos, realizar pedidos e finalizar compras com praticidade."
    )

    texto = tk.Label(frame_direita, text=descricao, wraplength=400, justify="left", font=("Segoe UI Light", 13, "bold"), bg="#ffdc6a")
    texto.pack(anchor="w", pady=(5, 15))

    botao_fechar = tk.Button(frame_direita, text="FECHAR", bg="#c26d2d", fg="white", relief="flat",
                             padx=15, pady=5, command=janela.destroy)
    botao_fechar.pack(anchor="w")

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
    aboutus_screen()
